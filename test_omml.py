import docx
from docx.oxml import parse_xml

doc = docx.Document()
p = doc.add_paragraph()

omml_str = """<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
  <m:oMath>
    <m:sSub>
      <m:e><m:r><m:t>x</m:t></m:r></m:e>
      <m:sub><m:r><m:t>spv</m:t></m:r></m:sub>
    </m:sSub>
    <m:r><m:t> = [</m:t></m:r>
    <m:sSub><m:e><m:r><m:t>f</m:t></m:r></m:e><m:sub><m:r><m:t>1</m:t></m:r></m:sub></m:sSub>
    <m:r><m:t>, </m:t></m:r>
    <m:sSub><m:e><m:r><m:t>f</m:t></m:r></m:e><m:sub><m:r><m:t>2</m:t></m:r></m:sub></m:sSub>
    <m:r><m:t>, ..., </m:t></m:r>
    <m:sSub><m:e><m:r><m:t>f</m:t></m:r></m:e><m:sub><m:r><m:t>22</m:t></m:r></m:sub></m:sSub>
    <m:sSup><m:e><m:r><m:t>]</m:t></m:r></m:e><m:sup><m:r><m:t>T</m:t></m:r></m:sup></m:sSup>
    <m:r><m:t>,   m &#8712; {0, 1}</m:t></m:r>
    <m:sSup><m:e><m:r><m:t></m:t></m:r></m:e><m:sup><m:r><m:t>22</m:t></m:r></m:sup></m:sSup>
  </m:oMath>
</m:oMathPara>"""

p._p.append(parse_xml(omml_str))
doc.save('test_eq1.docx')
print('test_eq1.docx generated successfully.')
