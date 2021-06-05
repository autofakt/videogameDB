-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: videogamedb
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `games`
--

DROP TABLE IF EXISTS `games`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `games` (
  `gid` int NOT NULL AUTO_INCREMENT,
  `title` varchar(45) NOT NULL,
  `platform` varchar(45) NOT NULL,
  `price` float DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  PRIMARY KEY (`gid`),
  UNIQUE KEY `gid_UNIQUE` (`gid`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `games`
--

LOCK TABLES `games` WRITE;
/*!40000 ALTER TABLE `games` DISABLE KEYS */;
INSERT INTO `games` VALUES (1,'FIFA 2021',' PS4',14.99,1),(2,'CounterStrike',' Xbox One',9.99,3),(3,'Dota 2',' PC',8.99,2),(4,'Apex',' PC',14.99,2),(5,'Diablo 2: Resurrected',' PC',4.99,7),(6,'League of Legends',' PC',7.99,4),(7,'World of Warcraft',' PC',12.88,5),(8,'Overwatch',' PC',5.99,3),(9,'RuneScape',' PC',9.99,5),(10,'Farming Simulator 2021',' PC',7.99,8),(11,'Pokemon Go',' Switch',9.99,1),(13,'Red Dead Redemption 2',' PS4',19.99,6),(14,'Cyberpunk',' PS5',17.99,3),(15,'Witcher 3',' PS4',11.99,1),(16,'Sim City 4',' PC',10.99,3),(17,'Tracktor Sim',' PC',4.99,2),(18,'Eve',' PC',8.99,4),(20,'Madden',' PS5',9.99,7),(21,'Portal 4',' PS5',6.99,6),(22,'Star Wars',' Xbox One',12.99,3),(23,'Mario Cart',' Switch',4.99,15);
/*!40000 ALTER TABLE `games` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-16 10:38:08
