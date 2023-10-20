import os

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\tJippi! nya glosor")

    glosdictonary = {}

    while True:
        val = print_menu()
            
        if val=="1":#mata in nya glosor
            glosdictonary = add_glosor()
            print(f"Bug= {type(glosdictonary)}")
            input("Väntar")
            #os.system('cls' if os.name == 'nt' else 'clear')

        elif val=="2":#kör glosförhör
            starta_forhor(glosdictonary)
        
        else:#exit program
            break

    

#-------------------------------------------------------------------
def print_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\t-:MENU:-")
    print("\t1. Mata in nya glosor som sen sparas")
    print("\t2. Kör glosförhör")
    print("\t3. Avsluta programmet")

    return input("\n\n\tMata in val: ")

def add_glosor():
    t_glosdictonary = {}
    #Mata in
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        sweglosa = input("\n\tMata in Svensk glosa: ")
        utlglosa = input("\n\tMata in utlänsk stavning: ")
 
        t_glosdictonary[sweglosa] = utlglosa
        
        en_till = input("\n\tVill du mata in en till? j/n ")

        if (en_till == "n"):
            break


    return t_glosdictonary
    
def starta_forhor(input_dictonary):

    input("\n\tNu startar glosförhöret, press enter ")

    #for glosa in input_dictonary:
            
        #svar = input(f"\n\t{glosa}: ")
        
        #if (svar == input_dictonary[glosa]):
         #   print("\tRätt!\n")

        #else:
         #   print(f"\tFel svar, korrekt är: {input_dictonary[glosa]}\n")


main()