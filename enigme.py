#!/usr/bin/env python
#coding: utf-8

#Fichier qui permet d'afficher la page web d une énigme

import cgi
import Utils
import cgitb
import ldap
import Template
import mysql.connector
cgitb.enable()

formulaire = cgi.FieldStorage()

###########################################RECUPERATION DES ENIGMES##########################################################

CookiesMod=Utils.cookies()
SessionToken=CookiesMod.ReadSession("session")
name=CookiesMod.ReadSession('name')
teamName=CookiesMod.ReadSession('teamName')
dnIUT=CookiesMod.ReadSession('DNiut')
Status=CookiesMod.ReadSession('status')
DNteam=CookiesMod.ReadSession('DNteamName')

def Display():
	if formulaire.getvalue("ID")!=None:						#On vérifie que l'ont à bien reçu l'ID de l'énigme à afficher
		id=cgi.escape(formulaire.getvalue("ID"))
		sqlDB=Utils.SQLTest("concours")
		rows = sqlDB.Search("ID, Titre, Question, Reponse, Catégorie, Point, Fichier","enigmes","ID="+id)		#On récupére toutes les infos de l'énigme

		print'Content-type: text/html'
		print''

		print'''<!DOCTYPE html>
        	<html>
        	<head>
        	        <title>Enigme n°'''+id+'''</title>
        	        <meta charset="UTF-8">
			<link href="bootstrap-3.3.7/css/bootstrap.min.css" rel="stylesheet">
        		<!-- <link rel="stylesheet" type="text/css" href="/index.css"> -->
        		<!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        		<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        		<!--[if lt IE 9]>
        			<script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
        			<script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
        		<![endif]-->
        	<head>
        	<body>'''
		if len(rows)!=0:																	#On vérifie que l'on à bien récuperé des informations
			Template.VerticalMenu.Display(name, teamName, Status, "enigme")					#On affiche le menu vertical
			print '''<div class="col-lg-10 text-center">
					<div class="row">
						<form method="post" action="verifenigme.py" class="col-lg-12">
							<Legend>Enigme n° '''+str(rows[0][0])+'''</Legend>
							<div class="form-group">
								<Label>Question : '''+str(rows[0][2])+'''</Label>
								<textarea placeholder="Votre Reponse" name="reponse" class="form-control"></textarea>
        	                                       	</div>
							<div class="form-group">
								<input type="hidden" value="'''+str(rows[0][0])+'''" name="ID">
								<input type="submit" value="Verifiez">
        	                               		</div>'''
			if str(rows[0][6])!="None":									#On regarde si on à un fichier avec l'énigme
				print	'''		<div class="form-group">
								<a href="/enigmes/'''+str(rows[0][0])+"/"+str(rows[0][6])+'''" download>
									<button type="button" class="btn btn-primary">
										Fichier complémentaire<span class="badge badge-primary">1</span>
									</button>
								</a>
							</div>'''
			else:
				print '''	</form>
					</div>
        	         	</div>
			</div>'''
		else:
			Template.Error.Display("ERREUR : ENIGME NON TROUVE", "enigmeliste.py")
	else:
		Template.Error.Display("AUCUNE ENIGME SELECTIONNE", "enigmeliste.py")

Display()
