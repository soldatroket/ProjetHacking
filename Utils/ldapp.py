#!/usr/lib/python
#coding: utf-8
import ldap
import ldap.modlist as modlist
import password

#Fichier qui contient la classe LdsapTest qui permet de manipuler l'annuaire Ldap

class LdapTest:
	#Class permettant de réaliser des opérations dans l'annuaire Ldap
	def Connection(self, dn, mdp):
		#Fonction qui permet de se connecter à un annuaire Ldap et retourne la connexion
		l=ldap.initialize("ldap://127.0.0.1")			#On initialise la connexion sur notre Ldap
		try:
			l.protocol_version=ldap.VERSION3		#Définition de la version LDAP utilisé
			l.simple_bind_s(dn, mdp)			#On se connecte à l'annuaire
			valid = True
			return l					#On retourne la connexion
		except ldap.LDAPError, error:
			print error

	def Search(self, baseDN, searchScope, retrieveAttributes, searchFilter, MultResult, returnDN):
		#Fonction qui nous permet de réaliser des recherches dans l'annuaire Ldap
		l=self.Connection("cn=admin,o=concours", "root") 						#On se connecte à l'annuaire
		ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)		#On effectue une recherche dans l'annuaire qui nous renvoye un code unique
		result_set = []
		if MultResult == False:										#On regarde si l'ont souhaite plusieurs ou un seul résultat en retour
			result_type, result_data = l.result(ldap_result_id, 0)					#On récupére le type et les données de la recherche grace aux code( le 0 signifie une seul réponse)
			if result_type == ldap.RES_SEARCH_ENTRY:						#On vérifie que le type de donnée corresponde bien à une recherche
				result_set.append(result_data)
			if len(result_set) > 0:									#On vérifie que l'ont à bien un résultat
				if returnDN==False:								#On vérifie si l'ont souhaite retourné ou non le DN de la réponse
					resultat=result_set[0][0][1]						#La réponse ce trouvant sous forme de tableau, on séléctione uniquement la réponse
					if len(retrieveAttributes)==1:						#On vérifie le nombre d'attribut de recherche
						resultat=resultat[retrieveAttributes[0]]
						return resultat[0]						#Retourne une valeur
					elif len(retrieveAttributes)>1:
						resultat2=[]
						for attr in retrieveAttributes:					#Si l'ont à plusieurs attribue on va alors réaliser une boucle sur chaques attributs
							resultat2.append(resultat[attr])
						return resultat2						#Retourne un tableau
				else:
					resultat=result_set[0][0][0]						#On séléctionne la partie du tableau correspondant au DN de la réponse
					return resultat								#retourne une valeur
			else:
				return "Pas de resultat"							#Si l'ont à pas de résultat ont retourne "Pas de resultat"
		else:
			result_type, result_data = l.result(ldap_result_id, 1)					#On récupére le type et les données de la recherche (1 signifie plusieurs résultats)
			if result_type == ldap.RES_SEARCH_RESULT:
				result_set.append(result_data)
			if len(result_set) > 0:
				resultat=[]
				for i in result_set[0]:								#On fait une boucle sur chaque résultat
					r=i[1]
					resultat3=[]
					for dico in r:								#On parcours chaque élément de la réponse
						if retrieveAttributes.count(dico)!=0:				#Si l'ont à un attribut de recherche présent dans la réponse
							for res in r[dico]:					#Pour chaque attribut présent dans la réponse je vais l'ajouter dans un tableaux
								resultat3.append(res)
					if len(retrieveAttributes)==1:
						for elem in resultat3:						#Je boucle sur chaque élément de mon tableau
							resultat.append(elem)					#J'ajoute chaque élément dnas mon tableau resultat
					elif len(retrieveAttributes)>1:
						resultat.append(resultat3)
				return resultat
			else:
				return "Pas de resultat"							#Si l'ont à pas de resultat à la recherche on retourne "Pas de resultat"
		l.unbind_s()											#Déconnexion


	def AddMember(self, cn, sn, mail, DNiut, employee, password):
		#fonction permettant d'ajoutez un membre
		l=self.Connection("cn=admin,o=concours", "root")						#On se connecte à l'annuaire Ldap
		dn="cn="+cn+",ou=people,o=concours"								#On reconstitue le dn de l'utilisateur à ajouté
		attrs = {}											#On crée un dictionnaire qui contiendra les données du membre
		attrs['objectClass'] = 'inetOrgPerson'
		attrs['cn'] = cn
		attrs['sn'] = sn
		attrs['mail'] = mail
		attrs['secretary'] = DNiut
		attrs['userPassword'] = password
		attrs['employeeType'] = str(employee)
		ldif = modlist.addModlist(attrs)								#On crée le ldif associé à ce dictionnaire
		l.add_s(dn,ldif)										#On ajoute le ldif dans l'annuaire
		l.unbind_s()											#Déconnexion

	def DelMember(self, dn):
		#Fonction utilisé pour supprimer un membre
		l=self.Connection("cn=admin,o=concours", "root")
		l.delete_s(dn)											#On supprime le membre dans l'annuaire au DN concerné
		l.unbind_s()

	def AddGroup(self, teamName, members, dnIUT, owner):
		#Fonction utilisé pour ajouté une équipe
		l=self.Connection("cn=admin,o=concours", "root")
		dn="cn="+teamName+","+dnIUT									#On crée le DN de l'équipe
		attrs = {}											#On crée le dictionnaire qui vas contenire les info de l'équipe
		attrs['objectClass']='groupofnames'
		attrs['cn']=teamName
		DNmembers=[]
		for i in members:										#Les membres sont reçus sous forme de tableau, on va donc boucler dessus afin de reconstituer le DN de chaque membre
			DNmembers.append("cn="+str(i)+",ou=people,o=concours")
		attrs['member']=DNmembers
		attrs['owner']="cn="+owner+",ou=people,o=concours"
		attrs['description']="0"
		ldif = modlist.addModlist(attrs)
		l.add_s(dn,ldif)
		l.unbind_s()

	def ModifyGroup(self,DNiut ,TeamName, NewTeamName, NewMember):
		#Fonction qui va modifier une équipe
		l=self.Connection("cn=admin,o=concours", "root")
		newdn="cn="+NewTeamName+","+DNiut								#On crée le nouveau DN de l'équipe
		l.modrdn_s('cn='+TeamName+','+DNiut, 'cn='+NewTeamName, True)					#On modifie le DN de l'équipe
		mod = [(ldap.MOD_REPLACE, "member", NewMember )]
		l.modify_s(newdn,mod)										#On modifie l'équipe
		l.unbind_s()											#Déconnexion

	def Compare(self, dn, attr, value):
		#Fonction qui nous sert à comparé des valeurs dans l'annuaire
		l=self.Connection("cn=admin,o=concours", "root")
		try:
			resultat=l.compare_s(dn,attr,value)							#On compare la valeur de l'attribut "attr" avec la valeur "value" 
			return resultat										#retourne un True ou False
		except ldap.LDAPError:
			return False
		l.unbind_s()											#Déconnexion

	def AddScore(self, value, DNteam):
		#Fonction utilisé pour rajouter des points à une équipe
		l=self.Connection("cn=admin,o=concours", "root")
		searchScope = ldap.SCOPE_SUBTREE
		retrieveAttributes = ['description']								#On séléctionne l'attribut descritpion qui correspond au score de l'équipe
		searchFilter = "objectClass=groupOfNames"							#On séléctionne uniquement les équipes
		oldscore = self.Search(DNteam, searchScope, retrieveAttributes, searchFilter, False, False)	#On fait une recherche pour récuperé uniquement le score de l'équipe concerné
		newscore = int(oldscore)+value									#On ajoute au nombre de point de l'équipe la valeur souhaiter
		old = {'description':str(oldscore)}
		new = {'description':str(newscore)}
		ldif = modlist.modifyModlist(old,new)								#On crée le ldif pour modifier la description de l'équipe
		l.modify_s(DNteam,ldif)										#On applique la modification
		l.unbind_s()											#Déconnexion

	def GetScoreIUT(self, DNiut):
		#Fonction utilisé pour obtenir le score global d'un IUT
                searchScope = ldap.SCOPE_ONELEVEL
                retrieveAttributes = ['description']
                searchFilter = "objectClass=groupOfNames"
		TeamScore=self.Search(DNiut, searchScope, retrieveAttributes, searchFilter, True, False)	#On récupére le score de toutes les équipes d'un IUT sous forme de tableau
		Total=0
		for i in TeamScore:										#On boucle sur le score pour l'additionner
			Total+=int(i)
		return Total											#On retourne le total

	def Modify(self, cn, attr, value):
		#Fonction qui vas nous permettre de modifier un membre
		l=self.Connection("cn=admin,o=concours", "root")
                dn="cn="+cn+",ou=people,o=concours"
                mod = [(ldap.MOD_REPLACE, attr, value )]
                l.modify_s(dn,mod)
                l.unbind_s()

	def GetDN(self, dn, usr):
		#Fonction qui nous permet de retourné le DN d'une réponse (inutile)
		searchScope = ldap.SCOPE_SUBTREE
		retrieveAttributes = None
		searchFilter = "cn="+usr
		dn=self.Search(dn, searchScope, retrieveAttributes, searchFilter, False, True)
		return dn
