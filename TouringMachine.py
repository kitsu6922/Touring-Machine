print("Selecciona un tipo de convercion y enseguida ingresa el texto \n\t 1:Upper\n\t 2:Lower\n\t 3:Capitalize\n\t 4:Title\n\t 5:Contrary \n Ejemplo:  3hola mundo")
cadena=input()
vector=list(cadena)
for x in range(1,len(vector),1):
    if vector[0]=="1":
        #Upper
        if vector[x].islower():
            vector[x]=vector[x].upper()
    elif vector[0]=="2":
        #Lower
        if vector[x].isupper():
            vector[x]=vector[x].lower()
    elif vector[0]=="3":
        #Capitalize
        if x==1 and vector[x].islower():
            vector[x]=vector[x].upper()
        elif x>1 and vector[x].isupper():
            vector[x]=vector[x].lower()
    elif vector[0]=="4":
        #Title
        if x==1 and vector[x].islower():
            vector[x]=vector[x].upper()
        elif x>1 and vector[x-1].isspace() and vector[x].islower:
            vector[x]=vector[x].upper()
    elif vector[0]=="5":
        #Contrary
        if vector[x].islower():
            vector[x]=vector[x].upper()
        elif vector[x].isupper():
            vector[x]=vector[x].lower()
    print(""+vector[x],end="")