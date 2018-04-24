###############
Préinstallation
###############

Vous allez installer et configurer l'ensemble des composants permettant l'hébérgement du projet.

.. contents:: liste des différentes étapes : 
   :depth: 2
  
---------------  

Ldap
====

Dans notre projet on utilise la **Version 3** du protocol Ldap.
Aide pour l'installation : https://doc.ubuntu-fr.org/slapd
 
 

Installation
------------  

  Ouvrez un terminal est installer le paquet suivant :
  
.. code-block:: shell
    :linenos:
   
    sudo apt-get install slapd
    sudo apt-get install ldap-utils
      

.. warning::
            Lors de l'installation de slapd vous allez être invité à rentrer un mot de passe qui vous servira à configurer votre annuaire. Il est très important il ne faut pas l'oublié!
            
Une fois l'annuaire installé vous allez devoir le remplir, pour ce faire vous devez tout d'abord créer une nouvelle base.
J'ai mit à disposition le fichier d'une base qui se trouve dans BaseLdap/DB.LDIF. Il vous restera ensuite plus qu'a éxecuter la commande si dessous afin de l'y ajouter.

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

  Ouvrez un terminal et inscrivez ceci pour lancer l'installation de votre server MySQL :
    
.. code-block:: shell
    :linenos:
        
    sudo apt install mysql-server
          
.. warning::
    Vous allez ensuite être invité à rentrer un mot de passe. Il est très important il ne faut pas l'oublié!
    
Une fois votre base mySQL installée je vous conseille d'installer par la suite le module `phpmyadmin`_.
Vous allez ensuite devoir créer deux nouvelles bases de données : **concours** et **equipes**
Vous trouverez ensuite dans le dossier BaseSQL un fichier nommé concours.sql, il contient l'ensemble des tables par défaut pour la table concours. Vous allez devoir l'importer via phpmyadmin.
(**concours -> Import -> Fichier à importer -> concours.sql**)

Démarrage
---------

    Pour Démarrer votre serveur il vous suffit de faire :
    
.. code-block:: shell
    :linenos:
          
    sudo service mysql start
    
----------------

Apache
======

  Nous allons utiliser la derniére version d'apache : **2.7**
  Aide pour l'installation : https://doc.ubuntu-fr.org/apache
  


Installation
------------

  Ouvrez un terminal et inscrivez ceci pour lancer l'installation de votre serveur apache :
    
.. code-block:: shell
    :linenos:
        
    sudo apt install mysql-server
    
Une fois apache installé il faut lui authoriser l'éxécution de script python pour ce faire suivez les différentes étapes présentes dans la documentation technique.
    


Démarrage
---------

.. note:: Par défaut, le serveur apache se lance automatiquement lors de son installation mais aussi à l'allumage de la machine.

Pour démarrer le serveur rentrez ceci dans un terminal :
  
.. code-block:: shell
    :linenos:
    
    sudo service apache2 start
    
.. note:: Si votre serveur à bien démarré vous devriez avoir une page d'acceuil qui s'affiche en tapant *127.0.0.1* ou *localhost* dans un navigateur

---------------------

Modules
=======

phpmyadmin
----------

   Le module phpmyamdin nous permettra d'amdinistrer la base mySQL par interface graphique.
   
   Aide pour l'installation : https://doc.ubuntu-fr.org/phpmyadmin
   
   Pour installer ce module vous devez tout d'abord avoir installé la base mySQL. Ensuite vous devez inscrire ceci dans un terminal:
   
.. code-block:: shell
    :linenos:
    
    sudo apt-get install phpmyadmin
    
.. seealso:: Vous aurez besoin içi du mot de passe de votre base mySQL!

Une fois phpmyadmin installé vous devriez pouvoir y accéder via *127.0.0.1/phpmyadmin* ou *localhost/phpmyadmin*
   
   
