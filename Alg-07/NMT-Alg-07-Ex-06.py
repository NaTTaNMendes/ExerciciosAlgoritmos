def isAnagrama(string1, string2):
    """
    Retorna verdadeiro se as duas strings são anagramas.
    """
    string1 = string1.upper()
    string1 = string1.replace(" ", "")
    string2 = string2.upper()
    string2 = string2.replace(" ", "")
    letras = "ABCDEFGHIJKLMNOPQRSTUBWXYZ"
    dict1 = {}
    dict2 = {}

    for letra in string1:
        if (dict1.get(letra) != None):
            dict1[letra] = dict1[letra] + 1
        elif (letra in letras):
            dict1[letra] = 1

    for letra in string2:
        if (dict2.get(letra) != None):
            dict2[letra] = dict2[letra] + 1
        elif letra in letras:
            dict2[letra] = 1
    
    if (dict1.items() == dict2.items()):
        return True
    else:
        return False

def main():
    palavra1 = "William Shakespeare"
    palavra2 = "I am a weakish speller"

    if (isAnagrama(palavra1, palavra2)):
        print("São anagramas")
    else:
        print("Não são anagramas")

if __name__=="__main__":
    main()