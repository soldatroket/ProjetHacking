#!/usr/bin/env python
#coding: utf-8

#Script de vérification d'énigmes

import cgi
import Utils
import cgitb
import ldap
import Template
import hashlib
import mysql.connector
cgitb.enable()

formulaire = cgi.FieldStorage()

CookiesMod=Utils.cookies()
SessionToken=CookiesMod.ReadSession('session')
name=CookiesMod.ReadSession('name')
teamName=CookiesMod.ReadSession('teamName')
dnIUT=CookiesMod.ReadSession('DNiut')
Status=CookiesMod.ReadSession('status')

###################################################TRAITEMENT############################################################

if Status=="student" and teamName!="Pas de resultat":					#On verifie que le joueur est un étudiant et qu'il fait partit d'une équipe
	if formulaire.getvalue("ID")!=None and formulaire.getvalue("reponse")!=None:	#On vérifie que l'ont à reçu un ID d'énigme et une réponse
		sqlDB=Utils.SQLTest("equipes")
		DNTeam=CookiesMod.ReadSession('DNteamName')				#On lit le cookie DNteamName
		sha=hashlib.sha1()
        	sha.update(formulaire.getvalue("reponse"))
        	reponse=sha.hexdigest()							#On code la réponse en sha1
		ID=cgi.escape(formulaire.getvalue("ID"))				#On récupére l'ID de la question
		verifQ=sqlDB.VerifQuestionTeam(teamName, ID)				#On verifie si l'équipe à deja répondue à la question(False=répondue\True=pas répondue)
		if verifQ==True:
			sqlDB.SetDB("concours")
			verifR=sqlDB.Compare("enigmes", "reponse", "ID ="+ID, reponse)	#On vérifie que la réponse reçue est juste
			if verifR==True:
				sqlDB=Utils.SQLTest("concours")
				point=sqlDB.Search("point", "enigmes", "ID="+ID)	#On récupére le nombre de point associer à l'énigme dans la base SQL
				LdapMod=Utils.LdapTest()
				LdapMod.AddScore(point[0][0], DNTeam)			#On ajoute ce score à l'équipe qui à répondue
				sqlDB.SetDB("equipes")
				sqlDB.AddEntry(teamName, "ID, IDQuestion", (0,ID))	#On inscrit sur la base SQL le fait que l'énigme est répondue à la question
				Template.Error.Display("Bravo vous avez trouver", "enigmeliste.py")
			else:
				Template.Error.Display("Et non dommage :(", "enigme.py?ID="+ID)
		else:
			Template.Error.Display("Ton équipe a deja répondue a cette question....", "enigmeliste.py")
	else:
		Template.Error.Display("Erreur", "enigmeliste.py")
else:
	Template.Error.Display("Seul les étudiants inscrit dans une équipe peuvent répondre aux énigmes", "enigmeliste.py")
