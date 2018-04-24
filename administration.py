#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Script qui centralise toutes les fonctionnalités liée à l'administration

import cgi
import Utils
import cgitb
import ldap
import Template
import mysql.connector
cgitb.enable()

###########################################################RECUPERATIONS DES COOKIES#################################################################
CookiesMod=Utils.cookies()
SessionToken=CookiesMod.ReadSession("session")
name=CookiesMod.ReadSession('name')
teamName=CookiesMod.ReadSession('teamName')
dnIUT=CookiesMod.ReadSession('DNiut')
Status=CookiesMod.ReadSession('status')
DNteam=CookiesMod.ReadSession('DNteamName')

formulaire = cgi.FieldStorage()

if formulaire.getvalue('type') != None:
	TypeF=formulaire.getvalue('type')
else:
	TypeF=None

#####################################################################FONCTIONS##########################################################################

def member():
	#Fonction qui retourne les membres d'un IUT sous forme de tableau
	LdapMod=Utils.ldapp.LdapTest()
	baseDN = "ou=people,o=concours"
	searchScope = ldap.SCOPE_SUBTREE
	retrieveAttributes = ['cn']
	searchFilter = "(&(secretary="+dnIUT+")(employeeType=student))"
	ResultatM=LdapMod.Search(baseDN, searchScope, retrieveAttributes, searchFilter, True, False)
	return ResultatM

#############################################################TRAITEMENT FORMULAIRE##################################################################

if Status!="admin" or CookiesMod.VerifAdmin(SessionToken)==False: 				#Si la personne n'est pas un administrateur on la redirige
	Template.Error.Display("ACCES INTERDIT", "menu.py")

elif Status=="admin" and CookiesMod.VerifAdmin(SessionToken)==True:                            #On vérifie que la personne est bien un admin (cookie=admin et token valide)
	print'Content-type: text/html'
	print''

	print'''
	<!DOCTYPE html>
	<html>
	<head>
		<title>Concours</title>
		<meta charset="UTF-8">
		<link href="bootstrap-3.3.7/css/bootstrap.min.css" rel="stylesheet">
		<!-- JQuery CDNJS -->
		<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
		<!-- bootstrap-select CSS -->
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.12.4/css/bootstrap-select.min.css">
		<!-- bootstrap-select JavaScript -->
		<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.12.4/js/bootstrap-select.min.js"></script>
		<!-- <link rel="stylesheet" type="text/css" href="/index.css"> -->
    		<!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    		<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    		<!--[if lt IE 9]>
      			<script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      			<script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    		<![endif]-->
	</head>
	<body>'''
	Template.VerticalMenu.Display(name, teamName, Status, "administration")					#On affiche la barre de menu vertical
	if TypeF=="member":
		AllMember=member()
		Template.GestionMembres.Display(AllMember)
	
	elif TypeF=="enigme":
		sqlDB=Utils.SQLTest("concours")
                rows = sqlDB.Search("ID, Titre, Question, Reponse, Catégorie, Point, Fichier, owner","enigmes","owner='"+name+"'")	#On récupére toutes les énigmes crées par l'administrateur connecté
		Template.ShowEnigme.Display(rows)
	
	elif TypeF=="addenigme" and Status=="admin":
		sqlDB=Utils.SQLTest("concours")
                cat = sqlDB.Search("IDcat, NomCat","categorie","None")									#On récupére toutes les catégories
                point = sqlDB.Search("ID, Nom, Point","questiontype","None")								#On récupére les points de toutes les énigmes
		Template.AjoutEnigme.Display(point, cat)
	
	elif TypeF=="modifenigme" and formulaire.getvalue("id")!=None and Status=="admin":
		id=cgi.escape(formulaire.getvalue("id"))
		sqlDB=Utils.SQLTest("concours")
                enigme = sqlDB.Search("ID, Titre, Question, Reponse, Catégorie, Point, Fichier","enigmes","ID ="+id)			#On récupére tout les paramétres de l'énigme associé à l'ID
                cat = sqlDB.Search("IDcat, NomCat","categorie","None")									#On récupére toutes les catégories
                point = sqlDB.Search("ID, Nom, Point","questiontype","None")								#On récupére les points de toutes les énigmes
                Template.ModifEnigme.Display(enigme, cat, point)

	elif TypeF=="categorie" and Status=="admin":
                sqlDB=Utils.SQLTest("concours")
                Cat = sqlDB.Search("IDcat, NomCat","categorie", "None")									#On récupére toutes les catégories
                Template.GestionCat.Display(Cat)

	elif TypeF=="equipe":
		LdapMod = Utils.LdapTest()
		searchScope = ldap.SCOPE_SUBTREE
       		retrieveAttributes = ['cn']
        	searchFilter = "objectclass=groupofnames"
		equipe=LdapMod.Search(dnIUT, searchScope, retrieveAttributes, searchFilter, True, False)				#On récupére le nom de toutes les équipes d'un IUT
		Template.ShowEquipe.Display(equipe, dnIUT)

        elif TypeF=="addequipe":
		baseDN="ou=people,o=concours"
                LdapMod = Utils.LdapTest()
                searchScope = ldap.SCOPE_SUBTREE
                retrieveAttributes = ['cn']
                searchFilter = "(&(secretary="+dnIUT+")(employeeType=student))"
                members=LdapMod.Search(baseDN, searchScope, retrieveAttributes, searchFilter, True, False)				#On récupére le pseudo de tout les joueurs d'un IUT
                Template.AddEquipe.Display(members)

	elif TypeF=="modifequipe":
		dnEquipe="cn="+formulaire.getvalue('name')+","+dnIUT
                baseDN="ou=people,o=concours"
		LdapMod = Utils.LdapTest()
                searchScope = ldap.SCOPE_SUBTREE
                retrieveAttributes = ['member']
		retrieveAttributes2 = ['cn']
                searchFilter = "objectClass=groupOfNames"
		searchFilter2 = "(&(secretary="+dnIUT+")(employeeType=student))"
                DNTeamMembers=LdapMod.Search(dnEquipe, searchScope, retrieveAttributes, searchFilter, True, False)			#On récupére tout les membres d'une équipe
		TeamMembers=[]
		for i in DNTeamMembers:													#On fait une boucle sur tout les membres
			searchFilter3 = "(objectClass=inetOrgPerson)"
			TeamMembers.append(LdapMod.Search(i, searchScope, retrieveAttributes2, searchFilter3, False, False))		#On ajoute dans le tableau TeamMember, le pseudo de chaque membres(admin et joueur)
		members=LdapMod.Search(baseDN, searchScope, retrieveAttributes2, searchFilter2, True, False)				#On ajoute dans le tableau members le pseudo de tout les joueurs uniquement
		Template.ModifEquipe.Display(formulaire.getvalue('name'), TeamMembers, members)
