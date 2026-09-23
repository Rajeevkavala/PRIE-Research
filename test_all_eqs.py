import os
import docx
from docx.oxml import parse_xml

doc = docx.Document()

eqs = [
    # Eq 1
    ("""<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
      <m:oMath>
        <m:sSub><m:e><m:r><m:t>x</m:t></m:r></m:e><m:sub><m:r><m:t>spv</m:t></m:r></m:sub></m:sSub>
        <m:r><m:t> = [</m:t></m:r>
        <m:sSub><m:e><m:r><m:t>f</m:t></m:r></m:e><m:sub><m:r><m:t>1</m:t></m:r></m:sub></m:sSub><m:r><m:t>, </m:t></m:r>
        <m:sSub><m:e><m:r><m:t>f</m:t></m:r></m:e><m:sub><m:r><m:t>2</m:t></m:r></m:sub></m:sSub><m:r><m:t>, ..., </m:t></m:r>
        <m:sSub><m:e><m:r><m:t>f</m:t></m:r></m:e><m:sub><m:r><m:t>22</m:t></m:r></m:sub></m:sSub>
        <m:sSup><m:e><m:r><m:t>]</m:t></m:r></m:e><m:sup><m:r><m:t>T</m:t></m:r></m:sup></m:sSup>
        <m:r><m:t>,    m &#8712; {0, 1}</m:t></m:r>
        <m:sSup><m:e><m:r><m:t></m:t></m:r></m:e><m:sup><m:r><m:t>22</m:t></m:r></m:sup></m:sSup>
      </m:oMath>
    </m:oMathPara>""", 1),

    # Eq 2
    ("""<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
      <m:oMath>
        <m:r><m:t>&#8466;(&#952;) = -</m:t></m:r>
        <m:nary>
          <m:naryPr><m:chr m:val="&#8721;"/><m:limLoc m:val="undOvr"/></m:naryPr>
          <m:sub><m:r><m:t>i=1</m:t></m:r></m:sub>
          <m:sup><m:r><m:t>N</m:t></m:r></m:sup>
          <m:e>
            <m:r><m:t>[</m:t></m:r>
            <m:sSub><m:e><m:r><m:t>w</m:t></m:r></m:e><m:sub><m:r><m:t>pos</m:t></m:r></m:sub></m:sSub>
            <m:sSub><m:e><m:r><m:t>y</m:t></m:r></m:e><m:sub><m:r><m:t>i</m:t></m:r></m:sub></m:sSub>
            <m:r><m:t> ln </m:t></m:r>
            <m:sSub><m:e><m:acc><m:accPr><m:chr m:val="&#770;"/></m:accPr><m:e><m:r><m:t>p</m:t></m:r></m:e></m:acc></m:e><m:sub><m:r><m:t>i</m:t></m:r></m:sub></m:sSub>
            <m:r><m:t> + (1 - </m:t></m:r>
            <m:sSub><m:e><m:r><m:t>y</m:t></m:r></m:e><m:sub><m:r><m:t>i</m:t></m:r></m:sub></m:sSub>
            <m:r><m:t>) ln (1 - </m:t></m:r>
            <m:sSub><m:e><m:acc><m:accPr><m:chr m:val="&#770;"/></m:accPr><m:e><m:r><m:t>p</m:t></m:r></m:e></m:acc></m:e><m:sub><m:r><m:t>i</m:t></m:r></m:sub></m:sSub>
            <m:r><m:t>)]</m:t></m:r>
          </m:e>
        </m:nary>
        <m:r><m:t> + &#937;(&#952;)</m:t></m:r>
      </m:oMath>
    </m:oMathPara>""", 2),

    # Eq 3
    ("""<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
      <m:oMath>
        <m:acc><m:accPr><m:chr m:val="&#770;"/></m:accPr><m:e><m:r><m:t>P</m:t></m:r></m:e></m:acc>
        <m:r><m:t>(Y = 1 | z) = &#963;(Az + B) = </m:t></m:r>
        <m:f>
          <m:num><m:r><m:t>1</m:t></m:r></m:num>
          <m:den><m:r><m:t>1 + exp(-(Az + B))</m:t></m:r></m:den>
        </m:f>
      </m:oMath>
    </m:oMathPara>""", 3),

    # Eq 4
    ("""<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
      <m:oMath>
        <m:r><m:t>f(x) = </m:t></m:r>
        <m:sSub><m:e><m:r><m:t>&#981;</m:t></m:r></m:e><m:sub><m:r><m:t>0</m:t></m:r></m:sub></m:sSub>
        <m:r><m:t> + </m:t></m:r>
        <m:nary>
          <m:naryPr><m:chr m:val="&#8721;"/><m:limLoc m:val="undOvr"/></m:naryPr>
          <m:sub><m:r><m:t>j=1</m:t></m:r></m:sub>
          <m:sup><m:r><m:t>22</m:t></m:r></m:sup>
          <m:e>
            <m:sSub><m:e><m:r><m:t>&#981;</m:t></m:r></m:e><m:sub><m:r><m:t>j</m:t></m:r></m:sub></m:sSub>
            <m:r><m:t>(x)</m:t></m:r>
          </m:e>
        </m:nary>
      </m:oMath>
    </m:oMathPara>""", 4),

    # Eq 5
    ("""<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
      <m:oMath>
        <m:sSup><m:e><m:r><m:t>c</m:t></m:r></m:e><m:sup><m:r><m:t>*</m:t></m:r></m:sup></m:sSup>
        <m:r><m:t> = arg min</m:t></m:r>
        <m:sSub><m:e><m:r><m:t></m:t></m:r></m:e><m:sub><m:r><m:t>c</m:t></m:r></m:sub></m:sSub>
        <m:r><m:t> loss(f(c), </m:t></m:r>
        <m:sSup><m:e><m:r><m:t>y</m:t></m:r></m:e><m:sup><m:r><m:t>*</m:t></m:r></m:sup></m:sSup>
        <m:r><m:t>) + </m:t></m:r>
        <m:f>
          <m:num><m:sSub><m:e><m:r><m:t>&#955;</m:t></m:r></m:e><m:sub><m:r><m:t>1</m:t></m:r></m:sub></m:sSub></m:num>
          <m:den><m:r><m:t>k</m:t></m:r></m:den>
        </m:f>
        <m:nary>
          <m:naryPr><m:chr m:val="&#8721;"/><m:limLoc m:val="undOvr"/></m:naryPr>
          <m:sub><m:r><m:t>j &#8712; &#8499;</m:t></m:r></m:sub>
          <m:sup><m:r><m:t></m:t></m:r></m:sup>
          <m:e>
            <m:f>
              <m:num><m:r><m:t>|c</m:t></m:r><m:sSub><m:e><m:r><m:t></m:t></m:r></m:e><m:sub><m:r><m:t>j</m:t></m:r></m:sub></m:sSub><m:r><m:t> - x</m:t></m:r><m:sSub><m:e><m:r><m:t></m:t></m:r></m:e><m:sub><m:r><m:t>j</m:t></m:r></m:sub></m:sSub><m:r><m:t>|</m:t></m:r></m:num>
              <m:den><m:sSub><m:e><m:r><m:t>MAD</m:t></m:r></m:e><m:sub><m:r><m:t>j</m:t></m:r></m:sub></m:sSub></m:den>
            </m:f>
          </m:e>
        </m:nary>
        <m:r><m:t> + </m:t></m:r>
        <m:sSub><m:e><m:r><m:t>&#955;</m:t></m:r></m:e><m:sub><m:r><m:t>2</m:t></m:r></m:sub></m:sSub>
        <m:r><m:t> dpp(c)</m:t></m:r>
      </m:oMath>
    </m:oMathPara>""", 5),

    # Eq 6
    ("""<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
      <m:oMath>
        <m:sSub><m:e><m:r><m:t>c</m:t></m:r></m:e><m:sub><m:r><m:t>j</m:t></m:r></m:sub></m:sSub>
        <m:r><m:t> = </m:t></m:r>
        <m:sSub><m:e><m:r><m:t>x</m:t></m:r></m:e><m:sub><m:r><m:t>j</m:t></m:r></m:sub></m:sSub>
        <m:r><m:t>  &#8704; j &#8712; &#8464;,    ||&#916;x||</m:t></m:r>
        <m:sSub><m:e><m:r><m:t></m:t></m:r></m:e><m:sub><m:r><m:t>0</m:t></m:r></m:sub></m:sSub>
        <m:r><m:t> &#8804; 3.0,    </m:t></m:r>
        <m:sSub><m:e><m:r><m:t>c</m:t></m:r></m:e><m:sub><m:r><m:t>j</m:t></m:r></m:sub></m:sSub>
        <m:r><m:t> &#8712; [0.0, 1.0]  &#8704; j &#8712; &#8499;</m:t></m:r>
      </m:oMath>
    </m:oMathPara>""", 6),

    # Eq 7
    ("""<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
      <m:oMath>
        <m:sSub><m:e><m:r><m:t>S</m:t></m:r></m:e><m:sub><m:r><m:t>fused</m:t></m:r></m:sub></m:sSub>
        <m:r><m:t> = 0.35 &#183; </m:t></m:r>
        <m:sSub><m:e><m:r><m:t>S</m:t></m:r></m:e><m:sub><m:r><m:t>aud</m:t></m:r></m:sub></m:sSub>
        <m:r><m:t> + 0.35 &#183; </m:t></m:r>
        <m:sSub><m:e><m:r><m:t>S</m:t></m:r></m:e><m:sub><m:r><m:t>vid</m:t></m:r></m:sub></m:sSub>
        <m:r><m:t> + 0.30 &#183; </m:t></m:r>
        <m:sSub><m:e><m:r><m:t>S</m:t></m:r></m:e><m:sub><m:r><m:t>spk</m:t></m:r></m:sub></m:sSub>
      </m:oMath>
    </m:oMathPara>""", 7),

    # Eq 8
    ("""<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
      <m:oMath>
        <m:r><m:t>ECE = </m:t></m:r>
        <m:nary>
          <m:naryPr><m:chr m:val="&#8721;"/><m:limLoc m:val="undOvr"/></m:naryPr>
          <m:sub><m:r><m:t>m=1</m:t></m:r></m:sub>
          <m:sup><m:r><m:t>M</m:t></m:r></m:sup>
          <m:e>
            <m:f>
              <m:num><m:r><m:t>|B</m:t></m:r><m:sSub><m:e><m:r><m:t></m:t></m:r></m:e><m:sub><m:r><m:t>m</m:t></m:r></m:sub></m:sSub><m:r><m:t>|</m:t></m:r></m:num>
              <m:den><m:r><m:t>N</m:t></m:r></m:den>
            </m:f>
            <m:r><m:t> |acc(B</m:t></m:r><m:sSub><m:e><m:r><m:t></m:t></m:r></m:e><m:sub><m:r><m:t>m</m:t></m:r></m:sub></m:sSub><m:r><m:t>) - conf(B</m:t></m:r><m:sSub><m:e><m:r><m:t></m:t></m:r></m:e><m:sub><m:r><m:t>m</m:t></m:r></m:sub></m:sSub><m:r><m:t>)|</m:t></m:r>
          </m:e>
        </m:nary>
      </m:oMath>
    </m:oMathPara>""", 8),
]

for xml_str, num in eqs:
    p = doc.add_paragraph()
    p._p.append(parse_xml(xml_str))

doc.save('test_all_eqs.docx')
print('Successfully saved test_all_eqs.docx with 8 equations!')
