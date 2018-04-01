#!/usr/bin/env python
#-*- coding: utf-8 -*-
import cgi
import cgitb
import Utils
cgitb.enable()
form=cgi.FieldStorage()

CookiesMod=Utils.cookies()

if CookiesMod.ReadSession("session")!="None":
	print'Content-type: text/html'
	print'Location:menu.py'
	print ''
else:
	if form.getvalue('mail'):
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
	<script>
	function validateForm(){
		var pseudo= document.getElementById('pseudo');
		var mdp= document.getElementById('mdp');
		if (pseudo.value == "" || mdp.value == "") {
			alert("Vous devez remplir tous les champs");
        return false;
		}else{
			return true;
			}
		}
	</script>
	<h1 class="Titre">CONNEXION</h1>
	<div class="BoxPos">
	<div class="BoxStyle">'''
	if form.getvalue('type')==None:
		print '''<span style="vertical-align: -webkit-baseline-middle;">Identification<span>
		<hr>
		<form nom="FormulaireID" onsubmit="return validateForm()" action="connexion.py" method="post">
			<input type="text" placeholder="Identifiant" name="pseudo">
			<br>
			<input type="password" placeholder="Mot de passe" name="mdp">
			<br>
			<br>
			<input type="submit" value="connexion">
		</form>
		<a href="index.py?type=resetmdp" style="font-size:15px;">Mot de passe oublié?</a>
	</div>
	</div>
</body>
</html>
	'''
	elif form.getvalue('type')!=None and form.getvalue('type')=="resetmdp":
        	print '''<span style="vertical-align: -webkit-baseline-middle;">Identification<span>
                <hr>
                <form nom="FormulaireID" action="index.py" method="post">
			<p style="font-size:15px;">Entrez votre mail pour que l'ont puissent vous renvoyer un mot de passe</p></br>
                        <input type="text" placeholder="Votre Mail" name="mail">
                        <br>
                        <br>
                        <input type="submit" value="Envoyer">
                </form>
        </div>
        </div>
</body>
</html>
        '''
