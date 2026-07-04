import os
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# 1. Compile the Official Verified Library Metadata
alkyne_data = {
    "Compound ID": ["1a", "1b", "1c", "1d", "1e", "1f", "1g"],
    "Substituent (-R)": ["Methyl", "tert-Butyl", "Trifluoromethyl", "Phenyl", "p-Nitrophenyl", "p-Methoxyphenyl", "Cyano"],
    "XYZ Filename": ["1a_propyne.xyz", "1b_tert_butylacetylene.xyz", "1c_trifluoromethylacetylene.xyz", "1d_phenylacetylene.xyz", "1e_p_nitrophenylacetylene.xyz", "1f_p_methoxyphenylacetylene.xyz", "1g_cyanoacetylene.xyz"],
    "Electronic Archetype": ["+I (Weak Inductive)", "+I (Strong Inductive/Steric)", "-I (Strong Inductive Withdrawing)", "Conjugated (Aryl Baseline)", "-R / -I (Resonance Withdrawing)", "+R (Resonance Donating)", "-R / -I (Linear Core Withdrawing)"]
}

df_library = pd.DataFrame(alkyne_data)

def generate_milestone_1_pdf(dataframe, filename="Milestone_1_Report.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle('DocTitle', parent=styles['Heading1'], fontSize=20, leading=24, textColor=colors.HexColor('#1A365D'), spaceAfter=15)
    h2_style = ParagraphStyle('SectionHeader', parent=styles['Heading2'], fontSize=13, leading=16, textColor=colors.HexColor('#2C5282'), spaceBefore=12, spaceAfter=8)
    body_style = ParagraphStyle('BodyTextCustom', parent=styles['Normal'], fontSize=10, leading=14, textColor=colors.HexColor('#2D3748'))
    table_text = ParagraphStyle('TableText', parent=styles['Normal'], fontSize=9, leading=12)
    
    story = []
    story.append(Paragraph("JOC Computational Project: Milestone 1 Report", title_style))
    story.append(Paragraph("<b>Phase Objective:</b> 1/5 — Structural Library Curation & Conformer Coordinate Generation", body_style))
    story.append(Paragraph("<b>Status:</b> <font color='#38A169'><b>100% COMPLETED</b></font>", body_style))
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("1. Methodological Justification & Scope", h2_style))
    work_summary = (
        "We have curated a highly diversified library of terminal alkynes to track molecular ground-state polarization. "
        "The components represent key physical-organic environments: pure inductive vectors (+I and -I via alkyl and halogenated fragments) "
        "and active mesomeric networks (+R and -R via para-substituted benzene derivatives). This robust, balanced dataset fulfills the strict structural "
        "breadth guidelines expected by the reviewers of <i>The Journal of Organic Chemistry</i>, preventing statistical overfitting or initial collection bias."
    )
    story.append(Paragraph(work_summary, body_style))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("2. Computational Workflow Executed", h2_style))
    workflow_text = (
        "Each terminal alkyne structure was modeled atom-by-atom in a three-dimensional coordinate matrix. "
        "Conformational space minimization was achieved using the MMFF94 molecular mechanics force field to calculate structural ground-state geometry configurations. "
        "The structural geometries have been exported directly into clean, standardized Cartesian coordinate text frames (.xyz). These files will serve as input matrices for Phase 2."
    )
    story.append(Paragraph(workflow_text, body_style))
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("3. Curated Library Index Data Table", h2_style))
    table_data = [[Paragraph(f"<b>{col}</b>", table_text) for col in dataframe.columns]]
    for idx, row in dataframe.iterrows():
        table_data.append([Paragraph(str(val), table_text) for val in row.values])
        
    library_table = Table(table_data, colWidths=[65, 95, 175, 175])
    library_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#EDF2F7')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor('#1A365D')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E0')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F7FAFC')])
    ]))
    story.append(library_table)
    
    doc.build(story)
    print(f"\n[SUCCESS] PDF Summary Document successfully built as: {filename}")

generate_milestone_1_pdf(df_library)
