#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Fichier qui permet d'afficher la page de connexion du site web. Mais aussi la page du mot de passe oublié

import cgi
import cgitb
import Utils
cgitb.enable()
form=cgi.FieldStorage()

CookiesMod=Utils.cookies()

if CookiesMod.ReadSession("session")!="None":			#On regarde si l'on à deja des cookies enregistrés, si oui on va rediriger l'utilisateur vers le menu
	print'Content-type: text/html'
	print'Location:menu.py'
	print ''
else:
	if form.getvalue('mail'):				#On regarde si l'on à recu un attribut mail (utilisé pour le reset de mot de passe)
        	Utils.password.Pass().GeneratePass(form.getvalue('mail'))

	print'Content-type: text/html'
	print''
	print '''<!DOCTYPE html>
<html>
<head>
	<title>ConcoursPython</title>
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
	<div class="container">
		<header class="row">
			<section class="col-lg-12" style="line-height: 150px;text-align:center;">CONNEXION</section>
		</header>
		<section class="row">
			<div class="col-lg-6 col-lg-offset-3">'''
	if form.getvalue('type')==None:
		#Partie page de connexion
		print '''<div class="col-lg-8 col-lg-offset-2">		
				<form nom="FormulaireID" action="connexion.py" method="post" class="col-lg-10 col-lg-offset-1">
					<Legend>Identification</Legend>
					<div class="form-group">
						<label for="ID">Identifiant : </label>
						<input id="ID" type="text" placeholder="Identifiant" name="pseudo" class="form-control" required>
					</div>
					<div class="form-group">
						<label for="MDP">Mot de passe : </label>
						<input id=""MDP type="password" placeholder="Mot de passe" name="mdp" class="form-control" required>
					</div>
					<div class="form-group">
						<input type="submit" value="connexion"  class="form-control">
					</div>	
				</form>
				<div class="col-lg-10 col-lg-offset-1">
					<a href="index.py?type=resetmdp" style="font-size:15px;">Mot de passe oublié?</a>
				</div>
			</div>
		<div class="row">
			<div class="col-lg-6 col-lg-offset-3 text-center">
				<a href="result.py" style="font-size: 20px;"><span class="label label-success">Voir résultat</span></a>
			</div>
		</div>
	'''
	elif form.getvalue('type')!=None and form.getvalue('type')=="resetmdp":
        	#Partie Mot de passe oublié
		print '''<div class="col-lg-8 col-lg-offset-2">	
                		<form nom="FormulaireID" action="index.py" method="post" class="col-lg-10 col-lg-offset-1">
					<Legend>Mot de passe oublier</Legend>
					<div class="form-group">
						<label for="mail">Email : </label>
						<div class="input-group">
                        				<input type="email" placeholder="Votre Mail" name="mail" id="mail" class="form-control" required>
							 <span class="input-group-addon">@</span> 
						</div>
					</div>
					<div class="form-group">                     
						<input type="submit" value="Envoyer">
					</div>               
				</form>
        		</div>'''
	print '''</div>
		</section>
	</div>
</body>
</html>'''
