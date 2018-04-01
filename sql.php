<?php
$bdd=new PDO('mysql:host=localhost;dbname=concours;charset=utf8','root','lolotte');
if(isset($_GET['id']) && is_numeric($_GET['id']) && $_COOKIE['status']=="admin"){
	$id=htmlspecialchars($_GET['id']);
	$requete=$bdd->exec("DELETE FROM enigmes WHERE id = '".$id."'");
	if($requete==1){
	header("refresh:5;url=administration.py?type=enigme");
	?>
	<html>
	<head>
		<meta http-equiv="content-type" content="text/html; charset=UTF-8">
	</head>
	<body>
		<h1>L'énigme numéro <?php echo $id; ?> a bien était supprimer</h1>
		<h3>Vous allez être rediriger dans 5 secondes</h3>
	</body>
	</html>
	<?php
	}
}elseif(isset($_POST['type']) && $_POST['type']=="addenigme" && $_COOKIE['status']=="admin"){
	try{
	$titre=htmlspecialchars($_POST['title']);
	$questions=htmlspecialchars($_POST['answer']);
	$reponse=sha1(htmlspecialchars($_POST['reponse']));
	$difficulter=htmlspecialchars($_POST['strenght']);
	$categorie=htmlspecialchars($_POST['cat']);
	$requete=$bdd->prepare('INSERT INTO enigmes(Titre, Question, Reponse, Catégorie, Point, Fichier) VALUES(?, ?, ?, ?, ?, NULL)');
	$requete->bindValue(1, $titre, PDO::PARAM_STR);
	$requete->bindValue(2, $questions, PDO::PARAM_STR);
	$requete->bindValue(3, $reponse, PDO::PARAM_STR);
	$requete->bindValue(4, $categorie, PDO::PARAM_STR);
	$requete->bindValue(5, $difficulter, PDO::PARAM_INT);
	$requete->execute();
	header("refresh:5;url=administration.py?type=addenigme");
	?>
        <html>
        <head>
                <meta http-equiv="content-type" content="text/html; charset=UTF-8">
        </head>
        <body>
                <h1>Votre énigme a bien était rajouter</h1>
                <h3>Vous allez être rediriger dans 5 secondes</h3>
        </body>
        </html>
<?php
	}catch(PDOException $e){
		echo "ERREUR".$e->getmessage();
	}
}
?>
