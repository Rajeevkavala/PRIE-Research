import docx
import zipfile
import re
import os
import win32com.client

base_docx = r"d:\4-1 AD\All College Docs and ppts\Documentations\PDR\PRIE-Research\test_inject_base.docx"
out_docx = r"d:\4-1 AD\All College Docs and ppts\Documentations\PDR\PRIE-Research\test_inject_out.docx"

d = docx.Document()
d.add_paragraph("Paragraph before chart")
d.add_paragraph("[[CHART_5]]")
d.add_paragraph("Paragraph after chart")
d.save(base_docx)

# Extract chart from test_chart_doc.docx
with zipfile.ZipFile("test_chart_doc.docx", "r") as z_src:
    c1_xml = z_src.read("word/charts/chart1.xml")
    c1_rels = z_src.read("word/charts/_rels/chart1.xml.rels")
    emb_xlsx = z_src.read("word/embeddings/Microsoft_Excel_Worksheet.xlsx")

drawing_xml = """<w:r><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0">
<wp:extent cx="3048000" cy="1828800"/>
<wp:effectExtent l="0" t="0" r="0" b="0"/>
<wp:docPr id="5001" name="Chart 5"/>
<wp:cNvGraphicFramePr/>
<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
<a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/chart">
<c:chart xmlns:c="http://schemas.openxmlformats.org/drawingml/2006/chart" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" r:id="rIdChart5"/>
</a:graphicData>
</a:graphic>
</wp:inline></w:drawing></w:r>"""

# Read base_docx zip
files = {}
with zipfile.ZipFile(base_docx, "r") as z_in:
    for name in z_in.namelist():
        files[name] = z_in.read(name)

# 1. Update word/document.xml
doc_xml = files["word/document.xml"].decode("utf-8")
doc_xml = re.sub(r"<w:r[^>]*><w:t>\[\[CHART_5\]\]</w:t></w:r>", drawing_xml, doc_xml)
files["word/document.xml"] = doc_xml.encode("utf-8")

# 2. Update word/_rels/document.xml.rels
rels_xml = files["word/_rels/document.xml.rels"].decode("utf-8")
rel_entry = '<Relationship Id="rIdChart5" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/chart" Target="charts/chart1.xml"/>'
rels_xml = rels_xml.replace("</Relationships>", f"{rel_entry}</Relationships>")
files["word/_rels/document.xml.rels"] = rels_xml.encode("utf-8")

# 3. Update [Content_Types].xml
ct_xml = files["[Content_Types].xml"].decode("utf-8")
ct_entries = """<Override PartName="/word/charts/chart1.xml" ContentType="application/vnd.openxmlformats-officedocument.drawingml.chart+xml"/>
<Override PartName="/word/embeddings/Microsoft_Excel_Worksheet1.xlsx" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"/>"""
ct_xml = ct_xml.replace("</Types>", f"{ct_entries}</Types>")
files["[Content_Types].xml"] = ct_xml.encode("utf-8")

# 4. Add chart files
files["word/charts/chart1.xml"] = c1_xml
# Update chart1.xml.rels target
c1_rels_str = c1_rels.decode("utf-8").replace("Microsoft_Excel_Worksheet.xlsx", "Microsoft_Excel_Worksheet1.xlsx")
files["word/charts/_rels/chart1.xml.rels"] = c1_rels_str.encode("utf-8")
files["word/embeddings/Microsoft_Excel_Worksheet1.xlsx"] = emb_xlsx

# Write to out_docx
with zipfile.ZipFile(out_docx, "w", zipfile.ZIP_DEFLATED) as z_out:
    for name, content in files.items():
        z_out.writestr(name, content)

print("Created injected document:", out_docx)

# Verify opening in Word via COM
word = win32com.client.Dispatch("Word.Application")
word.Visible = False
try:
    wdoc = word.Documents.Open(out_docx)
    print("Word successfully opened injected doc! InlineShapes count:", wdoc.InlineShapes.Count)
    if wdoc.InlineShapes.Count > 0:
        shape = wdoc.InlineShapes(1)
        print("Shape has chart:", shape.HasChart)
        if shape.HasChart:
            print("Chart type:", shape.Chart.ChartType)
            print("Chart title (if any):", shape.Chart.HasTitle)
    wdoc.Close(False)
    print("SUCCESS: Native DrawingML Chart verified by Word COM!")
finally:
    word.Quit()
