import pickle
import json

print(".:Glosor:.")

glosor = []
#file = open("tglosor.dat", "w+")


Tread = input('Läs senaste glosor från fil? j/n :' )

if Tread=='j':
	with open('test.txt',  'rb') as fp: glosor = pickle.load(fp)
	print('läs fil')
	
else:
	print('mata in glosor')
	while 1:
		
		Sveglosa = input('Mata in Svensk Glosa: ')
		Engglosa = input('Mata in Engelsk Glosa: ')
		glosa = [Sveglosa, Engglosa]
		glosor.append(glosa)
		
		if 'n' == input('Vill du mata in en glosa till? j/n: '):
			break
			

while 1:
	print('\n' * 100)
	print('Nu startar glosförhöret')
	
	poeng=0
	
	for g in glosor:
		
		if g[1] == input(g[0] +' = '):
			print('Rätt!')
			poeng= poeng+1
			
		else:
			print('Fel! korrekt svar: ' + g[1])
			
	print('Du hade ' + str(poeng)+ ' av '+ str(len(glosor)))
	
	if 'n' == input('Vill du göra om förhöret? j/n: '):
		break
if 'j' == input('Vill du spara senaste glosor? j/n: '):
	with open('test.txt', 'wb') as fp: pickle.dump(glosor, fp)
	
	#file.writelines(glosor)
	#file.close()
	#glosor[]with.open('tglosor.dat', 'wb'):

		
		
