#!/usr/bin/env python
#-*- coding: utf-8 -*-
import mysql.connector
import cgi
import cgitb
cgitb.enable()

class SQLTest:
	B2D = ""

	def __init__(self, db):
		self.B2D=db

	def SetDB(self, db):
		self.B2D=db

	def Connection(self):
		conn = mysql.connector.connect(host="localhost",user="root",password="lolotte", database=self.B2D)
		return conn

	def Search(self, Select, From, Where):
		conn = self.Connection()
		cursor = conn.cursor()
		if(Where=="None" or Where==None):
			query = "SELECT "+Select+" FROM "+From+""
		else:
			query = "SELECT "+Select+" FROM "+From+" WHERE "+Where+""
		try:
			cursor.execute(query)
			rows = cursor.fetchall()
			conn.commit()
			return rows
		except mysql.connector.Error as err:
			#print err
			conn.commit()

	def AddEntry(self, table, attr, value):
		conn = self.Connection()
		cursor = conn.cursor()
		val=""
		for i in range(len(value)):
			if i==0:
				val+="%s"
			else:
				val+=",%s"
		query = ("INSERT INTO "+table+" ("+attr+") " "VALUES ("+val+")")
		try:
			cursor.execute(query, value)
			conn.commit()
		except mysql.connector.Error as err:
		        print'Content-type: text/html'
        		print''
			print "Erreur AddEntry : "
			print err

	def UpdateEntry(self, table, attr, value, where):
		conn = self.Connection()
		cursor = conn.cursor()
		val=""
		if len(attr)==1:
			query = ("UPDATE `"+table+"` SET `"+str(attr[0])+"`='"+str(value[0])+"' WHERE `"+where[0]+"` = '"+str(where[1])+"'")
		else:	
			for i in range(len(value)):
                        	if i==0:
                                	val+="`"+attr[i]+"` = '"+str(value[i])+"'"
                        	else:
                                	val+=", `"+attr[i]+"` = '"+str(value[i])+"'"
			query = ("UPDATE `"+table+"` SET "+val+" WHERE "+where[0]+" = '"+str(where[1])+"'")
		try:
			cursor.execute(query)
			conn.commit()
		except mysql.connector.Error as err:
			print "Content-type: text/html"
                	print ""
			print "Erreur Update : "
			print err

	def DelEntry(self, table, attr, value):
		conn = self.Connection()
		cursor = conn.cursor()
		query = ("DELETE FROM `"+table+"` WHERE "+attr+" = '"+value+"'")
		try:
			cursor.execute(query)
			conn.commit()
		except mysql.connector.Error as err:
			print "Erreur DelEntry : "
			print err

	def CreateTeamTable(self, Name):
		conn = self.Connection()
		TableName="CREATE TABLE `"+Name+"`" 
		Attrs=" ( `ID` INT(255) NOT NULL AUTO_INCREMENT, `IDQuestion` INT(255) NOT NULL , PRIMARY KEY (`ID`) )"
		query=TableName+Attrs
		cursor = conn.cursor()
		cursor.execute(query)
		conn.commit()

	def DeleteTable(self, Name):
		conn = self.Connection()
		cursor=conn.cursor()
		query="DROP TABLE "+Name
		cursor.execute(query)
		conn.commit()

	def Compare(self, table, attr, where, value):
		conn = self.Connection()
		attrValue=self.Search(attr, table, where)
		if attrValue[0][0]==value:
			return True
		else:
			return False

	def VerifQuestionTeam(self, teamName, ID):
		conn = self.Connection()
		rows = self.Search("IDQuestion", teamName, "IDQuestion = \'"+ID+"\'")
		if len(rows)==1:
			return False
		else:
			return True

	def RenameTable(self, Old, New):
		conn = self.Connection()
		cursor = conn.cursor()
		query = "ALTER TABLE "+Old+" rename "+New
		cursor.execute(query)
		conn.commit()
