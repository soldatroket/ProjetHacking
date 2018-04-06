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
       Avant tout il vous faut invoquer vote classe si vous souhaitez l'utilisé.
       Pour ce faire, vous faite :

.. code-block:: python
   :linenos:
   
   LdapTest=Utils.ldapp.LdapTest
   
   
   
.. method:: LdapTest.Connection(dn,mdp)
            ---------------------------
   Cette méthode est utilisé uniquement par le script lui même.
   Elle permet d'initialisé une connection avec un annuaire Ldap et retourne un objet **LdapObject**
   
   :param str dn: DN de connexion
   :param str recipient: Mot de passe liée au DN
   :return: LdapObject
   :rtype: Object
   
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
   :param str TeamName : Correspond au nom actuel de l'équipe. 
   :param str NewTeamName: Correspond au nouveau nom de l'équipe.
   :param str NewMember: Correspond à un tableau contenant les DN des membres de l'équipe.
   :return: *None*
   :rtype: *None*
   
**Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      LdapTest=Utils.ldapp.LdapTest
      LdapTest.ModifyGroup("ou=M2M,o=iut,o=concours", "LesHackeurs92", "LesBG92",["cn=paul,ou=people,o=concours","cn=roberto,ou=people,o=concours"])

SqlTest
-------

cookies
-------

password
--------
