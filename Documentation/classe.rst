=====
Class
=====

.. contents:: Liste des classes
   :depth: 2

LdapTest
--------

.. class:: LdapTest

   Description
   +++++++++++

       Cette classe nous permet de **manipuler l'annuaire Ldap**.
       Avant tout il vous faut invoqué la classe si vous souhaitez l'utilisé.
       Pour ce faire, vous faite :

.. code-block:: python
   :linenos:
   
   LdapTest=Utils.ldapp.LdapTest()
   
   
   
.. decoratormethod:: LdapTest.Connection(dn,mdp)

   Cette méthode est utilisé uniquement par le script ldapp.py lui même.
   Elle permet d'initialisé une connection avec un annuaire Ldap et retourne un objet **LdapObject**
   
   :param str dn: DN de connexion
   :param str recipient: Mot de passe liée au DN
   :return: LdapObject
   :rtype: LdapObject
   
   **Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      LdapObj=LdapTest.Connection("cn=admin,o=concours","toto")



.. decoratormethod:: LdapTest.Search(baseDN, searchScope, retrieveAttributes, searchFilter, MultResult, returnDN)

   Cette méthode est utilisé pour réaliser des recherches dans l'annuaire Ldap.
   
   :param str baseDN: DN de base d'ou l'ont souhaite réaliser la recherche
   :param str searchScope: Paramétre de recherche Ldap, peut valoir : LDAP.SCOPE_BASE, LDAP.SCOPE_SUBTREE, LDAP.SCOPE_CHILDREN 
   :param list(str) retrievAttributes: Tableau contenant le nom du/des attributs recherchés
   :param str searchFilter: Contient la condition de recherche
   :param bool retrievAttributes: Si **False** la méthode retournera une seule reponse sous forme de chaine de caractére. **True** elle retournera une ou plusieurs réponse sous forme de tableau.
   :param list(str) retrievAttributes: Si **True** la méthode retournera uniquement le **DN** de la réponse
   :return: Un tableau ou une chaine de caractére
   :rtype: list(str) or str
   
.. warning:: Pour pouvoir utilisé les paramétres de recherches Ldap, vous devez tout d'abord importé le module **ldap**
   
**Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      LdapTest=Utils.ldapp.LdapTest
      result=LdapTest.Search("ou=M2M,o=iut,o=concours", LDAP.SCOPE_SUBTREE, ["cn"], "objectclass=inetorgperson", True, False)

.. decoratormethod:: LdapTest.AddMember(cn, sn, mail, DNiut, employee, password)

   Cette méthode est utilisé pour ajouté un membre dans dans l'annuaire Ldap sous le noeud *ou=people,o=concours*.
   
   :param str cn: Correspond au pseudonyme du membre.
   :param str sn: Correspond au second pseudonyme du membre. 
   :param str mail: Correspond au mail unique du membre.
   :param str DNiut: Contient le DN de l'iut auquelle est rataché le membre.
   :param str employee: Correspond au type du membre.Pour un administrateur : **Admin** .Pour un joueur lambda : **Student** .
   :param str password: Correspond au mot de passe du membre préalablement chiffré en sha1.
   :return: *None*
   :rtype: *None*
   
**Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      LdapTest=Utils.ldapp.LdapTest
      LdapTest.AddMember("paul", "dupont", "paul.dupont@yopmail.com", "ou=M2M,o=iut,o=concours", "Admin", "ZedkfjvDFg")

.. decoratormethod:: LdapTest.DelMember(dn)

   Cette méthode est utilisé pour supprimé un membre de l'annuaire Ldap
   
   :param str dn: Correspond au DN du membre à supprimé.
   :return: *None*
   :rtype: *None*
   
**Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      LdapTest=Utils.ldapp.LdapTest
      LdapTest.DelMember("cn=paul,ou=people,o=concours")
      
.. decoratormethod:: LdapTest.AddGroup(teamName, members, dnIUT, owner)

   Cette méthode est utilisé pour ajouté une équipe dans l'annuaire Ldap.
   
   :param str teamName: Correspond au nom de l'équipe.
   :param list(str) members: Correspond à un tableau qui contient le pseudonyme de tout les membres de l'équipe. 
   :param str dnIUT: Contient le DN de l'iut auquelle est rataché l'équipe.
   :param str owner: Contient le pseudo de l'Administrateur qui est responsable de l'équipe.
   :return: *None*
   :rtype: *None*
   
**Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      LdapTest=Utils.ldapp.LdapTest
      LdapTest.AddGroup("LesHackeursDu92", ["jean","pierre","paul"], "ou=M2M,o=iut,o=concours", "henry")
      
.. decoratormethod:: LdapTest.ModifyGroup(DNiut ,TeamName, NewTeamName, NewMember)

   Cette méthode est utilisé pour modifié une équipe dans l'annuaire Ldap.
   
   :param str DNiut: Correspond au DN de l'iut responsable de l'équipe.
   :param str TeamName: Correspond au nom actuel de l'équipe. 
   :param str NewTeamName: Correspond au nouveau nom de l'équipe.
   :param str NewMember: Correspond à un tableau contenant les DN des membres de l'équipe.
   :return: *None*
   :rtype: *None*
   
**Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      LdapTest=Utils.ldapp.LdapTest
      LdapTest.ModifyGroup("ou=M2M,o=iut,o=concours", "LesHackeurs92", "LesBG92",["cn=paul,ou=people,o=concours","cn=roberto,ou=people,o=concours"])

.. decoratormethod:: LdapTest.Compare(dn, attr, value)

   Cette méthode est utilisé pour comparé l'annuaire Ldap.
   
   :param str dn: Correspond au DN de l'objet qui contient l'attribut que vous souaitez comparé.
   :param str attr : Correspond à l'attribut à comparé. 
   :param str value: Contient la valeur qui vas être utilisé pour la comparaison.
   :return: Retourne un boolean qui correpsond au résulat de la comparaison. *True = Comparaison vérifié*
   :rtype: *bool*
   
**Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      LdapTest=Utils.ldapp.LdapTest
      result=LdapTest.Compare("cn=paul,ou=people,o=concours", "userPassword", "ZlDFgfdgdLGF")
      
.. decoratormethod:: LdapTest.AddScore(value, DNteam)

   Cette méthode est utilisé pour rajouté un score à une équipe de l'annuaire Ldap.
   
   :param int value: Correspond au nombre de points que l'ont souhaite rajouté à l'équipe.
   :param str DNteam: Correspond au DN de l'équipe.
   :return: *None*
   :rtype: *None*
   
**Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      LdapTest=Utils.ldapp.LdapTest
      LdapTest.AddScore(12, "LesBG92")

.. decoratormethod:: LdapTest.Modify(cn, attr, value)

   Cette méthode nous permet de modifié un attribut d'un membre
   
   :param str cn: Pseudonyme du membre à modifié.
   :param str attr: Nom de l'attribut à modifié.
   :param str value: La nouvelle valeur de l'attibut
   :return: *None*
   :rtype: *None*
   
**Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      LdapTest=Utils.ldapp.LdapTest
      LdapTest.Modify("jean", "mail", "jean.paul@gmail.com"
      
.. decoratormethod:: LdapTest.GetDN(dn, usr)

   Cette méthode nous permet de retourné le DN d'une réponse
   
   :param str dn: Noeud de base dans lequelle on éffectue la recherche.
   :param str usr: Pseudonyme du membre
   :return: *DN de la réponse*
   :rtype: *str*
   
.. warning:: Cette fonction est obsolète et inutile, je conseille de ne pas l'utilisé.

---------------------------

SqlTest
-------

.. class:: SQLTest

   Description
   +++++++++++

       Cette classe nous permet de **manipulé la base mySQL**.
       Avant tout il vous faut invoqué votre classe si vous souhaitez l'utilisé.
       Pour ce faire, vous faite :
       
.. code-block:: python
   :linenos:
   
   Password=Utils.sql.SQLTest()
   
.. decoratormethod:: SQLTest.__init__(db)

   Ce constructeur de la classe SQLTest permet de définir la base de donnée utilisé par défaut.
   
   :param str db: Correspond au nom de la base utilisé.
   :return: *None*
   :rtype: *None*
   
**Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      sqlTest=Utils.sql.SQLTest("concours")
      
.. decoratormethod:: SQLTest.SetDB(db)

   Cette méthode permet de (re)définir la base de donnée utilisé.
   
   :param str db: Correspond au nom de la base utilisé.
   :return: *None*
   :rtype: *None*
   
**Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      sqlTest=Utils.sql.SQLTest()
      sqlTest.SetDB("concours")
      
.. decoratormethod:: SQLTest.Connection()

   Cette méthode est appelé uniquement par la classe SQLTest elle même. Elle permet de se connecté à une base mySQL et retourné une connexion
   
   :return: *Connector*
   :rtype: *Connector*

.. decoratormethod:: SQLTest.Search(Select, From, Where)

   Cette classe permet d'effectué une recherche dans la base mySQL.
   
   :param str Select: Correspond au attributs recherché, peut être multiple en les espaçant d'une virgule : *,*
   :param str From: Correspond au nom de la table dans lequel il faut recherché les attributs.
   :param str Where: Correspond à la condition de recherche. Mettre "None" pour aucun paramêtre de recherche
   :return: *Retourne le résultat sous forme de tableau*
   :rtype: *list*
   
**Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      sqlTest=Utils.sql.SQLTest("concours")
      recherche=sqlTest.Search("IDcat, NomCat","categorie","ID = 2")
      
.. decoratormethod:: SQLTest.AddEntry(table, attr, value)

   Cette méthode permet d'ajouté une entrée dans la base mySQL.
   
   :param str table: Correspond à la table dans laquel ont souhaite rajouté une entrée.
   :param str attr: Correspond au nom de l'attribut auquel ont rajoute l'entrée. Peut être multiple en les espaçant d'une virgule
   :param tuple value: Correspond à la valeur de l'attribut. Doit être dans un tuple et dans le même ordre que les attributs de la variable attr
   :return: *Retourne le résultat sous forme de tableau*
   :rtype: *list*
   
**Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      sqlDB=Utils.sql.SQLTest("concours")
      attr="Titre, Question, Reponse, Catégorie, Point, owner"
		sqlDB.AddEntry("enigmes", attr, ("Mer", "j", "jaune", "poisson", "dur", "paul"))
      
.. decoratormethod:: SQLTest.UpdateEntry(table, attr, value, where)
   
   Cette méthode permet de mettre à jour une entrée dans la base mySQL.
   
   :param str table: Correspond à la table dans laquel ont souhaite mettre à jour l'entrée.
   :param tuple attr: Correspond au nom de l'attribut auquel ont rajoute l'entrée doit ce trouvé dans un tuple et peut donc être multiple.
   :param tuple value: Correspond à la valeur de l'attribut il doit aussi être dans un tuple et dans le même ordre que la variable attr.
   :param tuple where: Correspond à la condition de la ligne à laquel ont souhaite modifié l'entrée. Doit ce trouvé dan sun tuple. Le premier élément correspond à l'attribut. Et le deuxième élément à la valeur que doit être égal l'attribut.
   :return: *None*
   :rtype: *None*
   
**Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      sqlDB=Utils.sql.SQLTest("concours")
      fn="cat.jpeg"
      sqlDB.UpdateEntry("enigmes", ("Fichier",), (fn,), ("ID", "2"))
		
.. decoratormethod:: SQLTest.DelEntry(table, attr, value)
   
   Cette méthode permet de supprimé une entrée dans la base mySQL.
   
   :param str table: Correspond à la table dans laquel ont souhaite supprimé l'entrée.
   :param str attr: Correspond au nom de l'attribut qui qui correpsond à la condition de suppression.
   :param str value: Correspond à la valeur dont la variable attr doit être égal pour supprimé l'entrée.
   :return: *None*
   :rtype: *None*
   
**Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      sqlDB=Utils.sql.SQLTest("concours")
      sqlDB.DelEntry("equipe", "ID", "2")
      
.. decoratormethod:: SQLTest.CreateTeamTable(Name)
   
   Cette méthode permet de crée la table d'une équipe dans la base mySQL.
   
   :param str Name: Correspond au nom de l'équipe.
   :return: *None*
   :rtype: *None*
   
**Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      sqlDB=Utils.sql.SQLTest("concours")
      sqlDB.CreateTeamTable("bg")
      
.. decoratormethod:: SQLTest.DeleteTable(Name)
   
   Cette méthode permet de supprimé une table dans la base mySQL.
   
   :param str Name: Correspond au nom de la table.
   :return: *None*
   :rtype: *None*
   
**Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      sqlDB=Utils.sql.SQLTest("concours")
      sqlDB.DeleteTable("bg")
      
.. decoratormethod:: SQLTest.Compare(table, attr, where, value)
   
   Cette méthode permet de supprimé une table dans la base mySQL.
   
   :param str table: Correspond au nom de la table dans lequel il faut recherché l'attribut.
   :param str attr: Correspond à l'attribut recherché.
   :param str where: Correspond à la condition de recherche. Mettre "None" pour aucun paramêtre de recherche.
   :param str or int value: Correspond à la valeur de comparaison.
   :return: *Retourne True pour une comparaison vérifé et False pour une comparaison non vérifié*
   :rtype: *bool*
   
**Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      sqlDB=Utils.sql.SQLTest("concours")
      verifR=sqlDB.Compare("enigmes", "reponse", "ID = 2", "42")
      
.. decoratormethod:: SQLTest.VerifQuestionTeam(teamName, ID)
   
   Cette méthode permet de vérifié si une équipe donné à répondue ou non à une énigme grâce à son ID.
   
   :param str teamName: Correspond au nom de l'équipe en question.
   :param str ID: Correspond à l'ID de l'énigme à vérifié.
   :return: *Retourne True si l'équipe n'y à pas répondue et False dans le cas contraire*
   :rtype: *bool*
   
**Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      sqlDB=Utils.sql.SQLTest("concours")
      verifQ=sqlDB.VerifQuestionTeam("bg", "2")   

.. decoratormethod:: SQLTest.RenameTable(Old, New)
   
   Cette méthode permet de rennomer une table dans la base mySQL.
   
   :param str Old: Correspond à l'ancien nom de la table.
   :param str New: Correspond au nouveau nom de la table.
   :return: *None*
   :rtype: *None*
   
**Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      sqlDB=Utils.sql.SQLTest("concours")
      verifQ=sqlDB.RenameTable("equipe", "team")  
      
-------------------------

cookies
-------

.. class:: cookies

   Description
   +++++++++++

       Cette classe nous permet de **d'écrire et de lire des cookies** dans un navigateur.
       Avant tout il vous faut invoqué la classe si vous souhaitez l'utilisé.
       Pour ce faire, vous faite :

.. code-block:: python
   :linenos:
   
   LdapTest=Utils.cookies.cookies()
   
.. decoratormethod:: SQLTest.SetCookie(cn, memberof, DNmemberof,DNiut,status)
   
   Cette méthode permet d'écrire les cookies nécessaire los de la connexion d'un utilisateur.
   Les cookies inscrits lors de la connexion sont :
+----------------+-----------------------------+
| Nom du cookie  | Déscription                 |
+================+=============================+
| name           | Pseudonyme du membre        |
+----------------+-----------------------------+
| status         | Status du membre:           |
|		 |  Admin ou student           |
+----------------+-----------------------------+
| DNteamName     | DN de l'équipe du membre    |
+----------------+-----------------------------|
| DNiut          | DN de l'iut liée au membre  |
+----------------+-----------------------------+
| teamName	 |  Nom de l'équipe du membre  |
+----------------+-----------------------------+   
   :param str Old: Correspond à l'ancien nom de la table.
   :param str New: Correspond au nouveau nom de la table.
   :return: *None*
   :rtype: *None*
   
**Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      sqlDB=Utils.sql.SQLTest("concours")
      verifQ=sqlDB.RenameTable("equipe", "team")  

-------------------------------

password
--------

.. class:: pass

   Description
   +++++++++++

       Cette classe nous permet de **généré un mot de passe et de l'envoyé par mail**.
       Avant tout il vous faut invoqué votre classe si vous souhaitez l'utilisé.
       Pour ce faire, vous faite :
       
.. code-block:: python
   :linenos:
   
   Password=Utils.password.pass()
      
.. decoratormethod:: pass.GeneratePass(mail)

   Cette méthode nous permet de généré un mot de passe et l'envoye automatiquement à un email
   
   :param str mail: Correspond au mail auquelle ont envoye le mot de passe.
   :return: *Renvoye le mot de passe généré*
   :rtype: *str*
   
**Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      Pass=Utils.password.pass()
      Pass.GeneratePass("jean.paul@gmail.com")
      
.. seealso:: L'appel de cette méthode entraine l'appel de la méthode suivante *SendPass*.
      
.. decoratormethod:: pass.SendPass(mail, password)

   Cette méthode nous permet d'envoyé un mot de passe à un mail donné
   
   :param str mail: Correspond au mail auquelle ont envoye le mot de passe.
   :param str password: Corepsond au mot de passe à envoyé.
   :return: *None*
   :rtype: *None*
   
**Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      Pass=Utils.password.pass()
      Pass.SendPass("jean.paul@gmail.com", "toto")
      
.. seealso:: Cette méthode et uniquement appelé par la méthode GeneratePass(). Il est déconseillé d'appelé cette méthode directement
