#Använder dictionary istället för list i list
def main():
    glosLista = {}

    print("GLOSOR!")
    while True:
        svGlosa = input("Ange en svensk glosa: ")
        enGlosa = input("Ange den engelska översättningen: ")

        glosLista.update({svGlosa : enGlosa})
        
        fortsatt  = input("Vill du ange fler? j/n: ")
        if fortsatt == "n":
            break

    while True:
       

        print("\n Nu start glosförhöret!")

        for glosa in glosLista:
            svar = input(f"\n {glosa} : ")

            if svar == glosLista[glosa]:
                print(" Rätt svar!")
            else :
                print(f"\nFel svar, det är {glosLista[glosa]}")
       
        fortsatt2  = input("Vill du köra om? j/n: ")
        if fortsatt2 == "n":
            break

main()