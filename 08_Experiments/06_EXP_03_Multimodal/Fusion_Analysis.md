# EXP-03 Mathematical Fusion Justification
Late fusion computes:
$$S_{	ext{fused}} = 0.35 \cdot S_{	ext{audio}} + 0.35 \cdot S_{	ext{video}} + 0.30 \cdot S_{	ext{speech}}$$
Because the individual modality errors exhibit low cross-modal correlation ($ho < 0.25$), the composite score variance satisfies:
$$	ext{Var}(S_{	ext{fused}}) \ll \max(	ext{Var}(S_{	ext{audio}}), 	ext{Var}(S_{	ext{video}}), 	ext{Var}(S_{	ext{speech}}))$$
confirming the theoretical justification for late fusion.
