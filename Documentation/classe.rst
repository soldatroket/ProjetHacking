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

   Cette fonction est utilisé uniquement par le script lui même.
   Elle permet d'initialisé une connection avec un annuaire Ldap et retourne un objet **LdapObject**

   
SqlTest
-------

cookies
-------

password
--------
