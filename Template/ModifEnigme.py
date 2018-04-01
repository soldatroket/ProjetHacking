#!/usr/bin/env python
#coding: UTF-8

def Display(enigme, cat, point):
	print '''<div class="col-lg-10">
			<div class="row">
			<form enctype="multipart/form-data" method="post" action="b2d.py?type=modifenigme" class="col-lg-8 col-lg-offset-2">
						<Legend>Modification d'énigmes</Legend>				
						<div class="form-group">                                        
							<Label>TITRE :</Label>
							<input type="text" name="title" placeholder="'''+enigme[0][1].encode('utf-8')+'''" value="'''+enigme[0][1].encode('utf-8')+'''" class="form-control">
						</div>
						<div class="form-group">
							<Label>QUESTION :</Label>
							<textarea name="answer" placeholder="'''+enigme[0][2].encode('utf-8')+'''" value="'''+str(enigme[0][2].encode('utf-8'))+'''" class="form-control">'''+enigme[0][2].encode('utf-8')+'''</textarea>
						</div>
						<div class="form-group">
                                                	<Label>REPONSE :</Label>
							<textarea name="reponse" class="form-control"></textarea>
							<span class="badge badge-info">Votre réponse n'apparait pas car elle est crypter</span>
						</div>
						<div class="form-group">
							<Label>DIFFICULTER : </Label>
                                                	<select name="strenght" class="form-control">'''
	for row in point:
        	if row[2]==enigme[0][5]:
              		print "<option value="+str(row[2])+" selected>"+row[1]+" ("+str(row[2])+" points)</option>"
        	else:
                	print "<option value="+str(row[2])+">"+row[1]+" ("+str(row[2])+" points)</option>"
	print '''
                                       			</select>
						</div>
                                        	<div class="form-group">
                                                	<Label>CATEGORIE :</Label>
                                                	<select name="cat" class="form-control">'''
	for row in cat:
        	if row[1]==enigme[0][4]:
			print "<option value="+str(row[1])+" selected>"+row[1]+"</option>"
		else:
			print "<option value="+str(row[1])+">"+row[1]+"</option>"
	print '''
                                                	</select>
						</div>
						<div class="form-group">
                                                	<Label>Fichier: </Label>
							<input type="file" name="file">'''
	if enigme[0][6]!="":
		print '''				<span class="badge badge-pill badge-primary">Fichier Uploader : '''+str(enigme[0][6])+'''</span>
						</div>
                                        	<input name="ID" type="hidden" value='''+str(enigme[0][0])+'''>
						<input type="submit" value="Modifier">
						<input type="reset" value="Annuler modification">
                                </form>
                                </div>
                        </div>
			</div>
			</div>
                        </body>
			</html>'''
