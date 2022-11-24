import requests
import json


def noticias(url='https://hn.algolia.com/api/v1/search?tags=story'):
    noticias = []
    r = requests.get(url).text
    r1 = json.loads(r)
    r2 = r1['hits']
    for i in r2:
        titulo = i['title']
        url = i['url']
        id_noticia = i['objectID']
        autor = i['author']
        votos = i['points']
        comentarios = i['num_comments']

        list_title_url = {
            'titulo': titulo,
            'url': url,
            'id_noticia': id_noticia,
            'autor': autor,
            'votos': votos,
            'comentarios': comentarios,
        }
        noticias.append(list_title_url)
    return noticias


def new_noticias(
        url='https://hn.algolia.com/api/v1/search_by_date?tags=story'):
    noticias = []
    r = requests.get(url).text
    r1 = json.loads(r)
    r2 = r1['hits']
    for i in r2:
        titulo = i['title']
        url = i['url']
        id_noticia = i['objectID']
        autor = i['author']
        votos = i['points']
        comentarios = i['num_comments']
        list_title_url = {
            'titulo': titulo,
            'url': url,
            'id_noticia': id_noticia,
            'autor': autor,
            'votos': votos,
            'comentarios': comentarios,
        }
        noticias.append(list_title_url)
    return noticias


def get_comments(id):
    url_base = f'https://hn.algolia.com/api/v1/items/{id}'
    comments = []
    r = requests.get(url_base).text
    r1 = json.loads(r, encoding='utf-8')
    comment = r1['children']
    for i in comment:
        autor = i['author']
        text = i['text']
        if autor or text != None:
            all_comments = {'autor': autor, 'texto': text}
            comments.append(all_comments)

    return comments
