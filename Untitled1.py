#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Calcula la multiplicació i la suma de dos números. Donats
#dos nombres de tipus integer, retorna el seu producte
#només si el producte és igual o inferior a 1000, si no,
#retorna la seva suma.

def suma (a,b):
    resul= a + b
    return resul

def multi (a,b):
    resul= a * b
    return resul

var1 = int(input("ingrese la variable 1 "))
var2 = int(input("ingrese la variable 2 "))

resul=multi(var1,var2)
resul2=suma(var1,var2)

if resul <= 1000:
    print (("la multiplicacion es "), resul)
else:
    print (("la suma es "), resul2)


# In[2]:


#2. Imprimeix per pantalla els primers 15 números naturals
#fent servir un bucle while.

i = 0
while (i <= 14):
    i +=1
    print (i, end=",")


# In[3]:


#3. Imprimeix per pantalla els primers 15 números naturals
#fent servir un bucle for.

for i in range (1, 16):
    print (i, end=",")


# In[20]:


#4. Calcula la suma d'1 a un número donat que l’usuari pot
#introduir per pantalla.

def suma_divisores(numero):
    suma = 0
    for i in range (1, numero + 1):
            suma += i
    return suma

numero = int(input("Ingresa un número: "))
print("La suma de sus divisores es: ")
print(suma_divisores(numero))


# In[29]:


#5. Escriu un programa que calcula la taula de multiplicar d’un
#número que l’usuari pot introduir per pantalla.

numero = int(input("Introduce un número: "))
for i in range (0,11):
    resultado = i * numero
    print(("%d x %d = %d") % (numero, i, resultado))


# In[2]:


#6. Donada la llista list = [20, 60, 80, 100], imprimeix-la per
#pantalla de manera invertida.

lista = [20,60,80,100]
lista.reverse()
print (lista)


# In[43]:


#7. Troba (imprimint per pantalla) l’element més gran d’una
#llista de nombres creada per tu.

x = [1,67]
print (("El número mas grande es: "), max(x))


# In[3]:


#8. Comptabilitza la quantitat de lletres, dígits i símbols
#especials de la llista donada. → string =
#[&#Pr@j3ctE#D4M#&]

texto = "&#Pr@j3ctE#D4M#&"

alf = 0
dig = 0
sim = 0

for i in texto:
    if i.isalpha() == 1:
        alf += 1
    elif i.isdigit() == 1:
        dig += 1
    else:
        sim += 1
       
print (("letras: "), alf, (" dig: "), dig, ("sim: "), sim)


# In[ ]:




