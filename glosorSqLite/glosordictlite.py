import os
import random
import glosor_db_handler

db_handler =  glosor_db_handler.glosor()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
        

    while True:
        val = print_menu()
            
        if val=="1":#mata in nya glosor
            #db_handler.my_drop_table()
            #db_handler.create_table()
            add_glosor()
            #print(f"Bug= {type(glosdictonary)}")
            
            #os.system('cls' if os.name == 'nt' else 'clear')

        elif val=="2":#kör glosförhör
            #glosdictonary = db_handler.get_glosor_from_db()
            starta_forhor()
        
        else:#exit program
            break

    
#-------------------------------------------------------------------
def print_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\t-:MENU:-")
    print("\t1. Mata in nya glosor som sen sparas i databasen")
    print("\t2. Kör glosförhör med glosor från Databasen")
    print("\t3. Avsluta programmet")

    return input("\n\n\tMata in val: ")

#--------------------------------------------------------------------------
def add_glosor():
    #t_glosdictonary = {}
    db_handler.my_drop_table()
    db_handler.create_table()
    #Mata in
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        sweglosa = input("\n\tMata in Svensk glosa: ")
        utlglosa = input("\n\tMata in utlänsk stavning: ")

        db_handler.add_glosa_to_table(sweglosa, utlglosa)
 
        #t_glosdictonary[sweglosa] = utlglosa

        en_till = input("\n\tVill du mata in en till? j/n ")

        if (en_till == "n"):
            break

    
    
def starta_forhor():

    input_dictonary = db_handler.get_glosor_from_db()


    
    
    #keys = input_dictonary.keys()
    #random.shuffle(keys)
    #for key in keys:
        #print key, my_dict[key]
    antal_ratt = 0

    os.system('cls' if os.name == 'nt' else 'clear')
    input("\n\tNu startar glosförhöret, press enter ")


    #for glosa in input_dictonary:
    for glosa in input_dictonary:
        #os.system('cls' if os.name == 'nt' else 'clear')            
        svar = input(f"\n\t{glosa}: ")
        
        if (svar == input_dictonary[glosa]):
            print("\tRätt!\n")
            antal_ratt = antal_ratt + 1 

        else:
           print(f"\tFel svar, korrekt är: {input_dictonary[glosa]}\n")

    print(f"\n\tDu hade {antal_ratt} av {len(input_dictonary)} rätt")
    input("\n\tFortsätt press: Enter ")

main()