#!/usr/bin/env python
#coding: utf8

#Script qui va permettre d'afficher les résultats en récuperant les différentes valeurs
import cgi
import Utils
import cgitb
import ldap
import Template
import mysql.connector
cgitb.enable()

######################################################RECUPERATION DES COOKIES###########################################################################

CookiesMod=Utils.cookies()
SessionToken=CookiesMod.ReadSession("session")
name=CookiesMod.ReadSession('name')
teamName=CookiesMod.ReadSession('teamName')
dnIUT=CookiesMod.ReadSession('DNiut')
Status=CookiesMod.ReadSession('status')
DNteam=CookiesMod.ReadSession('DNteamName')

LdapMod=Utils.LdapTest()
formulaire=cgi.FieldStorage()

###########################################################FONCTIONS####################################################################################

def GetListeIut():
	#Fonction qui retourne un tableau remplit de sous tableaux qui contiennent le nom et le score de chaque IUT sous la forme : [nom, score]
	Donnees=[]
	baseDN = "o=iut,o=concours"
	searchScope = ldap.SCOPE_ONELEVEL
	retrieveAttributes = ['ou']
	searchFilter = "objectClass=organizationalUnit"
	ListeIUT=LdapMod.Search(baseDN, searchScope, retrieveAttributes, searchFilter, True, False)
	for i in ListeIUT:
		dnIUT="ou="+i+",o=iut,o=concours"
		LocalScore=LdapMod.GetScoreIUT(dnIUT)
		Donnees.append([i,LocalScore])
	return Donnees


def GetListeEquipe():
	#Fonction qui retourne un tableau remplit de sous tableaux qui contiennent le nom et le score de chaque equipe sous la forme : [nom, score] 
	Donnees=[]
	baseDN = "o=iut,o=concours"
	searchScope = ldap.SCOPE_SUBTREE
	retrieveAttributes = ['cn', 'description']
	searchFilter = "objectClass=groupOfNames"
        ListeEquipe=LdapMod.Search(baseDN, searchScope, retrieveAttributes, searchFilter, True, False)
        for i in ListeEquipe:
                Donnees.append([i[0],i[1]])
	return Donnees

def Display(title, label, list, graph):
	#Fonction qui affiche les résultats
        print'Content-type: text/html'
        print''

        print'''
                <!DOCTYPE html>
                <html>
                <head>
                        <title>Concours</title>
                        <meta charset="UTF-8">
                        <!--<meta http-equiv="refresh" content="1"> -->
                        <link rel="stylesheet" type="text/css" href="menu.css">
                        <link href="bootstrap-3.3.7/css/bootstrap.min.css" rel="stylesheet">
                        <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
                        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
                        <!--[if lt IE 9]>
                                <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
                                <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
                        <![endif]-->
                <head>
        <body>'''
        Template.VerticalMenuChart.Display(name, teamName, "0", Status, "resultat")
        Template.Chart.Display(title, label, list, graph)
        print'''
        </div>
        </body>
        </html>'''

###########################################################TRAITEMENT FORMULAIRE########################################################################################

if formulaire.getvalue("donnees"):						#On verifie que l'ont à bien reçu des données
	choix=cgi.escape(formulaire.getvalue("donnees"))
	if choix=="iut":
		Liste=GetListeIut()
		Titre="Score par IUT"
		Label="IUT"
	if choix=="equipe":
		Liste=GetListeEquipe()
		Titre="Score par EQUIPES"
		Label="EQUIPE"
	if formulaire.getvalue("graphique"):
                graph=formulaire.getvalue("graphique")
        else:
                graph="bar"
	Display(Titre, Label, Liste, graph)
else:										#Sinon on affiche les valeurs par défaut
	Liste=GetListeIut()
	Label="IUT"
	Titre="Score par IUT"
	if formulaire.getvalue("graphique"):
        	graph=formulaire.getvalue("graphique")
	else:
        	graph="bar"
	Display(Titre, Label, Liste, graph)
