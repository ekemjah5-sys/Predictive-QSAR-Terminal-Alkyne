# Part 2: Read the text asset cache and compile the professional JOC PDF
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def compile_manuscript_to_pdf():
    if not os.path.exists("manuscript_text.tmp"):
        print("[ERROR] Missing manuscript text cache file from Part 1.")
        return

    with open("manuscript_text.tmp", "r", encoding="utf-8") as f:
        raw_text = f.read()

    # Parse sections out of the cached text database
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

    # Setup reportlab document with editorial standard margins
    doc = SimpleDocTemplate("JOC_Manuscript_Submission.pdf", pagesize=letter,
                            rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle('JOC_Title', parent=styles['Heading1'], fontSize=15, leading=19, fontName='Helvetica-Bold', alignment=1, spaceAfter=15)
    abs_head = ParagraphStyle('JOC_AbsHead', parent=styles['Heading2'], fontSize=11, leading=14, fontName='Helvetica-Bold', alignment=1, spaceAfter=6)
    abs_body = ParagraphStyle('JOC_AbsBody', parent=styles['Normal'], fontSize=9.5, leading=14, fontName='Helvetica-Oblique', leftIndent=24, rightIndent=24, alignment=4, spaceAfter=20)
    sec_head = ParagraphStyle('JOC_SecHead', parent=styles['Heading2'], fontSize=12, leading=16, fontName='Helvetica-Bold', spaceBefore=14, spaceAfter=8, keepWithNext=True)
    body_style = ParagraphStyle('JOC_Body', parent=styles['Normal'], fontSize=10, leading=16, fontName='Helvetica', spaceAfter=12, alignment=4)
    eq_style = ParagraphStyle('JOC_Eq', parent=styles['Normal'], fontSize=11, leading=15, fontName='Helvetica-Oblique', alignment=1, spaceBefore=8, spaceAfter=12)

    story = []
    
    # Assembly logic from section components
    story.append(Paragraph(sections.get('TITLE', ''), title_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.gray, spaceAfter=14))
    
    story.append(Paragraph("Abstract", abs_head))
    story.append(Paragraph(sections.get('ABSTRACT', ''), abs_body))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.gray, spaceAfter=14))
    
    story.append(Paragraph("Introduction", sec_head))
    story.append(Paragraph(sections.get('INTRODUCTION', ''), body_style))
    
    story.append(Paragraph("Computational Methods", sec_head))
    story.append(Paragraph(sections.get('METHODS', ''), body_style))
    
    story.append(Paragraph("Results and Discussion", sec_head))
    story.append(Paragraph(sections.get('RESULTS', ''), body_style))
    story.append(Paragraph(sections.get('EQUATION', ''), eq_style))
    story.append(Paragraph(sections.get('RESULTS_CONTINUED', ''), body_style))
    
    story.append(Paragraph("Conclusion", sec_head))
    story.append(Paragraph(sections.get('CONCLUSION', ''), body_style))
    
    doc.build(story)
    
    # Cleanup temporary layout asset
    try: os.remove("manuscript_text.tmp")
    except: pass
    
    print("\n[SUCCESS] Final JOC Manuscript PDF successfully built as:")
    print("----> 'JOC_Manuscript_Submission.pdf'")

if __name__ == "__main__":
    compile_manuscript_to_pdf()
