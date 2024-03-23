from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', size=12)
pdf.image("shirtificate.png", (210 - 180) / 2, 80, w=180)

pdf.cell(text="hello world")
pdf.output("hello_world.pdf")
