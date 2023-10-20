import os

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\tJippi! nya glosor")

    glosdictonary = {}
    
    #Mata
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        sweglosa = input("\n\tMata in Svensk glosa: ")
        utlglosa = input("\n\tMata in utlänsk stavning: ")
 
        glosdictonary[sweglosa] = utlglosa
        
        en_till = input("\n\tVill du mata in en till? j/n ")

        if (en_till == "n"):
            break

    os.system('cls' if os.name == 'nt' else 'clear')        
    while True:
    
        input("\n\tNu startar glosförhöret, press enter ")

        for glosa in glosdictonary:
            
        
            svar = input(f"\n\t{glosa}: ")

            if (svar == glosdictonary[glosa]):
                print("\tRätt!\n")

            else:
                print(f"\tFel svar, korrekt är: {glosdictonary[glosa]}\n")

        one_more_time = input("\n\tVill du göra förhöret en gång till? j/n ")

        if one_more_time == "n":
            break

#-------------------------------------------------------------------
main()