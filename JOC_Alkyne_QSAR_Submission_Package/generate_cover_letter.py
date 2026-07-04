import os

# Define the formal cover letter text with integrated institutional details
cover_letter_content = """Southern British High School,
15, Rotimi Amaechi Avenue, Off Tinapa Road,
Calabar, Cross River State,
Nigeria.
July 3, 2026

To the Senior Editors,
The Journal of Organic Chemistry
American Chemical Society

Subject: Submission of Original Research Manuscript for Publication

Dear Editor,

I am pleased to submit our original research manuscript titled "Predictive QSAR Framework for Terminal Alkyne Acidity via Stereoelectronic Geometric Parsing" for consideration for publication as an Article in The Journal of Organic Chemistry. This research was co-authored with Ivara Samuel from the University of Cross River State, Calabar, Nigeria.

In this investigation, we present an interpretable and computationally efficient Quantitative Structure-Activity Relationship (QSAR) framework that models the ground-state polarization of terminal alkynes. Utilizing simple 3D Cartesian coordinates generated from low-overhead conformational minimizations, we successfully isolate structural size metrics from localized inductive electronic parameters. 

Importantly, our computational metrics demonstrate an excellent linear correlation (r = 0.812) with classical empirical Hammett substituent parameters. This direct validation bridges the historical gap between digital database screening and classical physical-organic principles, avoiding the "black-box" limitations common in modern machine-learning workflows. We believe these findings will significantly interest JOC readers working in synthetic methodology, copper-catalyzed click chemistry, and computational physical chemistry.

This manuscript has not been published previously and is not under consideration for publication elsewhere. All authors have reviewed and approved the submission of this work. Complete Cartesian coordinate datasets have been formatted and provided in the accompanying Supporting Information file to ensure total reproducibility.

Thank you very much for your time and consideration of our manuscript.

Sincerely,

Aniema Ekemini
Corresponding Author
Southern British High School, Calabar, Nigeria
Email: ekemjah5@gmail.com
"""

filename = "JOC_Cover_Letter.txt"

# Write the text string directly to a file
with open(filename, "w", encoding="utf-8") as f:
    f.write(cover_letter_content)

print(f"\n[SUCCESS] Cover Letter programmatically compiled.")
print(f"----> Created: '{filename}'")
