#!/usr/bin/env python
#coding: utf-8

def Display(AllMember):
	print '''<div class="col-lg-10">
                 	<div class="col-lg-8">
            			<div class="panel panel-primary">
              			<div class="panel-heading">Liste des participants ( '''+str(len(AllMember))+''' )</div>
				<table class="table table-striped table-bordered">
					<thead>
						<tr>
							<th>Pseudo</th>
							<th>Action</th>
						</tr>
					</thead>
					<tbody>'''
	for i in AllMember:
		print '<tr>'
		print '<td>'+i+'</td>'
		print '<td><a href="b2d.py?type=delmember&user='+i+'">Supprimez</td>'
		print '</tr>'
	print '''
                                              </tbody>  
					</table>
					</div>
				</div>
                                <div class="col-lg-4">
                                                <div class="panel panel-primary">
						<div class="panel-heading">Ajout de participant</div>
						<div class="panel-body">
						<form method="post" action="b2d.py?type=addmember">
							<div class="form-group">
								<Label>Prenom</Label>
                                                        	<input type="text" placeholder="Prenom" name="prenom" class="form-control" required>
							</div>
							<div class="form-group">                                                        
								<Label>Nom</Label>
								<input type="text" placeholder="Nom" name="nom" class="form-control" required>
							</div>
							<div class="form-group">
								<Label>Email</Label>                                                        
								<input type="email" placeholder="Mail" name="mail" class="form-control" required>
							</div>
							<div class="form-group">
								<Label>Type d'utilisateur</Label>
								<select name="employeType" class="form-control" required>
									<option value="student">Etudiant</option>
									<option value="Admin">Administrateur</option>
								</select>
							</div>                                                       
							<input type="submit" value="Ajoutez" style="margin-top: 0%;">
                                                </form>
						</div>
						</div>
                                </div>
                        </div>
	</div>
</div>
                '''

