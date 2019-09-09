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

# def save_show_pdf():
#     report = canvas.Canvas("ROI_Generos.pdf", pagesize=letter)

#     text = report.beginText(200,650)
#     text.setFont("Times-Roman", 12)
#     text.textLine("¿Que género habrías elegido en 2010?")
#     report.drawText(text)

#     report.drawImage("roi.png", 50, 300,width=500, height=250)

#     report.save()
#     webbrowser.open_new(r'ROI_Generos.pdf')


# def genero_roi_vote(genero):
#     roi = str(mean_roi_genre.ROI[genero])
#     vote = str(round(df_cine_vote_genre_mean.vote_average[genero], 2))
#     return print("El ROI del género", genero,"es:", roi,"%","y el voto medio:",vote)

# def max_10_pelis(genero):
#     max10_genre = pd.DataFrame(df_cine_vote,columns=['TITLE','GENRE','vote_average'])
#     max10_genre = max10_genre[max10_genre['GENRE']==genero]
#     py = max10_genre.nlargest(10, ['vote_average'])

#     return print(py)

# def max_10_roi(genero):
#     max10_roi = pd.DataFrame(df_cine_bv,columns=['TITLE','GENRE','ROI'])
#     max10_roi = max10_roi[max10_roi['GENRE']==genero]
#     py = max10_roi.nlargest(10, ['ROI'])
    
#     return print(py)