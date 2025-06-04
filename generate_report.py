import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")  
print("Data loaded successfully!")


summary = data.describe()

plt.figure(figsize=(8, 4))
data.hist(figsize=(10, 8))
plt.tight_layout()
plt.savefig("plot.png")
plt.close()

pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", size=14)
pdf.cell(200, 10, txt="Automated Data Report", ln=True, align="C")

pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Summary Statistics:", ln=True)

for col in summary.columns:
    pdf.cell(200, 10, txt=f"{col} - Mean: {summary[col]['mean']:.2f}", ln=True)

pdf.image("plot.png", x=10, y=80, w=180)  

pdf.output("report.pdf")
print("PDF report generated!")