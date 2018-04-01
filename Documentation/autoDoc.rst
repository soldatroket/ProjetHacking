************ 
Premiere page 
************* 

Package 
******* 

Utils
=====
Le packetage Utils contient un ensemble de scripts permettant entre autre de communiquer avec la **base SQL**, **annuaire Ldap**, **Lecture/Ecriture de cookies**, **Gestion mot de passe**.

Pour pouvoir utilisé une des classes des fichiers suivants : 

-**ldapp.py**

-**sql.py**

-**cookies.py**

-**password.py**.

Vous devez tout d’abord importer le Package nommé « **Utils** » qui vous importera l’ensemble de ces scripts. En inscrivant uniquement cette commande en début de script :

.. code-block:: python
   :linenos:   
      
      import Utils

Une fois ceci fait vous pouvez appellez l'ensemble des classes de ces fichiers.


Template
========
Le packetage « **Template** » contient des scripts de template pour les pages HTML

Pour pouvoir utilisés l'un de ces templates vous devez tout d'abord l'importer en faisant : 

.. code-block:: python
   :linenos:
   
      import Template
