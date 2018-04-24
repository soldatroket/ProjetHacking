#!/usr/bin/env python
#coding: utf8

#Script qui centralise toutes les opérations réaliser sur la base de donnée

import cgi
import os
import cgitb
import Utils
import hashlib
import Template
cgitb.enable()

###########################################################RECUPERATION COOKIES############################################################################

CookiesMod=Utils.cookies()
SessionToken=CookiesMod.ReadSession("session")
name=CookiesMod.ReadSession('name')
teamName=CookiesMod.ReadSession('teamName')
dnIUT=CookiesMod.ReadSession('DNiut')

formulaire=cgi.FieldStorage()

######################################################TRAITEMENT FORMULAIRE#######################################################################################

if formulaire.getvalue("type")!=None:						#On vérifie que l'on à bien reçu des infomrations
	#Si l'on n'a detecté un argument dans type on va regarder à quoi il correspond
	sqlDB=Utils.SQLTest("concours")

	if formulaire.getvalue("type")=="delenigme" and formulaire.getvalue("id")!=None: 	#Si le type vaut delenigme et que l'on à reçu un id correspondant à l'énigme à supprimer
		#Partie qui concerne la suppression d'énigme.
		#On à vérifié qu'il existait une valeur pour id, qui correspond au numéro de l'énigme.
		ID=cgi.escape(formulaire.getvalue('id'))			#On récupére et sécurise la valuer de id
		sqlDB.DelEntry("enigmes", "ID", ID)				#On supprime l'entrée de la base sql où le numéro d'énigme correspond à l'id
		os.chdir("/var/www/UnityScript/concours")			#On se place dans le répertoire de la ou sont enregistrées chaques énigmes afn de se préparer à supprimer la répertoire de l'énigme s'il existe
		if os.path.exists("enigmes/"+ID+"/"):				#On vérifie qu'il existe un dossier pour cette énigme, si oui on vas le supprimer
			path="enigmes/"+ID+"/"
			contenu=os.listdir(path)
			for i in contenu:					#On réalise une boucle pour supprimer tout les éléments à l'intérieur du dossier
				os.remove(path+i)				
			os.rmdir(path)						#Une fois le dossier vide on le supprime
		Template.Error.Display("Votre énigme à bien était supprimée", "administration.py?type=enigme")

	elif formulaire.getvalue("type")=="addenigme":						#Si le type  vaut addenigme
		#Partie concernant l'ajout d'une énigme.
		sha=hashlib.sha1()						#On invoque un objet hashlib avec le cryptage sha1, pour crypter la réponse de l'énigme
		fileitem=formulaire['file']					#On récupére et sécurise toutes les informations de l'énigme grâce au formulaire
                difficulter=cgi.escape(formulaire.getvalue("strenght"))
                titre=cgi.escape(formulaire.getvalue("title"))
                question=cgi.escape(formulaire.getvalue("answer"))
                reponse=cgi.escape(formulaire.getvalue("reponse"))
                sha.update(reponse)						#On charge la réponse dans notre objet hashlib puis on le crypt
                reponse=sha.hexdigest()
                categorie=cgi.escape(formulaire.getvalue("cat"))
                attr="Titre, Question, Reponse, Catégorie, Point, owner"	#On créer notre requête sql
		sqlDB.AddEntry("enigmes", attr, (titre, question, reponse, categorie, difficulter, name))	#On utilise SQLTest afin d'ajouter notre énigme dans la table énigmes
		sqlDB.SetDB("concours")
                ID=sqlDB.Search("`ID`, `Titre`", "`enigmes`", "`Titre`='"+str(titre)+"'")
		if fileitem.filename:						#On regarde si un fichier à était envoyé avec l'énigme
			os.chdir("/var/www/UnityScript/concours")
                        os.mkdir("enigmes/"+str(ID[0][0])+"/")			#On crée un dossier qui porte comme nom l'id de l'énigme en question
                        fn=os.path.basename(fileitem.filename)			#On récupére le nom du fichier envoyé
                        open('enigmes/'+str(ID[0][0])+'/'+fn, 'wb').write(fileitem.file.read())	#On enregistre notre fichier dans le dossier que l'on viens de créer avec son nom de base
			sqlDB.UpdateEntry("enigmes", ("Fichier",), (fn,), ("ID", ID[0][0]))	#On met à jour la table SQL de notre énigme en y ajoutant le nom du fichier
		Template.Error.Display("Votre enigme à bien était ajouté", "administration.py?type=enigme")

        elif formulaire.getvalue("type")=="modifenigme":			#Si le type vaut modifenigme
		#Partie concernant la modification d'une énigme
		fileitem=formulaire['file']									#On récupére et sécurise toute les informations de l'énigme recu par le formulaire
		id=cgi.escape(formulaire.getvalue("ID"))
		difficulter=cgi.escape(formulaire.getvalue("strenght"))
                titre=cgi.escape(formulaire.getvalue("title"))
                question=cgi.escape(formulaire.getvalue("answer"))
		categorie=cgi.escape(formulaire.getvalue("cat"))
		if fileitem.filename:										#On vérifie qu'un fichier à était envoyé
			os.chdir("/var/www/UnityScript/concours")				#On se place dans le répertoire ou son enregistrées les énigmes
                        if os.path.exists("enigmes/"+id+"/")==False:		#On vérifie que le dossier de l'énigme existe, sinon on le crée.
				os.mkdir("enigmes/"+id+"/")
                        else:
				for i in os.listdir("enigmes/"+id+"/"):		#On supprime tout ce qu'il y à dans le dossier de l'énigme pour le remplacer avec le nouveau fichier
					os.remove("enigmes/"+id+"/"+i)
			fn=os.path.basename(fileitem.filename)
                        open('enigmes/'+id+'/'+fn, 'wb').write(fileitem.file.read())	#On enregistre le nouveau fichier dans le répertoire de l'énigme
			sqlDB.UpdateEntry("enigmes", ("Fichier",), (fn,), ("ID", id))				#On met à jour la table SQL de notre énigme en y mettant le nom du fichier
		if "reponse" not in formulaire:													#On regarde si l'ont à reçu une nouvelle réponse d'énigme, si oui on va alors la crypter et la remplacer dans la base SQL
			sha=hashlib.sha1()
                	reponse=cgi.escape(formulaire.getvalue("reponse"))
                	sha.update(reponse)
                	reponse=sha.hexdigest()
                	sqlDB.UpdateEntry("enigmes", ("Titre", "Question", "Reponse", "Catégorie", "Point"), (titre, question, reponse, categorie, difficulter), ("ID", id))
                else:
			sqlDB.UpdateEntry("enigmes", ("Titre", "Question", "Catégorie", "Point"), (titre, question, categorie, difficulter), ("ID", id))
		Template.Error.Display("Votre énigme à bien était mise à jour", "administration.py?type=enigme")

	elif formulaire.getvalue("type")=="addmember":									#Si notre type vaut addmember
		#Partie concernant l'ajout d'un membre
		try:
			LdapMod=Utils.ldapp.LdapTest()											#On invoque LdapTest qui nous servirat à manipulé l'annuaire Ldap
        		sha=hashlib.sha1()
			cn=cgi.escape(formulaire.getvalue("prenom"))							#On récupére toutes les informations du membres transmise par formulaire
        		sn=cn+" "+cgi.escape(formulaire.getvalue("nom"))
			mail=cgi.escape(formulaire.getvalue("mail"))
			employe=cgi.escape(formulaire.getvalue("employeType"))
        		mdp=Utils.password.Pass().GeneratePass(mail)						#On génére un mot de passe puis on l'envoie à l'adresse mail de l'utiliateur(mot de passe qui servirat à l'utilisateur pour d'enregistrer son propre mot de passe
			sha.update(mdp)
			mdp=sha.hexdigest()
			LdapMod.AddMember(cn,sn,mail,dnIUT,employe, mdp)
			Template.Error.Display("Le membre à bien était ajouté", "administration.py?type=member")
		except:
			Template.Error.Display("Une erreur est survenue", "administration.py?type=member")

	elif formulaire.getvalue("type")=="delmember":									#Si notre type vaut delmember
        	#Partie concernant la suppression de membre
		LdapMod=Utils.ldapp.LdapTest()
		prenom=cgi.escape(formulaire.getvalue("user"))								#On récupére le pseudo du membre à supprimer
        	dn="cn="+prenom+",ou=people,o=concours"									#On reconstitue le DN du membre
        	LdapMod.DelMember(dn)													#On supprime le membre grâce à son DN
		Template.Error.Display("Le membre à bien était supprimé", "administration.py?type=member")

	elif formulaire.getvalue("type")=="addequipe":									#Si notre type vaut addequipe
		#Partie concernant l'ajout d'un équipe
		LdapMod=Utils.ldapp.LdapTest()
		sqlDB.SetDB("equipes")														#On se place dans la base equipes
		members=formulaire.getvalue("members")
		teamName=cgi.escape(formulaire.getvalue("teamname"))
		memberList=[]
		if type(members) is list:
			for m in members:														#On ajoute l'ensemble des membres de l'équipe dans un tableau
				memberList.append(m)
		else:
			memberList.append(members)
		LdapMod.AddGroup(teamName, memberList, dnIUT, name)							#On ajoute le groupe dans le LDAP grâce à notre fonction AddGroup
		sqlDB.CreateTeamTable(teamName)												#On crée un etable liée à notre équipe dans notre base SQL grâce à notre fonction CreateTeamTable
		Template.Error.Display("Votre équipe à bien était ajoutée", "administration.py?type=equipe")

	elif formulaire.getvalue("type")=="modifequipe":								#Si type vaut modif equipe
		#Partie concernant la modification d'une équipe
		LdapMod=Utils.ldapp.LdapTest()
		sqlDB.SetDB("equipes")
		members=formulaire.getvalue("members")
		teamName=cgi.escape(formulaire.getvalue("teamname"))
		newteamname=cgi.escape(formulaire.getvalue("newteamname"))
		memberList=[]
		if type(members) is list:
			for m in members:
				memberList.append("cn="+m+",ou=people,o=concours")					#On ajoute l'ensemble des membres de l'équipe dans un tableau
		else:
			memberList.append("cn="+members+",ou=people,o=concours")
		LdapMod.ModifyGroup(dnIUT,teamName, newteamname, memberList)				#On met à jour notre équipe grâce à notre focntion ModifyGroup
		sqlDB.RenameTable(teamName, newteamname)									#On renomme la table SQL de notre équipe avec le nouveau nom d'équipe
		Template.Error.Display("Votre équipe à bien était modifié", "administration.py?type=equipe")

	elif formulaire.getvalue("type")=="delequipe":									#Si type vaut delequipe
		#Partie concernant la suppression d'une équipe
		LdapMod=Utils.ldapp.LdapTest()
		sqlDB.SetDB("equipes")
		teamName=cgi.escape(formulaire.getvalue("teamname"))						#On récupére et sécurise le nom d'équipe
		sqlDB.DeleteTable(teamName)													#On supprime sa table SQL
		LdapMod.DelMember("cn="+str(teamName)+","+dnIUT)							#On supprime l'équipe grâce à notre fonction DelMember
		Template.Error.Display("Equipe supprimer", "administration.py?type=equipe")

	elif formulaire.getvalue("type")=="addcat":										#Si type vaut addcat
		#Partie concernant l'ajout d'une catégorie
		sqlDB.SetDB("concours")														#On se place dans la table concours
		catname=cgi.escape(formulaire.getvalue("catname"))							#On réupére et sécurise notre catégorie
		sqlDB.AddEntry("categorie", "NomCat", (catname,))							#On ajoute notre catégorie dans la base sql grâce à la fonction AddEntry
		Template.Error.Display("Votre catégorie à bien était ajouté.", "administration.py?type=categorie")

	elif formulaire.getvalue("type")=="delcat":										#Si type vaut delcat
		#Partie concernant la suppression de catégorie
		sqlDB.SetDB("concours")
		id=cgi.escape(formulaire.getvalue("id"))									#On récupére et sécurise l'id de notre catégorie
		sqlDB.DelEntry("categorie","IDcat",id)										#On supprime notre catégorie grâce à son ID et la fonction DelEntry
		Template.Error.Display("Votre catégorie à bien était supprimée", "administration.py?type=categorie")
