# Part 2: Read the unified text cache and compile the final customized JOC PDF
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def compile_final_manuscript():
    if not os.path.exists("final_manuscript_text.tmp"):
        print("[ERROR] Missing final manuscript text cache file from Part 1.")
        return

    with open("final_manuscript_text.tmp", "r", encoding="utf-8") as f:
        raw_text = f.read()

    # Parse headings out of the temporary text database
    sections = {}
    current_key = None
    current_lines = []
    
    for line in raw_text.split('\n'):
        if line.startswith('[') and line.endswith(']'):
            if current_key:
                sections[current_key] = '\n'.join(current_lines).strip()
            current_key = line[1:-1]
            current_lines = []
        else:
            current_lines.append(line)
    if current_key:
        sections[current_key] = '\n'.join(current_lines).strip()

    # Setup document template with ACS/JOC standard editorial margins (1 inch)
    doc = SimpleDocTemplate("JOC_Final_Manuscript.pdf", pagesize=letter,
                            rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle('FinalTitle', fontName='Helvetica-Bold', fontSize=15, leading=19, alignment=1, spaceAfter=10)
    author_style = ParagraphStyle('FinalAuth', fontName='Helvetica-Bold', fontSize=10.5, leading=14, alignment=1, spaceAfter=4)
    affil_style = ParagraphStyle('FinalAff', fontName='Helvetica-Oblique', fontSize=8.5, leading=12, alignment=1, spaceAfter=12, textColor=colors.HexColor('#2D3748'))
    abs_head = ParagraphStyle('FinalAbsH', fontName='Helvetica-Bold', fontSize=11, leading=14, alignment=1, spaceAfter=6)
    abs_body = ParagraphStyle('FinalAbsB', fontName='Helvetica-Oblique', fontSize=9.5, leading=14, leftIndent=24, rightIndent=24, alignment=4, spaceAfter=15)
    sec_head = ParagraphStyle('FinalSecH', fontName='Helvetica-Bold', fontSize=12, leading=16, spaceBefore=14, spaceAfter=6, keepWithNext=True)
    body_style = ParagraphStyle('FinalBody', fontName='Helvetica', fontSize=10, leading=16, spaceAfter=10, alignment=4)
    eq_style = ParagraphStyle('FinalEq', fontName='Helvetica-Oblique', fontSize=10.5, leading=14, alignment=1, spaceBefore=6, spaceAfter=10)

    story = []
    
    # Title & Contributors Header Assembly
    story.append(Paragraph(sections.get('TITLE', ''), title_style))
    story.append(Paragraph(sections.get('AUTHORS', ''), author_style))
    story.append(Paragraph(sections.get('AFFILIATIONS', '').replace('\n', '<br/>'), affil_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.gray, spaceAfter=12))
    
    # Abstract
    story.append(Paragraph("Abstract", abs_head))
    story.append(Paragraph(sections.get('ABSTRACT', ''), abs_body))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.gray, spaceAfter=12))
    
    # Core Narrative Sections
    story.append(Paragraph("Introduction", sec_head))
    story.append(Paragraph(sections.get('INTRODUCTION', ''), body_style))
    
    story.append(Paragraph("Computational Methods", sec_head))
    story.append(Paragraph(sections.get('METHODS', ''), body_style))
    story.append(Paragraph(sections.get('SUBMETHODS', ''), body_style))
    
    story.append(Paragraph("Results and Discussion", sec_head))
    story.append(Paragraph(sections.get('RESULTS', ''), body_style))
    story.append(Paragraph(sections.get('EQUATION', ''), eq_style))
    story.append(Paragraph(sections.get('RESULTS_CONTINUED', ''), body_style))
    
    story.append(Paragraph("Conclusion", sec_head))
    story.append(Paragraph(sections.get('CONCLUSION', ''), body_style))
    
    doc.build(story)
    
    # Clean up background cache layout
    try: os.remove("final_manuscript_text.tmp")
    except: pass
    
    print("\n[SUCCESS] Final Custom Manuscript PDF safely generated.")
    print("----> Open file: 'JOC_Final_Manuscript.pdf'")

if __name__ == "__main__":
    compile_final_manuscript()
