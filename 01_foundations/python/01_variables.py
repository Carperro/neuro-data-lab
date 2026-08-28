#Create a python program that stores your name, age, height, whether you are studying, and how many hours you studied today.
#Then calculate how many hours you would study in one week if you maintained the same daily schedule.

name = "Nico"           #Python detecta automaticamente el tipo de variable, no es necesario declarar el tipo de variable.
age = 28                #Los números enteros se representan con int (integer)
height = 1.74           #Los números decimales se representan con float (floating point)
is_student = True       #Los datos booleanos se representan con True o False (con mayúscula inicial)
study_hours = 14         #This number is integer and represents the hours studied today.


#This variable calculates the total hours that would be studied in one week, one month, and one year, if the same daily schedule is maintained.
weekly_hours = study_hours * 7 
monthly_hours = study_hours * 30
yearly_hours = study_hours * 365


#print(name)       #print() es una función que permite mostrar información como output en la consola.
#print(age)        #Comentaremos estas funciones para que no se muestren en el output.
#print(height)
#print(is_student)
#print(study_hours)
#print(weekly_hours)

#Como el output es aún poco legible, podemos mejorar la presentación de la información utilizando f-strings para formatear el output de manera más clara y comprensible.
#Para que sea más legible, podemos agregar saltos de línea en el output utilizando el carácter especial \n dentro del f-string.
#O podemos utilizar triple comillas para crear un string multilínea, como se muestra en el ejemplo anterior. 
#Esto permite que cada variable se muestre en una línea separada, mejorando la claridad del output.

presentation = f"""
Name: {name} 
Age: {age}
Height: {height}
Is student: {is_student}
Study hours today: {study_hours}
Weekly study hours: {weekly_hours}

Based on this schedule:
Monthly study hours: {monthly_hours}
Yearly study hours: {yearly_hours}"""
print(presentation)

#Para borrar variables de la memoria, podemos utilizar la keyword/statement 'del' que permite eliminar variables de manera explícita.
# del name, age, height, is_student, study_hours, weekly_hours, presentation <- de esta manera, podemos liberar memoria y evitar posibles errores en el programa.

#Now we can operate with the variables to perform calculations or comparisons.
#Calculate the hours that would be studied in one moth, and in one year, if the same daily schedule is maintained.

#For the month, we will assume that a month has 30 days, and for the year, we will assume that a year has 365 days.

#print(f"""
#Based on this schedule:

#Monthly study hours: {monthly_hours}
#Yearly study hours: {yearly_hours}""")

#We can add this code to the presentation variable to show all the information in a single output. 
#But for that, we need to declarate this variables before the presentation variable, so that they can be used in the f-string.

#Before the first commit, prove one last thing.
#We can use the type() function to check the type of a variable, and we can use the id() function to check the memory address of a variable.
print(type(name))
print(type(age))
print(type(height))
print(type(is_student)) 