from fpdf import FPDF
import webbrowser as wb

def createPDF(infoSong, song, artist):
    pdf = FPDF()
    pdf.add_page()

    #Title
    pdf.set_font('Arial', 'B', 22)
    title_text = song
    title_text1 = artist
    pdf.cell(180, 10, title_text,0,1,'C')
    pdf.cell(180, 10, title_text1, 0,1, 'C')

    #Image
    pdf.ln(h = 10)
    pdf.image('../pipelines-project/Input/iTunes.png', 10, 8, 33)

    #Body
    pdf.ln(h = 10)
    pdf.set_font('Arial','', 12)
    text = infoSong
    pdf.multi_cell(190.0, 10.0, text, 'J', False)
     
    #Generate PDF
    pdf.output('../pipelines-project/Output/music.pdf', 'F')
    return wb.open_new('../pipelines-project/Output/music.pdf')

   