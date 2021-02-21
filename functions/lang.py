def hi (lang):
    if lang == "en":
        print("Hello!!!")
    elif lang == "ro":
        print("Salut!!!")
    elif lang == "ru":
        print("Привет")
     
def bye (f):
    if f == "en":
        print("Good Bye!!!")
    elif f == "ru":
        print("До свидание!!!")
    elif f =="ro":
        print ("La revedere!!!")    
    else: 
        print("Вы должны выбрать язык из предложеных(ru,en,ro)")   
         
x=input("Выберите язык ru,ro,en:")
hi(x) 
bye(x)   