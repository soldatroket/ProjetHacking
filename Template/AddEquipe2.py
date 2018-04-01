#!/usr/bin/env python
#coding: utf-8

import ldap
import Utils

def Display(members):
	print '''<script>
		function changeNumberValue(event){
			hiddenNumber=document.getElementsByName("number");
			number=event.target.value;
			hiddenNumber[0].value=number;
			var x = document.getElementById("divInputMember");
			x.innerHTML="";
			for (var i=1;i<=number;i++){
				var select = document.createElement("select");
				select.name = i;
				select.className = "form-control";
				x.appendChild(select);'''
	for i in members:
		print 		'''var opt=document.createElement("option");'''
		print		'''opt.value="'''+i+'''";'''
		print		'''opt.text="'''+i+'''";'''
		print		"select.appendChild(opt);"
	print '''		}
		}


	</script>'''
	print '''<div class="col-lg-10">
				<form method="post" action="b2d.py">
					<Legend>Ajout d'équipe</Legend>
					<div class="form-group">
						<Label>Nom d'équipe</Label>
						<input type="text" placeholder="Nom d'équipe" name="teamname" class="form-control">
					</div>
					<div class="form-group">
						<Label>Nombres de membres</Label>
						<input type="number" value="0" min="1" max="'''+str(len(members))+'''" onchange="changeNumberValue(event);" class="form-control">
					</div>
					<div class="form-group">
							<div id="divInputMember">
								
							</div>
					</div>
					<input type="hidden" name="number">
					<input type="hidden" name="type" value="addequipe">
					<input type="submit" value="Créer">
                                </form>
			</div>
        </div>
        </body>
        </html>'''

