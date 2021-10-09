score = 0
# Vraag 1
antwoord1 = input("Waar woon ik? \na. Amsterdam \nb. Purmerend \nc. Alkmaar \nAntwoord: ")
if antwoord1 == "a" or antwoord1 == "Amsterdam":
    score += 1
    print("Correct!")
    print("Score: ", score)
    print("\n")
else: 
    print("Incorrect! De antwoord was Amsterdam.")
    print("Score: ", score)
    print("\n")

# Vraag 2
antwoord2 = input("Welk afkomst heb ik? \na. Truks \nb. Algerijns \nc. Marokkaans \nAntwoord: ")
if antwoord2 == "c" or antwoord2 == "Marokkaans":
    score += 1
    print("Correct!")
    print("Score: ", score) 
    print("\n")
else:
    print("Incorrect! De antwoord was Marokkaans.")
    print("Score: ", score)
    print("\n")

# Vraag 3
antwoord3 = input("Wat is mijn hobby? \na. Voetbal \nb. MMA \nc. Gamen \nAntwoord: ")
if antwoord3 == "b" or antwoord3 == "MMA":
    score += 1
    print("Correct!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect! De antwoord was MMA.")
    print("Score: ", score)
    print("\n") 

# Laaste bericht    
if score <= 1:
    print("Je totale score is:", score, "- BAKAYARO!")
elif score == 2:
    print("Je totale score is:", score, "- Okay.")
else:
    print("Je totale score is:", score, "- Nice!.")
                       
    


