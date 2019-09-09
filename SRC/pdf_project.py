from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def grafica_pdf():
        
    report = canvas.Canvas("Tsunami_causas.pdf", pagesize=letter)
    text = report.beginText(200,650)
    text.setFont("Times-Roman", 12)
    text.textLine("Causas de los Tsunamis")
    report.drawText(text)
    report.drawImage("Tsunami.png", 50, 300,width=500, height=250)
    report.save()

    webbrowser.open_new(r'Tsunami_causas.pdf')
    return print(py)

