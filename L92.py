#Leena and Elise
#Lab9

names = {"Macrowski":"Allison","Newton":"Abigail","Lombardo":"Emma","Bradley":"Leena","Burns":"Therese","Antimo":"Viviana","Lopez":"Abigail","Aguirre":"Anastacia","Ward":"Elise","Eidelbes":"Sydney","Patin":"Samantha","Guo":"Mandy"}
same = []
d = {}
for key,value in names.items():
    if value not in d:
        d[value] = 1
    else:
        d[value] = d[value] + 1
        same.append(value)
        

        
print(same)
    
names = {"Macrowski":"Allison","Newton":"Abigail","Lombardo":"Emma","Bradley":"Leena","Burns":"Therese","Antimo":"Viviana","Lopez":"Abigail","Aguirre":"Anastacia","Ward":"Elise","Eidelbes":"Sydney","Patin":"Samantha","Guo":"Mandy"}

