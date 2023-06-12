import speech_recognition as sr
import spacy
import webbrowser

nlp = spacy.load('pt_core_news_sm')


def ouvir_microfone():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Fale algo:")
        audio = r.listen(source)

    texto = r.recognize_google(audio, language='pt-BR')

    return texto


def pesquisar_temas(temas):
    url = 'https://www.google.com/search?q=' + temas.replace(' ', '+')
    webbrowser.open(url)

def repetir_fala():
    while True:
        fala = ouvir_microfone()
        if fala.lower() == "parar" or fala.lower() == "sair" or fala.lower() == "tchau" or fala.lower() == "para":
            print("Encerrando...")
            break
        print("Você disse: " + fala)
        listaDePalavras = fala.split(" ")
        pegarPalavrasRepetidas = set([palavra for palavra in listaDePalavras if listaDePalavras.count(palavra) > 1])
        print("Palavras repetidas: " + str(pegarPalavrasRepetidas))
        pesquisar_temas(fala)


repetir_fala()
