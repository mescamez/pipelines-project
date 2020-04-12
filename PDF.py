from fpdf import FPDF 

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 24)
pdf.cell(180, 10, 'Song Info', 2,0, "C")
pdf.set_font('Arial', 'B', 16)
pdf.cell(200, 10, "Lyrics")


pdf.output("song_info_pdf.pdf", "F")

