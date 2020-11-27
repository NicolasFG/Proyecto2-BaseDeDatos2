import nltk
import json
from nltk.stem import SnowballStemmer
import re
import math

stoplist = nltk.word_tokenize(open("stoplist.txt", "r").read())
stoplist += ['?', ',', '.', '!', '¿', '¡', ';', '(', ')', ':', '»', '«', '@', '#']
contador_tweets = 0

diccionario_tweets = {}
indice = {}


def filtrar_emojis(text):
    emoji_pattern = re.compile("["
                               u"\U00010000-\U0010ffff"
                               u"\U0001F300-\U0001F5FF"
                               u"\U0001F680-\U0001F6FF"
                               u"\U0001F1E0-\U0001F1FF"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)


def filtrar_text(text):
    text = filtrar_emojis(text)
    tokens = nltk.word_tokenize(text)
    clean_tokens = tokens.copy()
    for token in tokens:
        lowertoken = token.lower()
        if lowertoken in stoplist:
            clean_tokens.remove(token)

    return clean_tokens


def reduccion_tokens(clean_tokens):
    stemmer = SnowballStemmer('spanish')
    reduced_clean_tokens = []
    for token in clean_tokens:
        reduced_clean_tokens.append(stemmer.stem(token))

    return reduced_clean_tokens


def contar_repeticiones(tokens):
    result_tokens = []
    auxiliar = []
    for token in tokens:
        if token not in auxiliar:
            auxiliar.append(token)
            result_tokens.append([token, tokens.count(token)])
    return result_tokens


def extraer_tweets(file):
    global contador_tweets
    f = open(file, "r", encoding="utf-8", errors='ignore')
    tws = json.load(f)
    for tweet in tws:
        contador_tweets += 1
        if tweet['retweeted'] == False:
            tokens1 = filtrar_text(tweet['text'])
            tokens2 = reduccion_tokens(tokens1)
            tokens3 = contar_repeticiones(tokens2)
            for token in tokens3:
                if token[0] in indice:
                    indice[token[0]].append((tweet['id'], token[1]))
                else:
                    indice[token[0]] = []
                    indice[token[0]].append((tweet['id'], token[1]))
            diccionario_tweets[int(tweet['id'])] = tokens3
    f.close()


def calculartf_idf():
    for tweet in diccionario_tweets:
        for token in diccionario_tweets[tweet]:
            df = len(indice[token[0]])
            idf = math.log10(contador_tweets / df)
            token[1] = (1 + math.log10(token[1])) * idf
        tweet = normalizar_vector(diccionario_tweets[tweet])


def seleccion_tweets(collection, query, funcion):
    result = []
    sim = 0
    for tweet in collection:
        sim = funcion(query, collection[tweet])
        result.append((tweet, sim))
    result.sort(key=lambda tup: -tup[1])
    return result[:10]


def normalizar_vector(vector):
    modulo = 0
    for token in vector:
        modulo += (token[1] * token[1])

    modulo = math.sqrt(modulo)

    for token in vector:
        token[1] = token[1] / modulo
    return vector


def queryavector(query):
    terminos = reduccion_tokens(filtrar_text(query))
    vector = []
    auxiliar = []
    for palabra in terminos:
        if palabra not in auxiliar:
            vector.append([palabra, (1 + math.log10(terminos.count(palabra)))])
            auxiliar.append(palabra)
    return vector


def scoring(query, tweet):
    cont = 0
    for token in query:
        for tupla in tweet:
            if token[0] == tupla[0]:
                cont = cont + ((token[1] * tupla[1]))
    return cont


