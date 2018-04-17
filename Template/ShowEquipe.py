#!/usr/bin/env python
#coding: utf-8

import ldap
import Utils

#Fonction qui permmet d'afficher la liste des équipes d'un IUT

def Display(equipe, dniut):
	print '''<div class="col-lg-10">
				<div class="Titre">
						<a href="administration.py?type=addequipe" class="badge badge-primary">Ajouter une équipe</a>
				</div>
				<div class="panel panel-primary">
                                        <div class="panel-heading">Mes énigmes ( '''+str(len(equipe)) +''' )</div>
						<table class="table table-bordered table-striped">
							<thead>
								<tr>
									<th>Nom d'équipe</th>
									<th>Membres</th>
									<th colspan="2">ACTIONS</th>
								</tr>
							</thead>'''
	for i in range(0, len(equipe)):
		InfoMembers, DNIUTMembers=[], []
                LdapMod=Utils.LdapTest()
		baseDN = "cn="+equipe[i]+","+dniut
       		searchScope = ldap.SCOPE_BASE
       		AllFilter = "objectClass=*"
		MemberFilter = "objectclass=inetOrgPerson"
                IUTFilter = "objectclass=organizationalUnit"
	        DNMember=LdapMod.Search(baseDN, searchScope, ['member'], AllFilter, True, False)
		for dn in range(0, len(DNMember)):
			InfoMember=LdapMod.Search(DNMember[dn], searchScope, ['cn', 'secretary'], MemberFilter, False, False)
			InfoMembers.append(InfoMember)
		for dnIUT in range(0, len(InfoMembers)):
			dniut=InfoMembers[dnIUT][1][0]
			NameIUT=LdapMod.Search(dniut, searchScope, ['ou'], IUTFilter, False, False)
                        InfoMembers[dnIUT][1][0]=NameIUT
		print '''					<tr>
                							<td>'''+str(equipe[i])+'''</td>
                							<td>'''
		for y in range(0, len(InfoMembers)):
			print InfoMembers[y][0][0]+"(IUT : "+InfoMembers[y][1][0]+") | "
		print '''						</td>
                							<td>
										<a href="administration.py?type=modifequipe&name='''+str(equipe[i])+'''">modifier</a>
									</td>
                							<td>
										<a href="b2d.py?type=delequipe&teamname='''+str(equipe[i])+'''">supprimer</a>
									</td>
               							</tr>'''
        print '''				</table>
					</div>
				</div>
			</div>
        </div>
        </body>
        </html>'''

