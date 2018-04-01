#!/usr/lib/python
#-*- coding: utf-8 -*-
def Display(name, team, score, Status, pagename):
	print'''
	<div class="MenuPos">
	<div class="MenuStyle">
		<div class="IDinfo">
			<table>
				<td>
					<tr>INFO. PERSO</tr><br>
					<tr>Bonjour '''
	print name
	print '''
					</tr><br>
					<tr>'''
	if Status=="student":
		print "Equipe : "+team
	else:
		print "IUT : "+team
	print '''
					</tr><br>
					<tr>Points : '''
	print score
	print '''
					</tr><br>
				</td>
			</table>
		</div>
		<hr style="margin-right: 25px;">
		<div class="Menu">
			<table>
				<td>
					<tr>MENU</tr><br><br>
				</td>
				<td>
					<tr><a href="enigmeliste.py">Enigmes</a></tr><br><br>
					<tr><a href="result.py">Resultat</a></tr><br><br>'''
	if Status=="admin":
		print '<tr><a href="administration.py">Admistration</a></tr><br><br>'
	print '''
					<tr><a href="menu.py">Accueil</a></tr><br><br>
					<tr><a href="deconnexion.py">Deconnexion</a></tr><br><br>
				</td>
			</table>
		</div>
		<hr style="margin-right: 25px;">'''
	if Status=="admin" and pagename=="administration":
		print '''
			<div class="Menu">
			<table>
				<td>
					<tr><i>Administration</i></tr><br><br>
				</td>
				<td>
					<tr><a href="administration.py?type=member">Gestion des membres</a></tr><br><br>
					<tr><a href="administration.py?type=enigme">Gestion des énigmes</a></tr><br><br>
					<tr><a href="administration.py?type=equipe">Gestion des équipes</a></tr><br><br>
				</td>
			</table>
			</div>'''
	print '''
	</div>
	</div>'''
