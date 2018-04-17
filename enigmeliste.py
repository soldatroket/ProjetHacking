#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Script qui permet d'afficher la liste des énigmes

import cgi
import Utils
import cgitb
import ldap
import Template
import mysql.connector
cgitb.enable()

###################################Récupération des cookies#######################################

CookiesMod=Utils.cookies()
name=CookiesMod.ReadSession('name')
teamName=CookiesMod.ReadSession('teamName')
dnIUT=CookiesMod.ReadSession('DNiut')
Status=CookiesMod.ReadSession('status')
DNteam=CookiesMod.ReadSession('DNteamName')

sqlDB=Utils.SQLTest("concours")
enigmes=sqlDB.Search("ID, Titre, Question, Reponse, Catégorie, Point, Fichier","enigmes","None")		#On récupére toute les énigmes sur la base SQL
categorie=sqlDB.Search("IDcat, NomCat","categorie","None")							#On récupére toute les catégories sur la base SQL
sqlDB.SetDB("equipes")
reponse=sqlDB.Search("IDQuestion", teamName, "None")								#On récupére l'ID de toutes les énigmes dont l'équipe à répondu

#########################################PAGE HEADER#############################################

print'Content-type: text/html'
print''
print '''<html>
	<head>
		<meta http-equiv="content-type" content="text/html; charset=UTF-8">
		<title>Liste des énigmes</title>
		<link href="bootstrap-3.3.7/css/bootstrap.min.css" rel="stylesheet">
                <!-- <link rel="stylesheet" type="text/css" href="/index.css"> -->
                <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
                <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
                <!--[if lt IE 9]>
                        <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
                        <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
                <![endif]-->

	</head>
	<body>'''

#############################################PAGE BODY#############################################

Template.VerticalMenu.Display(name, teamName, Status, "enigmes")					#On affiche la barre vertical
print '''<div class="col-lg-10">
		<div class="row">
			<div class="col-lg-12 col-lg-offset-2">
				<table class="table table-bordered table-striped table-condensed text-center">'''
for i in categorie:											#On fait une boucle sur toutes les catégories
	print '''		<tr>
					<td colspan="2">
						<h1>'''+i[1]+'''</h1>
					</td>
				</tr>'''
	for y in enigmes:										#On réalise une boucle qui affiche les énigmes de la catégorie dans laquelle l'ont ce trouve
		if y[4]==i[1]:										#Condition qui permet de vérifier si l'énigme fait partit de la catégorie
			print '''<tr>
					<td>
						<h4>'''
			present=False
			if reponse!=None:								#Condition qui vérifie si l'ont à repondue à l'énigme
				print '''<div class="row">
						<div class="col-lg-4 col-lg-offset-2 text-left">'''
				for rep in reponse:
					if rep[0]==y[0]:
						present=True
				if present==True:							#Affiche un symabole validé à coter de l'énigme si l'ont y à repondue
					print		'<span class="glyphicon glyphicon-ok" aria-hidden="true"></span>'
				else:
					print           '<span class="glyphicon glyphicon-remove" aria-hidden="true"></span>'
			else:
				print '<span class="glyphicon glyphicon-remove" aria-hidden="true"></span>'
			print '''<a href=enigme.py?ID='''+str(y[0])+'''>'''+y[1]+'''</a>
						</div>
					</div>
						</h4>
					</td>
					<td>
						<h4> '''+str(y[5])+''' points </h4>
					</td>
				</tr>'''
print '''			</table>
			</div>
		</div>
	</div>
</div>
</body>
</html>
'''
