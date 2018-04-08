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
   
   
   
.. method:: LdapTest.Connection(dn,mdp)

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



.. method:: LdapTest.Search(baseDN, searchScope, retrieveAttributes, searchFilter, MultResult, returnDN)

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

.. method:: LdapTest.AddMember(cn, sn, mail, DNiut, employee, password)

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

.. method:: LdapTest.DelMember(dn)

   Cette méthode est utilisé pour supprimé un membre de l'annuaire Ldap
   
   :param str dn: Correspond au DN du membre à supprimé.
   :return: *None*
   :rtype: *None*
   
**Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      LdapTest=Utils.ldapp.LdapTest
      LdapTest.DelMember("cn=paul,ou=people,o=concours")
      
.. method:: LdapTest.AddGroup(teamName, members, dnIUT, owner)

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
      
.. method:: LdapTest.ModifyGroup(DNiut ,TeamName, NewTeamName, NewMember)

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

.. method:: LdapTest.Compare(dn, attr, value)

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
      
.. method:: LdapTest.AddScore(value, DNteam)

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

.. method:: LdapTest.Modify(cn, attr, value)

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
      
.. method:: LdapTest.GetDN(dn, usr)

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
   
.. decoratormethod:: SQLTest.init(db)

   Cette méthode nous permet de généré un mot de passe et l'envoye automatiquement à un email
   
   :param str mail: Correspond au mail auquelle ont envoye le mot de passe.
   :return: *Renvoye le mot de passe généré*
   :rtype: *str*
   
**Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      Pass=Utils.password.pass()
      Pass.GeneratePass("jean.paul@gmail.com")
   

cookies
-------

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
      
.. method:: pass.GeneratePass(mail)

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
      
.. method:: pass.SendPass(mail, password)

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
