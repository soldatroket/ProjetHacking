#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Script permettant de faire un reset du mot de passe d'un utilisateur

import cgi
import cgitb
import Utils
import hashlib
import ldap
import Template
cgitb.enable()

form=cgi.FieldStorage()

if form.getvalue('token')!=None:
	#On verifie que l'ont à bien reçu un token qui permet de vérifier la validité
        print'Content-type: text/html'
        print''
	sqlDB=Utils.sql.SQLTest("concours")
	verifToken=sqlDB.Search("token", "resetmdp", "token = '"+form.getvalue('token')+"'")	#On récupére/vérifie que le token recu est bien valide en le comparant à la base SQL
	if len(verifToken)==1:									#Si la longeur de verifToken vaut 1, alors le token est valide
		print """<!DOCTYPE html>
			<html>
				<head>
                			<title>Concours</title>
                			<meta charset="UTF-8">
                			<link href="bootstrap-3.3.7/css/bootstrap.min.css" rel="stylesheet">
                			<!-- <link rel="stylesheet" type="text/css" href="/index.css"> -->
                			<!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
                			<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
                			<!--[if lt IE 9]>
                        			<script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
                        			<script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
                			<![endif]-->
        			</head>
				<body>
					<div class="container-fluid">
						<div class="row">
							<form method=post action="resetpassword.py" class="col-lg-12">
								<input type="hidden" name="tkn" value="""+form.getvalue('token')+""">
								<div class="form-group">
									<Label>Nouveau mot de passe</Label>
									<input type="password" name="pass01" class="form-control" required>
								</div>
								<input type="submit">
							</form>
						</div>
					</div>
					</body>
			</html>
		"""
	else:
		Template.Error.Display("Accés refusé","index.py")

if form.getvalue('tkn')!=None and form.getvalue('pass01')!=None:
	#On vérifie que l'ont a bien recu le nouveau mot de passe 
	sha=hashlib.sha1()
	sha.update(form.getvalue('pass01'))						#On crypte le nouveau mot de passe en sha1
	passw=sha.hexdigest()
	LdapMod=Utils.ldapp.LdapTest()
	sqlDB=Utils.sql.SQLTest("concours")						#On se place dans la base concours
	mail=sqlDB.Search("mail", "resetmdp", "token = '"+form.getvalue('tkn')+"'") 	#On récupére le mail de l'utilisateur sur la base SQL en fonction du token reçu
	baseDN = "ou=people,o=concours"
	searchScope = ldap.SCOPE_SUBTREE
	retrieveAttributes = ['cn']
	searchFilter = "mail="+mail[0][0]
	cn=LdapMod.Search(baseDN, searchScope, retrieveAttributes, searchFilter, False, False)	#On récupére le pseudo du joueur liée à l'email
	LdapMod.Modify(cn, "userPassword", passw)					#On modifie le mot de passe de l'utilisateur
	sqlDB.DelEntry("resetmdp", "mail", mail[0][0])					#On supprime le token de la base SQL une fois l'opération réaliser
	Template.Error.Display("Votre mot de passe à bien était changé","index.py")