def obtener_texto(tweets):
    tweetscompletos = {}
    for tweet in tweets:
        if int(tweet[0]) <= 1027056503239393281:
            f = open('clean/tweets_2018-08-07.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1027419118302101505:
            f = open('clean/tweets_2018-08-08.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1027781321601548288:
            f = open('clean/tweets_2018-08-09.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1028143875700023296:
            f = open('clean/tweets_2018-08-10.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1028506254623338496:
            f = open('clean/tweets_2018-08-11.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1028868537895579649:
            f = open('clean/tweets_2018-08-12.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1029230802402463744:
            f = open('clean/tweets_2018-08-13.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1029593448297517057:
            f = open('clean/tweets_2018-08-14.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1029955887601999872:
            f = open('clean/tweets_2018-08-15.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1030318225240870912:
            f = open('clean/tweets_2018-08-16.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1030680579791114241:
            f = open('clean/tweets_2018-08-17.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1031043016482586624:
            f = open('clean/tweets_2018-08-18.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1031405425348861952:
            f = open('clean/tweets_2018-08-19.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1031767732923117568:
            f = open('clean/tweets_2018-08-20.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1032130162920497154:
            f = open('clean/tweets_2018-08-21.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1032492588249620481:
            f = open('clean/tweets_2018-08-22.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1032854831369789440:
            f = open('clean/tweets_2018-08-23.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1033217276089126912:
            f = open('clean/tweets_2018-08-24.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1033579687962968069:
            f = open('clean/tweets_2018-08-25.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1033941966218780673:
            f = open('clean/tweets_2018-08-26.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1034304113385848832:
            f = open('clean/tweets_2018-08-27.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1034666166848040960:
            f = open('clean/tweets_2018-08-28.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1035029330387247106:
            f = open('clean/tweets_2018-08-29.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1035391314328788993:
            f = open('clean/tweets_2018-08-30.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1035510785869602818:
            f = open('clean/tweets_2018-08-31.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1036478830159036417:
            f = open('clean/tweets_2018-09-02.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1036840933642436609:
            f = open('clean/tweets_2018-09-03.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1037203653373911041:
            f = open('clean/tweets_2018-09-04.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1037565805800710144:
            f = open('clean/tweets_2018-09-05.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1037927801578565632:
            f = open('clean/tweets_2018-09-06.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break
        elif int(tweet[0]) <= 1038290778387296256:
            f = open('clean/tweets_2018-09-07.json', "r", encoding="utf8", errors='ignore')
            tws = json.load(f)
            for i in tws:
                if i['id'] == tweet[0]:
                    fecha = i['date']
                    texto = i['text']
                    usuario = i['user_name']
                    tweetscompletos[tweet[0]] = (tweet[0], usuario, texto, fecha)
                    f.close()
                    break

    return tweetscompletos


def cargar_tweets():
    extraer_tweets('clean/tweets_2018-08-07.json')
    extraer_tweets('clean/tweets_2018-08-08.json')
    extraer_tweets('clean/tweets_2018-08-09.json')
    extraer_tweets('clean/tweets_2018-08-10.json')
    extraer_tweets('clean/tweets_2018-08-11.json')
    extraer_tweets('clean/tweets_2018-08-12.json')
    extraer_tweets('clean/tweets_2018-08-13.json')
    extraer_tweets('clean/tweets_2018-08-14.json')
    extraer_tweets('clean/tweets_2018-08-15.json')
    extraer_tweets('clean/tweets_2018-08-16.json')
    extraer_tweets('clean/tweets_2018-08-17.json')
    extraer_tweets('clean/tweets_2018-08-18.json')
    extraer_tweets('clean/tweets_2018-08-19.json')
    extraer_tweets('clean/tweets_2018-08-20.json')
    extraer_tweets('clean/tweets_2018-08-21.json')
    extraer_tweets('clean/tweets_2018-08-22.json')
    extraer_tweets('clean/tweets_2018-08-23.json')
    extraer_tweets('clean/tweets_2018-08-24.json')
    extraer_tweets('clean/tweets_2018-08-25.json')
    extraer_tweets('clean/tweets_2018-08-26.json')
    extraer_tweets('clean/tweets_2018-08-27.json')
    extraer_tweets('clean/tweets_2018-08-28.json')
    extraer_tweets('clean/tweets_2018-08-29.json')
    extraer_tweets('clean/tweets_2018-08-30.json')
    extraer_tweets('clean/tweets_2018-08-31.json')
    extraer_tweets('clean/tweets_2018-09-02.json')
    extraer_tweets('clean/tweets_2018-09-03.json')
    extraer_tweets('clean/tweets_2018-09-04.json')
    extraer_tweets('clean/tweets_2018-09-05.json')
    extraer_tweets('clean/tweets_2018-09-06.json')
    extraer_tweets('clean/tweets_2018-09-07.json')


def construir_indices():
    global indice
    global diccionario_tweets
    cargar_tweets()
    calculartf_idf()
    indexfile = open('index.json', 'w', encoding='utf-8', errors='ignore')
    indexfile.write(json.dumps(indice, ensure_ascii=False))
    indexfile.close()

    tweetindexfile = open('tweetindex.json', 'w', errors='ignore')
    tweetindexfile.write(json.dumps(diccionario_tweets, ensure_ascii=False))
    tweetindexfile.close()


def cargar_indices():
    f = open('index.txt', "r", encoding='utf8', errors='ignore')
    indice = json.load(f)
    f.close()

    f = open('tweetindex.txt', 'r', encoding='utf8', errors='ignore')
    diccionario_tweets = json.load(f)
    f.close()


construir_indices()


