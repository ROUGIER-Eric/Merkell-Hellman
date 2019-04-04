from random import *

def binaire(entier):
	liste_bits =[]
	if entier < 256:
		while entier != 0 :
			liste_bits.append(entier%2)
			entier = entier//2
		longueur_liste = len(liste_bits)
		if longueur_liste <= 8:
			for loop in range(8-longueur_liste):
				liste_bits.append(0)
		liste_bits.reverse()
	return liste_bits
	
def encodage_phrase(texte):
	liste_codes = []
	for caractere in texte:
		liste_codes.append(ord(caractere))
	return liste_codes

def super_croissante():
	n = 50
	a1 = randint(1,n)
	a2 = randint(1,n)
	while a2 == a1:
		a2 = randint(1,n)
	if a1 < a2:
		sequence = [a1,a2]
	else:
		sequence = [a2,a1]
	somme = a1+a2
	for i in range(6):
		a = somme + randint(1,n)
		sequence.append(a)
		somme = somme + a
	return sequence
	
def pgcd(a,b):
	if a == 0:
		return b
	else:
		return pgcd(b%a,a)

def cle1(sequence):
	somme = 0
	for valeur in sequence:
		somme = somme + valeur
	return somme+randint(1,50)
	
def cle2(N):
	A = randint(2,N)
	while pgcd(A,N)!=1:
		A = randint(2,N)
	return A

def cle_privee():
	sequence = super_croissante()
	N = cle1(sequence)
	A = cle2(N)
	return [N, A, sequence]

def cle_publique(cle_pr):
	cle_pu = []
	A = cle_pr[1]
	N = cle_pr[0]
	for a in cle_pr[2]:
		cle_pu.append((A*a)%N)
	return cle_pu
		
def codage_lettre(cle_pu, lettre):
	w = binaire(ord(lettre))
	c = 0
	i = 0
	for b in cle_pu:
		c = c + w[i]*b
		i = i +1
	return c

def codage(cle_pu, texte):
	c = []
	for lettre in texte:
		c.append(codage_lettre(cle_pu, lettre))
	return c
	
def inverse(A, N):
	B = 2
	while (B*A)%N != 1:
		B = B +1
	return B
		
def decodage1(liste_c, N, A):
	B = inverse(A,N)
	p = []
	for c in liste_c:
		p.append((B*c)%N)
	return p

def decimal(nombre_bin):
	nombre = 0
	n = 7
	for b in nombre_bin:
		nombre = nombre + b*2**n
		n = n - 1
	return nombre
		
	
def decodage(liste_c, cle_pr):
	liste_p = decodage1(liste_c, cle_pr[0], cle_pr[1])
	cle = cle_pr[2]
	texte = ''
	for p in liste_p:
		x = [0, 0, 0, 0, 0, 0, 0, 0]
		rang = 7
		while p != 0:
			if p >= cle[rang]:
				p = p - cle[rang]
				x[rang] = 1
			rang = rang - 1
		texte = texte + chr(decimal(x)) 
	return texte	
	
	
#N = 881
#A = cle2(N)
#cle_pr = [N,A,[2,7,11,21,42,89,180,354]]
#cle_pu = cle_publique(cle_pr)
#print("Voici la cle_publique utilisée : ", cle_pu) 
#message = input("Saisir un message : ")
#code = codage(cle_pu, message)
#print("Voici le code : ", code)
#print("Et le voici décrypté : ", decodage(code, cle_pr))
