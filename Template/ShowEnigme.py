#!/usr/bin/env python
#coding: utf-8

def Display(rows):
	print '''<div class="col-lg-10">'''
	print '''	<div class="col-lg-12">
				<a href="administration.py?type=addenigme" class="badge badge-primary">Ajouter une énigme</a>
				<a href="administration.py?type=categorie" class="badge badge-primary">Gestion des Catégories</a>
			</div>
			<div class="col-lg-12">
				<div class="panel panel-primary">
              				<div class="panel-heading">Mes énigmes ( '''+str(len(rows)) +''' )</div>
                        		<table class="table table-striped table-bordered">
						<tr>
							<th>N°</th>
							<th>TITRE</th>
							<th colspan="2">ACTION</th>
						</tr>'''
	for row in rows:
		print '<tr>'
		print '<td>'+str(row[0])+'</td>'
		print '<td>'+row[1]+'</td>'
		print '<td><a href="administration.py?type=modifenigme&id='+str(row[0])+'">modifier</a></td>'
		print '<td><a href="b2d.py?type=delenigme&id='+str(row[0])+'">supprimer</a></td>'
		print '</tr>'
	print '''			</table>
				</div>
        		</div>
        	</div>
		</div>
        </body>
        </html>'''
