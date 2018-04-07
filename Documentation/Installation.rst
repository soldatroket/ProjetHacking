############
Installation
############

Vous allé installé et configuré l'ensemble des composants permettant l'hébérgement du projet.

Voilà une liste qui définit toute les étapes : 

- `Ldap`_
- `Sql`_
- `Apache`_
- `Modules`_

  Vous allé donc voir l'ensemble de ces composants
  
---------------  

Ldap
====

Dans notre projet on utilise la Version 3 du protocol Ldap. 
  
Installation
------------  

  Ouvrez un terminal est installé le paquet suivant :
  
.. code-block:: shell
    :linenos:
   
    sudo apt-get install slapd
    sudo apt-get install ldap-utils
      

.. warning::
            Lors de l'installation de slapd vous allé ensuite être invité à rentré un mot de passe qui vous servira à configuré votre annuaire. Il est très important il ne faut pas l'oublié!
            
Démarrage
---------

    Pour Démarré votre annuaire il vous suffit de faire :
    
.. code-block:: shell
    :linenos:
          
    sudo service slapd start

--------------
       
Sql
===

  Installation
  ------------

  Ouvrez un terminal et inscrivez ceci :
    
.. code-block:: shell
    :linenos:
        
    sudo apt install mysql-server
          
.. warning::
    Vous allez ensuite être invité à rentré un mot de passe. Il est très important il ne faut pas l'oublié!
