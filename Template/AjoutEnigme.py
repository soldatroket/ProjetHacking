#!/usr/bin/env python
#coding: utf-8

def Display(point, cat):
	print '''<div class="col-lg-10">
			<div class="row">
				<form enctype="multipart/form-data" method="post" action="b2d.py" class="col-lg-8 col-lg-offset-2">
					<Legend>Ajout d'énigme</Legend>
                                        <div class="form-group">
						<Label>TITRE :</Label>
						<input type="text" name="title" placeholder="Titre de l'énigme" class="form-control" required>
					</div>
                                        <div class="form-group">
						<Label>QUESTION :</Label>
						<textarea name="answer" placeholder="Question de votre énigme" class="form-control" required></textarea>
					</div>
					<div class="form-group">
						<Label>REPONSE :</Label>
						<textarea name="reponse" class="form-control" required></textarea>
					</div>
                                         <div class="form-group">
						<Label>DIFFICULTER : </Label>
                                                <select name="strenght" class="form-control" required>'''
	for row in point:
		print "<option value="+str(row[2])+">"+row[1]+" ("+str(row[2])+" points)</option>"
	print '''
                                        	</select>
					</div>
                                       	<div class="form-group">
                                               	<Label>CATEGORIE :</Label>
                                                <select name="cat" class="form-control" required>'''
	for row in cat:
		print "<option value="+str(row[1])+">"+row[1]+"</option>"
	print '''
                                        	</select>
					</div>
					<div class="form-group">
                                                <Label>Fichier: </Label>
                                                <input name="file" type="file" id="file">
						<span class="badge badge-info">L'ajout d'un fichier est optionelle</span>
                                        </div>
                                        <input type="submit">
					<input type="hidden" name="type" value="addenigme"></td>
                                </form>
			</div>
		</div>
		</div>
                        </body>
                        </html>'''

