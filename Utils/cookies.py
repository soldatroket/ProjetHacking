#!/usr/lib/python
#coding: utf-8

#Module permettant l'éritures et la lectures de cookies

import cgi
import Cookie
import random
import os
import sql

class cookies:
	def SetCookie(self, cn, memberof, DNmemberof,DNiut,status):
		#Fonction permettant d'écrire un/des cookies
		sqlDB=sql.SQLTest("concours")
		cookie=Cookie.SimpleCookie()
		SessionNumber=random.randint(1,1000000000)
		cookie['session']=SessionNumber
		cookie['session']['expires']=1*1*3*60*60
		cookie['name']=cn
		cookie['status']=status
		cookie['DNteamName']=DNmemberof
		cookie['DNiut']=DNiut
		cookie['teamName']=memberof
		if status=="admin":
			result=sqlDB.Search("Name", "AdminToken", None)
			if len(result)!=0:
				match=False
				for row in result:
					if match==False:
						if(row[0]==cn):
							match=True
				if match==True:
					Where="`Name` = '"+cn+"'"
					sqlDB.UpdateEntry("AdminToken", ("Token",) , (SessionNumber,), ("Name", cn))
				else:
					val=(cn, SessionNumber)
	                                sqlDB.AddEntry("AdminToken", "Name, Token", val)
			else:
				val=(cn, SessionNumber)
				sqlDB.AddEntry("AdminToken", "Name, Token", val)
		print cookie
		print'Content-type: text/html'
		print'Location: menu.py'
		print'\n'
	
	def ReadSession(self, cookieName):
		#Fonction qui renvoie le contenue d'un cookie
		if 'HTTP_COOKIE' in os.environ:
			c=Cookie.SimpleCookie(os.environ['HTTP_COOKIE'])
			try:
				data=c[cookieName].value
				return data
			except KeyError:
				return "None"
		else:
			return "None"
			
	def ResetSession(self):
		#Fonction qui réinitialise tout les cookies
		cookie=Cookie.SimpleCookie()
		cookie['session']=None
		cookie['name']=None
		cookie['status']=None
		cookie['DNteamName']=None
		cookie['DNiut']=None
		cookie['teamName']=None
		return cookie

	def VerifAdmin(self, token):
		#Fonction qui retourne True/False en fonction de la validiter du token
		sqlDB=sql.SQLTest("concours")
		verifAccess=sqlDB.Search("Token","AdminToken", "Token = "+token)
		if len(verifAccess)==1:
			return True
		else:
			return False
