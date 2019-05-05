print('.:GLOSOR:.\n')

gloslistaArray=[]

mata='j'
i=0
tempglosa='';

while (mata != 'n'):
    glosaArray=[]
    #tempglosa = input('Mata in glosa separerat med : ex hund:dog ')
    input_variable = input("Mata in svensk glosa: ")
    input_variable2 = input("Mata in engelsk glosa: ")
    #tempglosa = str(input_variable)
    glosaArray.append(str(input_variable))
    glosaArray.append(str(input_variable2))    
    
    #print(tempglosa)
    
    #glosArray=tempglosa.split(":")
    #print(glosaArray[0])
    gloslistaArray.append(glosaArray)
    mata = input('Vill du mata in en glosa till j/n? ')
    i = i+1
    

mata='j'


while (mata != 'n'):
    print ("\n" * 100)
    print('\nNu startar glos-testet!\n')
    t_antalR=0
    t_antalglosor = len(gloslistaArray)
    
    
    for a in gloslistaArray:
        sv_glosa=a[0] + ' = '
        en_glosa=a[1]
        
        
        
        tglosa = input(sv_glosa)
        
        if tglosa == en_glosa:
            print('korrekt! \n')
            t_antalR=t_antalR+1
            
        else:
            print('Fel svar! korrekt svar: ', en_glosa , '\n' )


    if t_antalR==t_antalglosor :
        print('Grattis du kunde alla! Bra jobbat!')
    else :
        print('Du hade ', t_antalR , ' av ', t_antalglosor , 'stycken!')
    
    mata = input('Vill repetera provet j/n? \n')


#clearscreen = input('Vill clear screen j/n? ')

#if clearscreen == 'j':
    #emty screen
    #print(chr(27) + "[2J")import os
    
    #os.system('cls' if os.name == 'nt' else 'clear')
    #print ("\n" * 100) #Denna funkar!
