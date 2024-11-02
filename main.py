None
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            'SIGMA':'una persona que es superior que otras',
            'RIZZ':'cuando una persona coquetea con otra',
            'SKIBIDI':'es una animacion de youtube sobre inodoros cantantes',
            'SUS':'algo sospechoso',
            'FLEX': 'presumir algo',
            }
print (meme_dict.keys())
word = input('Escribe una palabra que no entiendas').upper()
if word in meme_dict:
    print ('Significado:', meme_dict [word])
else:
    print('la palabra aun no esta en el diccionario')  
