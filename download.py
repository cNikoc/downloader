from flask import Flask, render_template, request
import pytube

app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template('index.html')

@app.route('/search', methods=['post'])
def form():
    enlace = request.form['input']
    yt = pytube.YouTube(enlace)

    """ print("Titulo:", yt.title)
    print("Autor:", yt.author)
    print("Fecha de Publicacion:", yt.publish_date.strftime("%Y-%m-%d"))
    print("Numero de Vistas:", yt.views)
    print("Duracion del Video:", yt.length, "seconds") """
    

    """ DESCARGAR VIDEO Y AUDIO """
    yt.streams.get_highest_resolution().download()
    if enlace: return render_template('download.html', link=enlace, views=yt.views, title=yt.title, author=yt.author, date=yt.publish_date.strftime("%d-%m-%Y"))

if __name__ == '__main__':
    app.run(debug=True)

""" SOLO AUDIO """
""" yt.streams.get_audio_only().download()
print(link)
print("Audio del video descargado satisfactoriamente!") """