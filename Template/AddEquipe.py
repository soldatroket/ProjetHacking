#!/usr/bin/env python
#coding: utf-8

import ldap
import Utils

#Template qui affiche le formulaire d'ajout d'équipe

def Display(members):
	print '''<div class="col-lg-10">
			<form method="post" action="b2d.py">
					<Legend>Ajout d'équipe</Legend>
					<div class="form-group">
						<Label>Nom d'équipe</Label>
						<input type="text" placeholder="Nom d'équipe" name="teamname" class="form-control">
					</div>
					<div class="form-group">
						<Label>Membres (Max - 4)</Label><br>
						<select name="members" id="members" class="selectpicker" data-live-search="true" multiple data-max-options="4">'''
	for m in members:
		print "<option value="+m+">"+m+"</option>"
	print '''				</select>
					</div>
					<input type="hidden" name="type" value="addequipe">
					<input type="submit" value="Créer">
                                </form>
			</div>
        </div>
        </body>
        </html>'''

