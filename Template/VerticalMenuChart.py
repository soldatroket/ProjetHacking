#!/usr/lib/python
#-*- coding: utf-8 -*-

#Fonction qui permet d'aficher le menu vertical de la page des résultat

def Display(name, team, score, Status, pagename):
	print'''
	<div class="container" style="margin:0px;padding:0px;">
                <div class="row" >
                        <div class="col-lg-2"  style="background-color:lightgrey;height:100%;">
                                <div class="row">
                                        <nav class="col-lg-10 col-lg-offset-1">
                                                <h5>MENU</h5>
                                                <ul class="nav flex-column">
                                                        <li class="nav-item"><a class="nav-link" href="index.py"><span class="glyphicon glyphicon-home"></span> Accueil</a></li>
                                                </ul>
                                        </nav>
                                </div>
                                <div class="col-lg-10 col-lg-offset-1">
                                        <hr>
					<form action="" method="post">
						<Legend>OPTION</Legend>
						<div class="form-group">
							<Label>Résultat par :</Label>
							<select name="donnees" class="form-control">
								<option value="iut">IUT</option>
								<option value="equipe">Equipes</option>
							</select>
						</div>
						<div class="form-group">
                                                        <Label>Afficher en :</Label>
                                                        <select name="graphique" class="form-control">
                                                                <option value="bar">Barre</option>
                                                                <option value="line">Courbe</option>
                                                        	<option value="horizontalBar">Barre horizontal</option>
							</select>
                                                </div>
						<input type="submit" value="appliquer" class="form-control">
					</form>
                                </div>
        </div>'''
