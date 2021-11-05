import os
import sys
import time

def main():
    def Airport():
        print("je komt aan bij de airport. ga je legal of illigaal vliegen?")
        answer4 = input("\nA.Legaal\nB.Illigaal\nAntwoord: ")
        if answer4.casefold() == "A".casefold():
            print("\nje betaalt voor je ticket en kom enje gaat nu in de vliegtuig naar nederland.")
            print("je bent aangekomen in nl  je wordt gestuurd naar de vlugtelingen kamp.\n EINDE")
        elif answer4.casefold() == "B".casefold():
            print("de doune heeft je gepakt en je gaat naar de gevangenis")
            restartprogram()
        






    def restartprogram(): 
        restart = input("Begin op nieuw?(y/n): ")
        if restart.casefold() == "y":
            print("-----------------------------------------------------------------")
            main()
        else:
            print("\nok dan niet")
            exit()
    answer1 = input("Er is oorlog in afghanistan jij en ze gezin proberen weg te gaan van de bombardementen. Waar gaan jullie naar toe:\n\nA. jullie verstoppen in Dichtbij zijnde gebouw. \nB. jullie stappen in de auto en gaan naar het vliegveld.\nC. Verstoppen in een steegje totdat die explosies zijn gestopt.\nAntwoord: ")
    if answer1.casefold() == "A".casefold():
        print("De gebouw wordt geraakt ze zitten onder het puin. je zit vast. Wat doe je\n")
        answer2 = input("A. je roept naar hulp.\nB. Je probeert je kracht gebruiken om de stenen weg te halen.\nC. Je geeft op en blijft gewoon liggen.\nAntwoord: ")
        if answer2.casefold() == "A".casefold():
            print("Je Schreeuwt met alles wat je hebt.")
            for i in range(0,3):
                print("...")
                time.sleep(2)
                if i == 3:
                    break
            print("Maar niemand hoorde je")
            restartprogram()
        if answer2.casefold() == "B".casefold():
            print("het is je gelukt en je rent nu weg met je kinder naar het vliegveld")
            Airport()
        if answer2.casefold() == "C".casefold():
            print("Je geeft op en blijft gewoon liggen. Je ging dood aan bloedverlies")
            restartprogram()
    if answer1.casefold() == "B".casefold():
        Airport()

    if answer1.casefold() == "C".casefold():
      print("Jullie zijn verstopt in dichtbij zijnde steegje. De explosies komen steeds dichterbij. 1 van de bommen raak het gebouw 2 straten veder van jullie.De explosies zijn gestopt. Wat doe je")
      answer3 = input("A.Naar je auto rennen en naar het vliegveld\nB.Lopen naar het vliegveld\nC. Zoek iemand die kan helpen om naar het vliegveld te komen.\nAntwoord: ")
      if answer3.casefold() == "A".casefold():
          Airport()
      if answer3.casefold() == "B".casefold():
          Airport()
      if answer3.casefold() == "C".casefold():
          print("Hij brengt jullie naar de vliegveld\n")
          Airport()
main()




    
     

