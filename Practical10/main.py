from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial",size=20)
f = open(r"3rdSemResult.txt","r")

for x in f:
    pdf.cell(200,10,txt=x,ln=5,align='L')

pdf.output("3rdSemMarksheet.pdf")