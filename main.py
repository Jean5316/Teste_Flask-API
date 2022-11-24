from noticias import noticias, new_noticias, get_comments
from flask import Flask, render_template, request

app = Flask('MARATONA NEWS')


@app.route('/')
def home():
    noticias_popular = noticias()
    novas = new_noticias()
    order_by = request.args.get('order_by')
  
    return render_template('index.html',
                           popular=noticias_popular,
                           novas=novas,
                           order_by=order_by)


@app.route('/<id>')
def id(id):
    comments = get_comments(id)
    noticia = noticias()
    novas_noticia = new_noticias()
    all_noticias = noticia + novas_noticia
    id_funcion = id
    if id_funcion == id:
        for i in all_noticias:
            if i['id_noticia'] == id:
                todas = i
    return render_template('id.html', noticia=todas, comentarios=comments)


app.run(host='0.0.0.0')
