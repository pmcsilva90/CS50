from fpdf import FPDF

def main():

    name = input("Name: ")

    pdf = FPDF()
    pdf.add_page()
    pdf.image("shirtificate.png", (pdf.w - 180) / 2, 80, w=180)


    pdf.set_font('helvetica', size=40, style='B')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(pdf.epw, 0, text="CS50 Shirtificate", align='C')


    pdf.set_font('helvetica', size=26, style='B')
    pdf.set_text_color(255, 255, 255)
    pdf.cell(pdf.epw, 260, text=f"{name} took CS50", align='C')

    pdf.output("hello_world.pdf")

if __name__ == "__main__":
    main()
