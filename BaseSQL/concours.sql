-- phpMyAdmin SQL Dump
-- version 4.6.6deb4
-- https://www.phpmyadmin.net/
--
-- Client :  localhost:3306
-- Généré le :  Dim 08 Avril 2018 à 19:08
-- Version du serveur :  5.7.20-0ubuntu0.17.04.1
-- Version de PHP :  7.0.22-0ubuntu0.17.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `concours`
--

-- --------------------------------------------------------

--
-- Structure de la table `AdminToken`
--

CREATE TABLE `AdminToken` (
  `Name` varchar(255) NOT NULL,
  `Token` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Contenu de la table `AdminToken`
--

INSERT INTO `AdminToken` (`Name`, `Token`) VALUES
('adminm2m', 946984543);

-- --------------------------------------------------------

--
-- Structure de la table `categorie`
--

CREATE TABLE `categorie` (
  `IDcat` int(255) NOT NULL,
  `NomCat` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `categorie`
--

INSERT INTO `categorie` (`IDcat`, `NomCat`) VALUES
(2, 'Crypto'),
(3, 'forensics'),
(1, 'Hacking');

-- --------------------------------------------------------

--
-- Structure de la table `enigmes`
--

CREATE TABLE `enigmes` (
  `ID` int(11) NOT NULL,
  `Titre` varchar(100) NOT NULL,
  `Question` varchar(1000) NOT NULL,
  `Reponse` varchar(1000) NOT NULL,
  `Catégorie` varchar(100) NOT NULL,
  `Point` int(20) NOT NULL,
  `Fichier` varchar(1000) DEFAULT NULL,
  `owner` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `questiontype`
--

CREATE TABLE `questiontype` (
  `ID` int(11) NOT NULL,
  `Nom` varchar(100) NOT NULL,
  `Point` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `questiontype`
--

INSERT INTO `questiontype` (`ID`, `Nom`, `Point`) VALUES
(1, 'Facile', 3),
(2, 'Moyen', 7),
(3, 'Difficile', 15);

-- --------------------------------------------------------

--
-- Structure de la table `resetmdp`
--

CREATE TABLE `resetmdp` (
  `token` varchar(100) NOT NULL,
  `mail` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `resetmdp`
--

INSERT INTO `resetmdp` (`token`, `mail`) VALUES
('LnNsTjntKU', 'test@test.test'),
('WXRjVMBALH', 'Test.test@test.tesst'),
('pBuU8GbNXY', 'Test.test@test.tesst'),
('igyhS0mlXh', 'Test.test@test.tesst'),
('rRJsbbEb6d', 'Test.test@test.tesst'),
('jQHDRBDjgP', 'dr@dret.lo'),
('V5Sj1Wp2C6', 'dr@dret.loe'),
('bzsbDWWehF', 'mze.Ff@gg.fr'),
('ATwq7LYWnQ', 'zerez.llz@gg.fr'),
('H4RW07iIe1', 'ljjkl.looi@yiy.fr'),
('ok', 'ok@ok.com'),
('w6dUE5lKeX', 'paul@yopmail.com'),
('0fqGTEkqRW', 'jj@yopmail.com'),
('wPORW5oa5o', 'jj@yopmail.com'),
('6Cq8HjNAIF', 'alexis@yopmail.com'),
('CCGQFR4hbj', 'raoul@yopmail.com');

--
-- Index pour les tables exportées
--

--
-- Index pour la table `AdminToken`
--
ALTER TABLE `AdminToken`
  ADD UNIQUE KEY `UniqueAdminToken` (`Name`,`Token`);

--
-- Index pour la table `categorie`
--
ALTER TABLE `categorie`
  ADD PRIMARY KEY (`IDcat`),
  ADD KEY `NomCat` (`NomCat`);

--
-- Index pour la table `enigmes`
--
ALTER TABLE `enigmes`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Point` (`Point`),
  ADD KEY `Catégorie` (`Catégorie`);

--
-- Index pour la table `questiontype`
--
ALTER TABLE `questiontype`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Point` (`Point`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `categorie`
--
ALTER TABLE `categorie`
  MODIFY `IDcat` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT pour la table `enigmes`
--
ALTER TABLE `enigmes`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=82;
--
-- AUTO_INCREMENT pour la table `questiontype`
--
ALTER TABLE `questiontype`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `enigmes`
--
ALTER TABLE `enigmes`
  ADD CONSTRAINT `CatEnigme` FOREIGN KEY (`Catégorie`) REFERENCES `categorie` (`NomCat`),
  ADD CONSTRAINT `PointEnigme` FOREIGN KEY (`Point`) REFERENCES `questiontype` (`Point`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
