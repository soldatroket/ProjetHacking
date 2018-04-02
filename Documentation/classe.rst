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
   :param list(str) retrievAttributes: Tableau contenant le nom des attributs recherchés
   :return: Un tableau ou une chaine de caractére
   :rtype: list(str) or str
   
.. warning:: Pour pouvoir utilisé les paramétres de recherches Ldap, vous devez tout d'abord importé le module **ldap**
   
   **Exemple :** 
   
   .. code-block:: python
      :linenos:
   
      LdapObj=LdapTest.Connection("cn=admin,o=concours","toto")

   
SqlTest
-------

cookies
-------

password
--------
