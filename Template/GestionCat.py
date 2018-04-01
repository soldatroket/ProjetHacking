#!/usr/bin/env python
#coding: utf-8

def Display(Cat):
	print '''<div class="col-lg-10">'''
	print '''	<div class="col-lg-6">
				<div class="panel panel-primary">
              				<div class="panel-heading">Liste des catégories ( '''+str(len(Cat)) +''' )</div>
                        		<table class="table table-striped table-bordered">
						<tr>
							<th>N°</th>
							<th>NOM</th>
							<th colspan="2">ACTION</th>
						</tr>'''
	for row in Cat:
		print '<tr>'
		print '<td>'+str(row[0])+'</td>'
		print '<td>'+row[1]+'</td>'
		print '<td><a href="b2d.py?type=delcat&id='+str(row[0])+'">supprimez</a></td>'
		print '</tr>'
	print '''			</table>
				</div>
        		</div>
			<div class="col-lg-4">
                        	<div class="panel panel-primary">
                     			<div class="panel-heading">Ajout de catégorie</div>
              				<div class="panel-body">
                   				<form method="post" action="b2d.py?type=addcat">
                                                        <div class="form-group">
                                                                <Label>Nom Catégorie</Label>
                                                                <input type="text" placeholder="Nom" name="catname" class="form-control" required>
                                                        </div>
                                                        <input type="submit" value="Ajoutez" style="margin-top: 0%;">
                                                </form>
                                   	</div>
                       		</div>
                	</div>
        	</div>
		</div>
        </body>
        </html>'''
