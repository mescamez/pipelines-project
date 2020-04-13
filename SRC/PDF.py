from fpdf import FPDF
import webbrowser as wb

def createPDF(infoSong):
    pdf = FPDF()
    pdf.add_page()

    #Title
    pdf.set_font('Arial', 'B', 22)
    pdf.cell(180, 10, 'Song Info',0,1,'C')

    #Image
    pdf.ln(h = 10)
    pdf.image('iTunes.png', 10, 8, 33)
    #pdf.set_font('Arial', 'U', 16)
    #pdf.cell(80, 10, 'Lyric')

    #Artist
    pdf.ln(h = 10)
    #pdf.set_font('Arial', 'U', 16)
    #pdf.cell(80, 10, 'Artist')
    pdf.set_font('Arial','', 8)
    text = infoSong
    pdf.cell(80, 10, text)
     
    #Generate PDF
    pdf.output('music.pdf', 'F')
    return wb.open_new('music.pdf')
    
"""
#Song
#pdf.ln(h = 10)
pdf.set_font('Arial', 'U', 16)
pdf.cell(80, 10, 'Song')
pdf.set_font('Arial','I', 16)
#pdf.cell(0, 10, 'Rolling in the deep')

#Album
pdf.ln(h = 10)
pdf.set_font('Arial', 'U', 16)
pdf.cell(80, 10, 'Album')

"""
   
