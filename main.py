#Diccionario
meme_dict = {
    "CRINGE": "algo raro o embarazoso",
    "LOL": "una respuesta a algo gracioso",
    "CREEPY":"aterrador, siniestro"
}
#variable
word = input("Ingrese la palabra a consultar").upper()

if word in meme_dict.keys():
    print("esa palabra significa...",meme_dict[word])
else:
    print("No existe esa palabra o esta mal escrita")
