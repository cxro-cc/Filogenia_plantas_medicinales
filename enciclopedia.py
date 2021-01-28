#! py
import webbrowser
planta = ("""Hola, bienvenidx a la enciclopedia de plantas medicinales (: 
   ____________________________________
   ------------------------------------
   ||              &&&               ||
   ||            %#%%%%% /#          ||
   ||        *#. ###%%& (###%        ||
   ||        #(%%* #%%%#% %###       ||
   ||      ###  ###%%%%%%#(( ##      ||
   ||        ###%%%%%%## %%#((#      ||
   ||     ###%%%#&#%&%%### ,%###     ||
   ||       %%.  %%%%%%#######%      ||
   ||        #((#%%%&&%#(#%%#(       ||
   ||          %%# % #%%%#,          ||
   ||               %                ||
   ____________________________________
   ------------------------------------

Este es un banco de filogenias de componentes activos de plantas los cuales son utilizados para tratar diferentes enfermedades,
En él encontrarás información de cada compuesto y ... 
una vez dentro del árbol de cada compuesto puedes dar click para ir a la información de la planta y de la secuencia
utilizada \n""")

func_comp = ("""    Como antidiabetico
    Para metabolismo de glucosa y lípidos
    Como antiinflamatoria, antioxidante y anticancerigena
    Para... \n""")

des_func = (""" Elige el número que desees, te llevará a una filogenia y al artículo del compuesto (: :    
    1- Antidiabético (kaempferol)
    2- Metabolismo de glucosa y lípidos (ac. clorigenico)
    3- Antiinflamatoria, antioxidante y anticancerigena (pinocembrin)
    4- \n""")

para_1 = ("https://htmlpreview.github.io/?https://github.com/cxro-cc/Filogenia_plantas_medicinales/blob/main/kaemp.html")
para_2 = ("https://htmlpreview.github.io/?https://github.com/cxro-cc/Filogenia_plantas_medicinales/blob/main/ac_clorogenico.html")
para_3 = ("https://htmlpreview.github.io/?https://github.com/cxro-cc/Filogenia_plantas_medicinales/blob/main/pino.html")

print (planta)

op= str(input(""" Por el momento solo tenemos plantas para tratar la diabetes, 
¿Deseas ver la función de cada compuesto? (s/n) \n"""))
if op == "s":
    print (func_comp)
    interes = str(input("""¿Te interesa ver alguno? (s/n) \n"""))
    if interes == "s":
        elige = str(input(des_func))
        if elige == "1":
            webbrowser.open(para_1)
            webbrowser.open("https://pubmed.ncbi.nlm.nih.gov/26536892/")
        elif elige == "2":
            webbrowser.open(para_2)
            webbrowser.open("https://www.hindawi.com/journals/ecam/2013/801457/")
        elif elige == "3":
            webbrowser.open(para_3)
            webbrowser.open("https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3747598/")    
        else:
            print ("oh, eso no hay")
    else:
        print ("Uh... lo intentamos")
        quit()
else:
    print ("Bueno, adiós (:")
