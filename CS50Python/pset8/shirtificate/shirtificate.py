from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', size=12)
pdf.image("shirtificate.png", 0, 50, 50)
pdf.cell(text="hello world")
pdf.output("hello_world.pdf")
