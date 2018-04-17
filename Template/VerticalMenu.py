#!/usr/lib/python
#-*- coding: utf-8 -*-

import Utils
import ldap

def GetScore(Status, team):
	#Fonction qui permet de récuperé le score d'une équipe
	if Status=="student":
        	if team!="Pas de resultat":
			CookiesMod = Utils.cookies()
			baseDN = CookiesMod.ReadSession('DNteamName')
                	searchScope = ldap.SCOPE_SUBTREE
                	retrieveAttributes = ['description']
                	searchFilter = "objectClass=groupOfNames"
                	LdapMod=Utils.ldapp.LdapTest()
                	score=LdapMod.Search(baseDN, searchScope, retrieveAttributes, searchFilter, False, False)
        		return score
		else:
                	team="Aucune equipe"
                	return 0
	else:
        	return 0


#Fonction qui permet d'afficher le menu vertical

def Display(name, team, Status, pagename):
	score=GetScore(Status, team)
	print'''
	<div class="container" style="margin:0px;padding:0px;">
		<div class="row" >
			<div class="col-lg-2"  style="background-color:lightgrey;height:100%;">
				<div class="row">
					<div class="col-lg-10 col-lg-offset-1">				
						<ul class="list-unstyled">'''
	print 					"<li>Bonjour "+name+"</li>"
	if Status=="student":
		print 				"<li>Equipe : "+team+"</li>"
		print				"<li>Points : "+str(score)+"</li>"
	else:
		print 				"<li>IUT : "+team+"</li>"
	print '''
						</ul>
					</div>
				</div>
				<div class="row">
					<div class="col-lg-10 col-lg-offset-1">
						<hr>
					</div>
				</div>	
				<div class="row">
					<nav class="col-lg-10 col-lg-offset-1">	
						<h5>MENU</h5>
						<ul class="nav flex-column">
							<li class="nav-item"><a class="nav-link" href="menu.py"><span class="glyphicon glyphicon-home"></span> Accueil</a></li>
							<li class="nav-item"><a class="nav-link" href="enigmeliste.py"><span class="glyphicon glyphicon-list-alt"></span> Enigmes</a></li>
							<li class="nav-item"><a class="nav-link" href="result.py"><span class="glyphicon glyphicon-stats"></span> Résultat</a></li>'''
	if Status=="admin":
		print 					'<li class="nav-item"><a class="nav-link" href="administration.py"><span class="glyphicon glyphicon-cog"></span> Admistration</a></li>'
	print '''
							<li class="nav-item"><a class="nav-link" href="deconnexion.py"><span class="glyphicon glyphicon-log-out"></span> Déconnexion</a></li>
						</ul>
					</nav>
				</div>
				<div class="col-lg-10 col-lg-offset-1">
					<hr>
				</div>'''
	if Status=="admin" and pagename=="administration":
		print '''<div class="row">
				<nav class="col-lg-10 col-lg-offset-1">
					<h5>Administration</h5>
					<ul class="nav flex-column">
						<li class="nav-item"><a href="administration.py?type=member">Gestion des membres</a></li>
						<li class="nav-item"><a href="administration.py?type=enigme">Gestion des énigmes</a></li>
						<li class="nav-item"><a href="administration.py?type=equipe">Gestion des équipes</a></li>
					</ul>
				</nav>
			</div>'''
	print '''
	</div>'''
