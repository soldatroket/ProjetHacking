#!/usr/lib/python
#-*- coding: utf-8 -*-
import random
import smtplib
import sql
import cgitb
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
cgitb.enable()

class Pass:
	def SendPass(self, mail, password):
		#Fonction Utilissé pour envoyé un mail
		Fromadd = "nathan.larrouy@gmail.com"
		Toadd = mail    ##  Spécification des destinataires
		cc = [""]    ## Spécification des destinataires en copie carbone (cas de plusieurs destinataires)
		bcc = ""    ## Spécification du destinataire en copie cachée (en copie cachée)
		message = MIMEMultipart()    ## Création de l'objet "message"
		message['From'] = Fromadd    ## Spécification de l'expéditeur
		message['To'] = Toadd    ## Attache du destinataire à l'objet "message"
		message['CC'] = ",".join(cc)    ## Attache des destinataires en copie carbone à l'objet "message" (cas de plusieurs destinataires)
		message['BCC'] = bcc    ## Attache du destinataire en copie cachée à l'objet "message"
		message['Subject'] = "Concours Hacking : Mot de passe"    ## Spécification de l'objet de votre mail
		msg = "Bonjour,\nVoici votre lien unique pour (re)definir votre mot de passe pour le concours : http://concours.unityscript.fr/resetpassword.py?token="+password+" "    ## Message à envoyer
		message.attach(MIMEText(msg.encode('utf-8'), 'plain', 'utf-8'))    ## Attache du message à l'objet "message", et encodage en UTF-8
		serveur = smtplib.SMTP('smtp.gmail.com', 587)    ## Connexion au serveur sortant (en précisant son nom et son port)
		serveur.starttls()    ## Spécification de la sécurisation
		serveur.login(Fromadd, "decharge40")    ## Authentification
		texte= message.as_string().encode('utf-8')    ## Conversion de l'objet "message" en chaine de caractère et encodage en UTF-8
		Toadds = [Toadd] + cc + [bcc]    ## Rassemblement des destinataires
		serveur.sendmail(Fromadd, Toadds, texte)    ## Envoi du mail
		serveur.quit()    ## Déconnexion du serveur

	def GeneratePass(self, mail):
		#Fonction utilisé pour généré un mot de passe
		char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabsdefghijklmnopqrstuvwxyz0123456789"
		token = ""
		for i in range(0, 10):							#On fait une boucle de 0 à 10 qui correspond à la longeur du mot de passe
			token += char[random.randint(0,len(char)-1)]			#On séléctionne un charactére aléatoire dans la chaine "char"
		self.SendPass(mail, token)						#On envoye le mdp à l'email concerné
		sqlDB=sql.SQLTest("concours")
		sqlDB.AddEntry("resetmdp", "token, mail", (token, mail))		#On crée le token dans la base SQL qui nous permettrat de vérifier la validiter de la demande
		return token
