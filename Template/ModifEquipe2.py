#!/usr/bin/env python
#coding: utf-8

import ldap
import Utils

def Display(TeamName, TeamMembers, members):
	TeamLength=len(TeamMembers)
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
					<Legend>Modification d'équipe</Legend>
					<div class="form-group">
						<Label>Nom d'équipe</Label>
						<input type="text" placeholder="'''+TeamName+'''" value="'''+TeamName+'''" name="newteamname" class="form-control">
					</div>
					<div class="form-group">
						<Label>Nombres de membres</Label>
						<input type="number" value="'''+str(TeamLength)+'''" min="1" max="'''+str(len(members))+'''" onchange="changeNumberValue(event);" class="form-control">
					</div>
					<div class="form-group">
						<Label>Membres</Label>
						<div id="divInputMember">'''
	for y in range(TeamLength):
		print "<select name="+str(y+1)+" class='form-control'>"
		print '<option value='+TeamMembers[y]+' selected="selected" >'+TeamMembers[y]+'</option>'
		for i in members:
			if TeamMembers.count(i)==0:
				print '<option value='+i+'>'+i+'</option>'
		print "</select>"
	print '''			</div></div>
					<input type="hidden" name="number" value="'''+str(TeamLength)+'''">
					<input type="hidden" name="teamname" value="'''+TeamName+'''">
					<input type="hidden" name="type" value="modifequipe">
					<input type="submit" value="Modifier">
					<input type="reset" value="Annuler modification">
                                </form>
			</div>
        </div>
        </body>
        </html>'''

