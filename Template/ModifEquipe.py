#!/usr/bin/env python
#coding: utf-8

import ldap
import Utils

def Display(TeamName, TeamMembers, members):
	TeamLength=len(TeamMembers)
	print '''<div class="col-lg-10">
				<form method="post" action="b2d.py">
					<Legend>Modification d'équipe</Legend>
					<div class="form-group">
						<Label>Nom d'équipe</Label>
						<input type="text" placeholder="'''+TeamName+'''" value="'''+TeamName+'''" name="newteamname" class="form-control">
					</div>
					<div class="form-group">
						<Label>Membres (Max - 4)</Label><br>
						<select name="members" id="members" class="selectpicker" data-live-search="true" multiple data-max-options="4">'''
	for i in members:
		if TeamMembers.count(i)==0:
			print '<option value='+i+'>'+i+'</option>'
		else:
			print '<option value='+i+' selected="selected">'+i+'</option>'
	print "</select>"
	print '''			</div>
					<input type="hidden" name="teamname" value="'''+TeamName+'''">
					<input type="hidden" name="type" value="modifequipe">
					<input type="submit" value="Modifier">
					<input type="reset" value="Annuler modification" id="reset">
                                </form>
			</div>
        </div>
<script>
$( "#reset" ).click(function() {
  $("#members").val( '''
	print TeamMembers,
	print ''' );
  $("#members").selectpicker("refresh");
});
$(document).ready(function () {
    $('.selectpicker').selectpicker();
});
</script>
</body>
</html>'''
