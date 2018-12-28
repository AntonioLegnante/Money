#scambio importo con il minor numero possibile di banconote da 20,10,5 e 1
print ("determina il numero minimo di banconote")
importo=int (input ("inserisci l'importo \t"))
venti = int (importo/20)
importo%=20
dieci = int (importo/10)
importo%=10
cinque =int (importo/5)
importo%=5 
uno =int (importo/1)
print ("banconote da 20 =" , venti ," 10 =" , dieci ," 5 =" , cinque , "1 =" , uno) 
