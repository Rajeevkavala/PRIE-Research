"""Generate a clean sample .docx with python-docx.

Canonical reference for document creation. Demonstrates the patterns that keep
output well-formed:
- explicit page size and margins
- a default font set on the Normal style
- heading styles (carry outline levels, so a TOC can find them)
- real bullet and numbered lists via built-in styles (never typed/unicode bullets)
- a table with explicit column widths set on every cell
- header text and a page-number footer field

Usage:
    python create_sample_docx.py [output.docx]
"""

import sys

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt


def _add_page_number(paragraph) -> None:
    """Insert a PAGE field so Word renders the live page number."""
    run = paragraph.add_run()
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = "PAGE"
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    run._r.append(begin)
    run._r.append(instr)
    run._r.append(end)


def _set_col_widths(table, widths) -> None:
    """Column widths only stick when set on every cell."""
    table.autofit = False
    for row in table.rows:
        for idx, width in enumerate(widths):
            row.cells[idx].width = width


def build(output_path: str) -> str:
    doc = Document()

    section = doc.sections[0]
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    section.left_margin = section.right_margin = Inches(1)
    section.top_margin = section.bottom_margin = Inches(1)

    normal = doc.styles["Normal"]
    normal.font.name = "Arial"
    normal.font.size = Pt(11)

    section.header.paragraphs[0].text = "Sarvam DOCX Sample"
    footer_p = section.footer.paragraphs[0]
    footer_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    footer_p.add_run("Page ")
    _add_page_number(footer_p)

    doc.add_heading("Clean DOCX", level=0)
    doc.add_heading("Body text", level=1)
    doc.add_paragraph(
        "Body text uses the Normal style. python-docx wraps text automatically; "
        "never insert manual line breaks with newline characters between paragraphs."
    )

    doc.add_heading("Lists", level=1)
    doc.add_paragraph("First bullet from a real list style.", style="List Bullet")
    doc.add_paragraph("Second bullet, also a real list item.", style="List Bullet")
    doc.add_paragraph("First numbered step.", style="List Number")
    doc.add_paragraph("Second numbered step.", style="List Number")

    doc.add_heading("Table", level=1)
    table = doc.add_table(rows=1, cols=3)
    table.style = "Table Grid"
    hdr = table.rows[0].cells
    hdr[0].text, hdr[1].text, hdr[2].text = "Component", "Description", "Status"
    row = table.add_row().cells
    row[0].text = "Renderer"
    row[1].text = "Column widths are set on every cell so they hold."
    row[2].text = "OK"
    _set_col_widths(table, [Inches(1.6), Inches(4.3), Inches(0.9)])

    doc.add_page_break()
    doc.add_heading("Second page", level=1)
    doc.add_paragraph("Content after an explicit page break.")

    doc.save(output_path)
    return output_path


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "sample.docx"
    print(f"Wrote {build(out)}")
