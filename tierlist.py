from turtle import color
import matplotlib.pyplot as plt


allresult = []
lastname = []
while True:
    
    name = input("Name: ")


    marrant = int(input("rate " + name + " funny: "))
    chiant = int(input("rate "+ name + " chiant: "))
    conversation = int(input("rate "+ name + " conversation: "))
    confiance = int(input("rate "+ name + " confiance: "))
    empathique = int(input("rate "+ name + " empathy: "))
    intelligence = int(input("rate "+ name + " intelligence: "))
    orateur = int(input("rate "+ name + " orateur: "))
    interet_commun = int(input("rate "+ name + " common interest: "))


    resultat = ((marrant - chiant + interet_commun + conversation + confiance + intelligence + orateur + empathique)/7)
    print(resultat)
    allresult.append(resultat)
    lastname.append(name)
    if input("Press enter to continue or stop to quit: ").lower() == "stop":
        break

print(allresult)    
print(lastname)    
plt.bar(lastname, allresult, color='red')
plt.show()
