from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Set font: Helvetica, bold, size 48
        self.set_font("Helvetica", "B", 48)
        # Title
        self.cell(0, 60, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

    def add_shirt(self, name):
        # Add the shirt image, centered
        # A4 width is 210mm. Image width is 190mm. x position = (210-190)/2 = 10
        self.image("shirtificate.png", x=10, y=70, w=190)
        # Set font for the name: Helvetica, bold, size 24
        self.set_font("Helvetica", "B", 24)
        # Set text color to white
        self.set_text_color(255, 255, 255)
        # Add the text with the user's name on the shirt
        # Adjust vertical position to be on the shirt's chest
        self.cell(0, 210, f"{name} took CS50", align="C")


def main():
    # Get the user's name
    name = input("Name: ")

    # Create a PDF object
    pdf = PDF()
    pdf.add_page(orientation="P", format="A4")
    pdf.add_shirt(name)

    # Save the PDF
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
