#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Script qui déconnecte un utilisateur (reset cookie + redirection)

import Utils

CookiesMod=Utils.cookies()
name=CookiesMod.ReadSession("name")
status=CookiesMod.ReadSession("status")

if status=="admin":								#On regarde si l'utilisateur est un admin
	sqlDB=Utils.SQLTest("concours")
	sqlDB.DelEntry("AdminToken", "Name", name)				#On supprime le token attribué à l'admin dans la base SQL

c=CookiesMod.ResetSession()							#On appelle la fonction ResetSession qui nous permet de réinitialiser tout les cookies

print c
print'Content-type: text/html'
print'Location: index.py'
print''
