import requests


def upload_id(url):
    '''
    Récupération de la liste d'ID
    '''
    id_list = []
    r = requests.get(url)
    id_list = r.json()
    return id_list


def check_id(list):
    '''
    Vérification des status url et création de la liste d'adresse
    '''
    global url_list
    url_list = []
    index = 0
    for id in list:
        url = (f'https://hacker-news.firebaseio.com/v0/item/{id}')
        r = requests.get(url)
        print('id:',  id, 'status:', r.status_code)
        if r.status_code == 200:
            url_list.append(url)
        index += 1      # limitation de la boucle à 5 pour test
        if index > 4:   #
            break       #
    print('-'*7)


def url_description(url):
    '''
    Affichage des informations de chaque adresse de la liste
    '''
    for url_id in url:
        dict = {}
        r = requests.get(url_id + '.json')
        dict = r.json()
        print('Title:', dict['title'])
        print('Discussion link:', url_id)
        print('Comments:', dict['descendants'])
        print('-'*7)


def id(url_id):
    list_id = upload_id(url_id)
    check_id(list_id)
    url_description(url_list)
