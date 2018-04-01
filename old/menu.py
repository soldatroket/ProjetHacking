#!/usr/bin/env python
#coding: utf-8
import cgi
import Utils
import cgitb
import ldap
import Template
cgitb.enable()

CookiesMod=Utils.cookies()
name=CookiesMod.ReadSession('name')
team=CookiesMod.ReadSession('teamName')
DNteam=CookiesMod.ReadSession('DNteamName')
Status=CookiesMod.ReadSession('status')

if Status=="student": 
	baseDN = DNteam
	searchScope = ldap.SCOPE_SUBTREE
	retrieveAttributes = ['description']
	searchFilter = "objectClass=groupOfNames"
	LdapMod=Utils.ldapp.LdapTest()
	score=LdapMod.Search(baseDN, searchScope, retrieveAttributes, searchFilter, False, False)
else:
	score=0

print'Content-type: text/html'
print''

print'''
<!DOCTYPE html>
<html>
<head>
	<title>Concours</title>
	<meta charset="UTF-8">
	<link rel="stylesheet" type="text/css" href="/menu.css">
	<head>
<body>'''
Template.VerticalMenu.Display(name, team, score, Status, "menu")
print '''
</body>
</html>'''
