#!/usr/bin/env python
#coding: utf-8

#Script permettant d'afficher le menu princial lors de la connexion d'un utilisateur

import cgi
import Utils
import cgitb
import ldap
import Template
cgitb.enable()

#######################################REUPERATION DES COOKIES####################################################

CookiesMod=Utils.cookies()
name=CookiesMod.ReadSession('name')
team=CookiesMod.ReadSession('teamName')
DNteam=CookiesMod.ReadSession('DNteamName')
Status=CookiesMod.ReadSession('status')

############################################FONCTION#################################################################

def Display():
	print'Content-type: text/html'
	print''

	print'''
	<!DOCTYPE html>
	<html>
	<head>
        	<link href="bootstrap-3.3.7/css/bootstrap.min.css" rel="stylesheet">
        	<title>Menu</title>
		<meta http-equiv="content-type" content="text/html; charset=UTF-8" />
        	<!-- <link rel="stylesheet" type="text/css" href="/index.css"> -->
        	<!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        	<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        	<!--[if lt IE 9]>
        	<script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
        	<script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
        	<![endif]-->
        <head>
	<body>'''
	Template.VerticalMenu.Display(name, team, Status, "menu")
	print '''
	</body>
	</html>'''

##########################################TRAITEMENT##################################################################

Display()
