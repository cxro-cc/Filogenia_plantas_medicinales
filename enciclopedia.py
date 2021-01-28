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
En él encontrarás información de cada compuesto junto con el artículo de la información, 
una vez dentro del árbol de cada compuesto puedes dar click en el número de acceso o en el nombre científico para llevarte
a los enlaces que necesitas uwu \n""")

func_comp = ("""    Como antidiabético
    Para metabolismo de glucosa y lípidos
    Como antiinflamatoria, antioxidante y anticancerigena
    Con actividad hipoglucemiante
    Como antioxidante \n""")

des_func = (""" Elige el número que desees, te llevará a una filogenia y al artículo del compuesto (: :    
    1- Antidiabético (kaempferol)
    2- Metabolismo de glucosa y lípidos (ac. clorigenico)
    3- Antiinflamatoria, antioxidante y anticancerigena (pinocembrin)
    4- Actividad hipoglucemiante (urseno)
    5- Antioxidante y capta radicales libres (flavonoide) \n""")

para_1 = ("https://htmlpreview.github.io/?https://github.com/cxro-cc/Filogenia_plantas_medicinales/blob/main/kaemp.html")
para_2 = ("https://htmlpreview.github.io/?https://github.com/cxro-cc/Filogenia_plantas_medicinales/blob/main/ac_clorogenico.html")
para_3 = ("https://htmlpreview.github.io/?https://github.com/cxro-cc/Filogenia_plantas_medicinales/blob/main/pino.html")
para_4 = ("https://htmlpreview.github.io/?https://github.com/cxro-cc/Filogenia_plantas_medicinales/blob/main/urseno.html")
para_5 = ("https://htmlpreview.github.io/?https://github.com/cxro-cc/Filogenia_plantas_medicinales/blob/main/flavonide.html")

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
        elif elige == "4":
            webbrowser.open(para_4)
            webbrowser.open("https://onlinelibrary.wiley.com/doi/abs/10.1002/ptr.966")
        elif elige == "5":
            webbrowser.open(para_5)
            webbrowser.open("https://www.redalyc.org/articulo.oa?id=579/57938407")
        else:
            print ("oh, eso no hay")
    else:
        print ("Uh... lo intentamos")
        quit()
else:
    print ("Bueno, adiós (:")
