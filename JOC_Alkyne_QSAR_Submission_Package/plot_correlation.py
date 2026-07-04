import os
import matplotlib.pyplot as plt
import numpy as np

# 1. Dataset Construction (Matching our verified physical parameters)
compounds = ["1a", "1b", "1c", "1d", "1e", "1f", "1g"]
substituents = ["Methyl", "tert-Butyl", "Trifluoromethyl", "Phenyl", "p-Nitrophenyl", "p-Methoxyphenyl", "Cyano"]
avg_en = [2.35, 2.31, 3.113, 2.34, 2.466, 2.383, 2.578]
hammett_sig_p = [-0.17, -0.20, 0.54, -0.01, 0.78, -0.27, 0.66]

# 2. Setup high-resolution figure dimensions (JOC single-column format)
plt.figure(figsize=(5.5, 4.5), dpi=300)
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial']

# 3. Calculate the linear regression line of best fit (Y = mX + c)
m, c = np.polyfit(avg_en, hammett_sig_p, 1)
x_line = np.linspace(min(avg_en)-0.1, max(avg_en)+0.1, 100)
y_line = m * x_line + c

# Calculate exact matrix item for r
r_matrix = np.corrcoef(avg_en, hammett_sig_p)
r_value = r_matrix[0, 1]

# 4. Plotting Components
plt.plot(x_line, y_line, color='#A0AEC0', linestyle='--', linewidth=1.5, label=f'Linear Fit (r = {r_value:.3f})')
plt.scatter(avg_en, hammett_sig_p, color='#1A365D', edgecolor='#2B6CB0', s=60, zorder=5)

# Label every point with a custom non-overlapping offset matrix
for i, txt in enumerate(compounds):
    # Dynamically shift text vectors for overlapping clusters
    if txt == "1b":
        xy_text = (5, -12)  # Push tert-butyl down
    elif txt == "1f":
        xy_text = (5, -12)  # Push p-methoxyphenyl down
    elif txt == "1a":
        xy_text = (5, 6)    # Keep methyl up
    else:
        xy_text = (5, 5)    # Standard fallback positioning
        
    plt.annotate(f"{txt} ({substituents[i]})", (avg_en[i], hammett_sig_p[i]), 
                 textcoords="offset points", xytext=xy_text, fontsize=8, color='#2D3748')

# 5. Label formatting using strict lowercase attributes
plt.xlabel('Calculated Average Electronegativity (Avg EN)', fontsize=10, fontweight='bold', labelpad=8)
plt.ylabel(r'Experimental Hammett Constant ($\sigma_p$)', fontsize=10, fontweight='bold', labelpad=8)
plt.title('Physical Validation Matrix: Electronegativity vs. Hammett Parameters', fontsize=10, fontweight='bold', pad=12)

plt.xlim(min(avg_en)-0.15, max(avg_en)+0.15)
plt.ylim(min(hammett_sig_p)-0.15, max(hammett_sig_p)+0.15)
plt.grid(True, linestyle=':', alpha=0.5, color='#CBD5E0')
plt.legend(loc='lower right', frameon=True, facecolor='white', edgecolor='#CBD5E0', fontsize=9)
plt.tight_layout()

output_img = "Figure1_Linear_Correlation.png"
plt.savefig(output_img, dpi=300)
plt.close()

print(f"\n[SUCCESS] Corrected, non-overlapping graph exported as: '{output_img}'")
