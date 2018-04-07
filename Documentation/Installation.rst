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

Dans notre projet on utilise la **Version 3** du protocol Ldap.
Aide pour l'installation : https://doc.ubuntu-fr.org/slapd
  
------------------  
  
Installation
------------  

  Ouvrez un terminal est installé le paquet suivant :
  
.. code-block:: shell
    :linenos:
   
    sudo apt-get install slapd
    sudo apt-get install ldap-utils
      

.. warning::
            Lors de l'installation de slapd vous allé ensuite être invité à rentré un mot de passe qui vous servira à configuré votre annuaire. Il est très important il ne faut pas l'oublié!
           
------------------           
           
Démarrage
---------

    Pour Démarré votre annuaire il vous suffit de faire :
    
.. code-block:: shell
    :linenos:
          
    sudo service slapd start

--------------
       
Sql
===

Aide pour l'installation : https://doc.ubuntu-fr.org/mysql

--------------

Installation
------------

  Ouvrez un terminal et inscrivez ceci pour lancé l'installation de votre server MySQL :
    
.. code-block:: shell
    :linenos:
        
    sudo apt install mysql-server
          
.. warning::
    Vous allez ensuite être invité à rentré un mot de passe. Il est très important il ne faut pas l'oublié!
    
---------------

Démarrage
---------

    Pour Démarré votre annuaire il vous suffit de faire :
    
.. code-block:: shell
    :linenos:
          
    sudo service mysql start
    
----------------

Apache
======

  Nous allons utilisé la derniére version d'apache : **2.7**
  Aide pour l'installation : https://doc.ubuntu-fr.org/apache
  
-------------------

Installation
------------

  Ouvrez un terminal et inscrivez ceci pour lancé l'installation de votre server apache :
    
.. code-block:: shell
    :linenos:
        
    sudo apt install mysql-server
    
------------------

Démarrage
---------

.. note:: Par défaut, le serveur apache se lance automatiquement lors de son installation mais aussi à l'allumage de la machine.

Pour démarré le serveur rentré ceci dans un terminal :
  
.. code-block:: shell
    :linenos:
    
    sudo service apache2 start
    
.. note:: Si votre serveur est bien démarré vous devriez avoir une page d'acceuil qui s'affiche en tapant *127.0.0.1* dans un navigateur
