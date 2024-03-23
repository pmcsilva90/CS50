from fpdf import FPDF

def main():

    name = input("Name: ")

    pdf = FPDF()
    pdf.add_page()
    pdf.image("shirtificate.png", (pdf.w - 180) / 2, 80, w=180)


    pdf.set_font('helvetica', size=40, style='B')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(pdf.epw, 20, text="CS50 Shirtificate", align='C', ln=True)


    pdf.set_font('helvetica', size=26, style='B')
    pdf.set_text_color(123, 123, 123)
    pdf.cell(pdf.epw, 100, text=f"{name} took CS50", align='C', ln=True)

    pdf.output("hello_world.pdf")

if __name__ == "__main__":
    main()
