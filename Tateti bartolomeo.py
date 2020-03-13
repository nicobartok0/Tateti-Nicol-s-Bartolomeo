print ("TATETI")
loop = 1
a = "A"
b = "B"
c = "C"
d = "D"
e = "E"
f = "F"
g = "G"
h = "H"
i = "I"
while loop == 1:
	print(a, "!", b ,"!", c)
	print(d, "!", e ,"!", f)
	print(g, "!", h ,"!", i)
	
	if a == b and b == c or d == e and e == f or g == h and h == i or a == d and d == g or b == e and e == h or c == f and f == i or a == e and e == i or c == g and g == e:
		print ("TRES EN RAYA")
		loop = 2
		exit() 
		
	print("Jugador 1, ingrese un espacio.")

	lugar = input("Ingrese un valor: ")
	if lugar == a:
		a = "X"
	
	if lugar == b:
		b = "X"
	
	if lugar == c:
		c = "X"
	
	if lugar == d:
		d = "X"
	
	if lugar == e:
		e = "X"
	
	if lugar == f:
		f = "X"
	
	if lugar == g:
		g = "X"
	
	if lugar == h:
		h = "X"
	
	if lugar == i:
		i = "X"
	
	print(a, "!", b ,"!", c)
	print(d, "!", e ,"!", f)
	print(g, "!", h ,"!", i)
	
	if a == b and b == c or d == e and e == f or g == h and h == i or a == d and d == g or b == e and e == h or c == f and f == i or a == e and e == i or c == g and g == e:
		print ("TRES EN RAYA")
		loop = 2
		exit() 
		
	print("Jugador 2, ingrese un espacio.")

	lugar = input("Ingrese un valor: ")
	if lugar == a:
		a = "O"
	
	if lugar == b:
		b = "O"
	
	if lugar == c:
		c = "O"
	
	if lugar == d:
		d = "O"
	
	if lugar == e:
		e = "O"
	
	if lugar == f:
		f = "O"
	
	if lugar == g:
		g = "O"
	
	if lugar == h:
		h = "O"
	
	if lugar == i:
		i = "O"
	if a == b and b == c or d == e and e == f or g == h and h == i or a == d and d == g or b == e and e == h or c == f and f == i or a == e and e == i or c == g and g == e:
		print ("TRES EN RAYA")
		loop = 2
		exit() 



