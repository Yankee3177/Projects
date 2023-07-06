CREATE DATABASE  IF NOT EXISTS `nutritionapp` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `nutritionapp`;
-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: nutritionapp
-- ------------------------------------------------------
-- Server version	8.0.27

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
-- Table structure for table `recipes`
--

DROP TABLE IF EXISTS `recipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recipes` (
  `recipeId` int NOT NULL AUTO_INCREMENT,
  `recipeName` char(50) DEFAULT NULL,
  `ingredients` longtext,
  `servings` int NOT NULL,
  `calories` int NOT NULL,
  `instructions` longtext,
  `userRecipe` int NOT NULL,
  PRIMARY KEY (`recipeId`),
  KEY `userIdFK` (`userRecipe`),
  CONSTRAINT `userIdFK` FOREIGN KEY (`userRecipe`) REFERENCES `users` (`userId`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes`
--

LOCK TABLES `recipes` WRITE;
/*!40000 ALTER TABLE `recipes` DISABLE KEYS */;
INSERT INTO `recipes` VALUES (1,'Chicken and White rice','Chicken,White Rice,Salt,Pepper,Olive Oil',2,301,'Rinse rice before cooking.Boil 2 cups of water for 1 cup of rice,add 1 tsp of Salt and Oil. Once water is boiling put temperature down to low and cover the rice. Wait 20 min and the rice is done. Put salt and pepper on the chicken and put in the oven at 325 F for 15 min.',1),(2,'Baked Chicken Tacos','Olive oil,Chicken,Taco Seasoning,onion,tomato,Green Chiles,Taco Shells,Refried beans,Mexican bland cheese',10,1000,'Preheat oven to 400F. Spray a 9×13 baking dish with nonstick spray.Heat 1 tablespoon olive oil over medium heat in a medium skillet.Add 1/2 cup onion to skillet and cook for 2-3 minutes, or until the onion is translucent\n and fragrant.Stir in the chicken, 1 ounce taco seasoning, tomatoes (FULLY DRAINED), and 1 can green chiles (FULLY  DRAINED) *see note. Stir to combine fully. Reduce to simmer and allow to cook for 5-8 minutes.Place the taco\n shells in the baking dish, standing up. I was able to fit 10 taco shells in the dish by adding 2 on each side.Bake the taco shells for 5 minutes by themselves to allow them to crisp up. Remove from the oven.Spoon 1 tablespoon\n of beans into the bottom of each taco shell. Top with the chicken mixture, almost to the top of each shell.Sprinkle each shell generously with shredded cheese, the more the better!Bake for 7-10 minutes or until cheese is fully \n melted and the edges of the shells are browned.',1),(4,'White rice','1 Cups of white rice',2,300,'Boil 2 cups of water and rice. Once boiling cover,set temperature to low and wait 20 min. ',1),(5,'Chicken','chicken',2,500,'cut chicken',5);
/*!40000 ALTER TABLE `recipes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `userId` int NOT NULL AUTO_INCREMENT,
  `userName` char(25) NOT NULL,
  `userPass` char(50) DEFAULT NULL,
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Yankee Cruz','123456'),(3,'Kayla Holbrook','123456'),(4,'Adam','123456'),(5,'yankee','03232001');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-06 16:34:47
