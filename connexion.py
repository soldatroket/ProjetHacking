#!/usr/bin/python
#-*- coding: utf-8 -*-

#Script qui permet de géré la connexion sur le site web

import Utils
import cgi
import cgitb
import ldap
import Template
import hashlib
cgitb.enable()

formulaire = cgi.FieldStorage()

def Status(id):
	#Fonction que retourne un message d'erreur suivant le code d'erreur reçu en parametre
	p=" "
	if(id==1):
		p="Veuillez completez tout les champs"
	if(id==2):
		p="Nom d'utilisateur ou mot de passe incorrect."
	Template.Error.Display(p, "/index.py")

if formulaire.getvalue('pseudo') != None and formulaire.getvalue('mdp') != None:	#Si pseudo et mot de passe différent de null
	LdapMod=Utils.ldapp.LdapTest()							#On charge la classe LdapTest pour manipuler la base ldap
	sha=hashlib.sha1()								#On charge sha1 qui nous permettra de coder le mot de passe en sha1
	user=cgi.escape(formulaire.getvalue('pseudo'))					#On sécurise les données
	mdp=cgi.escape(formulaire.getvalue('mdp'))
	sha.update(mdp)									#On charge la mot de passe dans sha
	mdp=sha.hexdigest()								#On crypte le mot de passe
	dn="cn="+cgi.escape(user)+",ou=people,o=concours"
	verification=LdapMod.Compare(dn,'userPassword',mdp)				#On compare le mot de passe reçu avec celui de l'annuaire Ldap
	if(verification==True):											#Si verification vaut True, cela veut dire que les mots de passes sont identiques
		CookiesMod=Utils.cookies()									#On charge la classe cookies qui nous permettrat d'écrire des cookies
		searchScope = ldap.SCOPE_SUBTREE
		retrieveAttributes = ['secretary']
		searchFilter = "cn="+user
		secretary=LdapMod.Search(dn, searchScope, retrieveAttributes, searchFilter, False, False)	#Je fait une recherche dans l'annuaire afin de récuperer l'iut rataché à l'utilisateur
		UserDN="cn="+user+",ou=people,o=concours"
		EquipeFilter="member="+UserDN
		equipe=LdapMod.Search("o=iut,o=concours", searchScope, ['cn'], EquipeFilter, False, False)	#On récupere le nom de l'équipe du joueur
		DNequipe=LdapMod.Search("o=iut,o=concours", searchScope, ['cn'], EquipeFilter, False, True)	#On récupere le DN de son équipe
		if(LdapMod.Compare(dn, "employeeType", "Admin")==True):						#On regarde si le joueur est un Admin
			iut=secretary.split("ou=")[1].split(",")[0]
			CookiesMod.SetCookie(user, iut, 'cn=bg,ou=M2M,o=iut,o=concours', secretary, 'admin')	#On inscrit les cookies en tant qu'admin
		else:
			CookiesMod.SetCookie(user, equipe, DNequipe, secretary, 'student')			#On inscrit les cookies en tant que joueur
	else:
		Status(2)
else:
	Status(1)
