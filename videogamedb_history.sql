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
-- Table structure for table `history`
--

DROP TABLE IF EXISTS `history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `history` (
  `hid` int NOT NULL AUTO_INCREMENT,
  `cid` int DEFAULT NULL,
  `bid` int DEFAULT NULL,
  `gid` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `price` float DEFAULT NULL,
  `orderTotal` float DEFAULT NULL,
  `date` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`hid`),
  KEY `cid_idx` (`cid`),
  KEY `bid_idx` (`bid`),
  KEY `gid_idx` (`gid`),
  CONSTRAINT `bid` FOREIGN KEY (`bid`) REFERENCES `bank` (`bid`),
  CONSTRAINT `cid2` FOREIGN KEY (`cid`) REFERENCES `customer` (`cid`),
  CONSTRAINT `gid2` FOREIGN KEY (`gid`) REFERENCES `games` (`gid`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='					';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `history`
--

LOCK TABLES `history` WRITE;
/*!40000 ALTER TABLE `history` DISABLE KEYS */;
INSERT INTO `history` VALUES (1,2,10,8,1,5.99,36.96,'2021-05-01 20:18:34.280336'),(2,2,10,10,1,7.99,36.96,'2021-05-01 20:18:34.280336'),(3,2,10,14,1,17.99,36.96,'2021-05-01 20:18:34.280336'),(4,2,10,5,1,4.99,36.96,'2021-05-01 20:18:34.280336'),(5,2,11,15,1,11.99,67.96,'2021-05-01 20:23:28.842885'),(6,2,11,13,1,19.99,67.96,'2021-05-01 20:23:28.842885'),(7,2,11,14,2,35.98,67.96,'2021-05-01 20:23:28.842885'),(8,1,9,10,1,7.99,20.97,'2021-05-15 07:38:46.488543'),(9,1,9,10,1,7.99,20.97,'2021-05-15 07:38:46.488543'),(10,1,9,5,1,4.99,20.97,'2021-05-15 07:38:46.488543'),(11,2,10,18,1,8.99,29.97,'2021-05-15 08:11:11.586643'),(12,2,10,15,1,11.99,29.97,'2021-05-15 08:11:11.586643'),(13,2,10,18,1,8.99,29.97,'2021-05-15 08:11:11.586643'),(14,2,11,9,1,9.99,63.95,'2021-05-15 12:43:02.484919'),(15,2,11,13,1,19.99,63.95,'2021-05-15 12:43:02.484919'),(16,2,11,14,1,17.99,63.95,'2021-05-15 12:43:02.484919'),(17,2,11,10,2,15.98,63.95,'2021-05-15 12:43:02.484919'),(18,2,10,10,1,7.99,7.99,'2021-05-15 12:46:18.914062'),(19,2,10,3,1,8.99,8.99,'2021-05-15 12:46:55.209090'),(20,2,10,9,1,9.99,9.99,'2021-05-15 13:11:45.294947'),(21,2,10,11,1,9.99,9.99,'2021-05-15 13:20:39.320526');
/*!40000 ALTER TABLE `history` ENABLE KEYS */;
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