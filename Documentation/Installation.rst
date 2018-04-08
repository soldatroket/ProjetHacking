###############
Préinstallation
###############

Vous allez installé et configuré l'ensemble des composants permettant l'hébérgement du projet.

.. contents:: liste des différentes étapes : 
   :depth: 2
  
---------------  

Ldap
====

Dans notre projet on utilise la **Version 3** du protocol Ldap.
Aide pour l'installation : https://doc.ubuntu-fr.org/slapd
 
 

Installation
------------  

  Ouvrez un terminal est installé le paquet suivant :
  
.. code-block:: shell
    :linenos:
   
    sudo apt-get install slapd
    sudo apt-get install ldap-utils
      

.. warning::
            Lors de l'installation de slapd vous allez ensuite être invité à rentré un mot de passe qui vous servira à configuré votre annuaire. Il est très important il ne faut pas l'oublié!
            
Une fois l'annuaire installé vous allez devoir le remplir, pour ce faire vous devez tout d'abord créer une nouvelle base.
J'ai mit à disposition le fichier d'une base qui se trouve dans BaseLdap/DB.LDIF. Il vous restera ensuite plus qu'a éxecuté le commande si dessous afin de l'y ajouté.

.. code-block:: shell
    :linenos:
          
    sudo ldapadd -Y EXTERNAL -H ldapi:/// -f <Votre fichier>
    
Quand vous aurez crée votre base, il faudrat y mettre les noeuds principaux du projet qui ce trouve dans le fichier BaseLdap/NoeudPrincipal.LDIF, ajouter le fichier grâce à la commande : 

.. code-block:: shell
    :linenos:
          
    sudo ldapadd -D "cn=admin, o=concours" -h 127.0.0.1 -W -f NoeudPrincipal.LDIF
           

:Remplissage d'exemple:           
  Une fois les noeuds crées j'ai un fichier exemple qui remplit l'ensemble de ces noeuds avec un IUT et un Administrateur. Vous pouvez aussi la remplir via le fichier dans BaseLdap/Exemple.LDIF en faisant : 
  
.. code-block:: shell
    :linenos:
          
    sudo ldapadd -D "cn=admin, o=concours" -h 127.0.0.1 -W -f Exemple.LDIF
    

  
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



Installation
------------

  Ouvrez un terminal et inscrivez ceci pour lancé l'installation de votre server MySQL :
    
.. code-block:: shell
    :linenos:
        
    sudo apt install mysql-server
          
.. warning::
    Vous allez ensuite être invité à rentré un mot de passe. Il est très important il ne faut pas l'oublié!
    
    Une fois votre base mySQL installé je vous conseille d'installé par la suite le module `phpmyadmin`_. 
    


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
  


Installation
------------

  Ouvrez un terminal et inscrivez ceci pour lancé l'installation de votre serveur apache :
    
.. code-block:: shell
    :linenos:
        
    sudo apt install mysql-server
    


Démarrage
---------

.. note:: Par défaut, le serveur apache se lance automatiquement lors de son installation mais aussi à l'allumage de la machine.

Pour démarré le serveur rentré ceci dans un terminal :
  
.. code-block:: shell
    :linenos:
    
    sudo service apache2 start
    
.. note:: Si votre serveur à bien démarré vous devriez avoir une page d'acceuil qui s'affiche en tapant *127.0.0.1* dans un navigateur

---------------------

Modules
=======

phpmyadmin
----------

   Le module phpmyamdin nous permettra d'amdinistrer la base mySQL par interface graphique.
   
   Aide pour l'installation : https://doc.ubuntu-fr.org/phpmyadmin
   
   Pour installé ce module vous devez tout d'abord avoir installé la base mySQL. Ensuite vous devez inscrire ceci dans un terminal:
   
.. code-block:: shell
    :linenos:
    
    sudo apt-get install phpmyadmin
    
.. seealso:: Vous aurez besoin içi du mot de passe de votre base mySQL!
   
   
