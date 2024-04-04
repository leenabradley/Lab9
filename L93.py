#Leena and Elise
#L93.py

cpsc_names = ["Allison","Macrowski","Abigail","Newton","Emma","Lombardo","Leena","Bradley","Therese","Burns","Viviana","Antimo","Abigail","Lopez","Anastacia","Aguirre","Elise","Ward","Sydney","Eidelbes","Samantha","Patin","Mandy","Guo"]

d = {}
for lastname in cpsc_names[1::2]:
    first = lastname[0] 
    if first not in d:
        d[first] = 1
    else:
        d[first] += 1
        
print(d)
