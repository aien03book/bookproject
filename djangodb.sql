-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: djangodb
-- ------------------------------------------------------
-- Server version	5.7.19-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=117 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add category',7,'add_category'),(26,'Can change category',7,'change_category'),(27,'Can delete category',7,'delete_category'),(28,'Can view category',7,'view_category'),(29,'Can add product',8,'add_product'),(30,'Can change product',8,'change_product'),(31,'Can delete product',8,'delete_product'),(32,'Can view product',8,'view_product'),(33,'Can add members',9,'add_members'),(34,'Can change members',9,'change_members'),(35,'Can delete members',9,'delete_members'),(36,'Can view members',9,'view_members'),(37,'Can add board',10,'add_board'),(38,'Can change board',10,'change_board'),(39,'Can delete board',10,'delete_board'),(40,'Can view board',10,'view_board'),(41,'Can add members',11,'add_members'),(42,'Can change members',11,'change_members'),(43,'Can delete members',11,'delete_members'),(44,'Can view members',11,'view_members'),(45,'Can add post',12,'add_post'),(46,'Can change post',12,'change_post'),(47,'Can delete post',12,'delete_post'),(48,'Can view post',12,'view_post'),(49,'Can add feedback',13,'add_feedback'),(50,'Can change feedback',13,'change_feedback'),(51,'Can delete feedback',13,'delete_feedback'),(52,'Can view feedback',13,'view_feedback'),(53,'Can add todo',14,'add_todo'),(54,'Can change todo',14,'change_todo'),(55,'Can delete todo',14,'delete_todo'),(56,'Can view todo',14,'view_todo'),(57,'Can add auth group',15,'add_authgroup'),(58,'Can change auth group',15,'change_authgroup'),(59,'Can delete auth group',15,'delete_authgroup'),(60,'Can view auth group',15,'view_authgroup'),(61,'Can add auth group permissions',16,'add_authgrouppermissions'),(62,'Can change auth group permissions',16,'change_authgrouppermissions'),(63,'Can delete auth group permissions',16,'delete_authgrouppermissions'),(64,'Can view auth group permissions',16,'view_authgrouppermissions'),(65,'Can add auth permission',17,'add_authpermission'),(66,'Can change auth permission',17,'change_authpermission'),(67,'Can delete auth permission',17,'delete_authpermission'),(68,'Can view auth permission',17,'view_authpermission'),(69,'Can add auth user',18,'add_authuser'),(70,'Can change auth user',18,'change_authuser'),(71,'Can delete auth user',18,'delete_authuser'),(72,'Can view auth user',18,'view_authuser'),(73,'Can add auth user groups',19,'add_authusergroups'),(74,'Can change auth user groups',19,'change_authusergroups'),(75,'Can delete auth user groups',19,'delete_authusergroups'),(76,'Can view auth user groups',19,'view_authusergroups'),(77,'Can add auth user user permissions',20,'add_authuseruserpermissions'),(78,'Can change auth user user permissions',20,'change_authuseruserpermissions'),(79,'Can delete auth user user permissions',20,'delete_authuseruserpermissions'),(80,'Can view auth user user permissions',20,'view_authuseruserpermissions'),(81,'Can add bookpool',21,'add_bookpool'),(82,'Can change bookpool',21,'change_bookpool'),(83,'Can delete bookpool',21,'delete_bookpool'),(84,'Can view bookpool',21,'view_bookpool'),(85,'Can add django admin log',22,'add_djangoadminlog'),(86,'Can change django admin log',22,'change_djangoadminlog'),(87,'Can delete django admin log',22,'delete_djangoadminlog'),(88,'Can view django admin log',22,'view_djangoadminlog'),(89,'Can add django content type',23,'add_djangocontenttype'),(90,'Can change django content type',23,'change_djangocontenttype'),(91,'Can delete django content type',23,'delete_djangocontenttype'),(92,'Can view django content type',23,'view_djangocontenttype'),(93,'Can add django migrations',24,'add_djangomigrations'),(94,'Can change django migrations',24,'change_djangomigrations'),(95,'Can delete django migrations',24,'delete_djangomigrations'),(96,'Can view django migrations',24,'view_djangomigrations'),(97,'Can add django session',25,'add_djangosession'),(98,'Can change django session',25,'change_djangosession'),(99,'Can delete django session',25,'delete_djangosession'),(100,'Can view django session',25,'view_djangosession'),(101,'Can add bookcate',26,'add_bookcate'),(102,'Can change bookcate',26,'change_bookcate'),(103,'Can delete bookcate',26,'delete_bookcate'),(104,'Can view bookcate',26,'view_bookcate'),(105,'Can add todo',27,'add_todo'),(106,'Can change todo',27,'change_todo'),(107,'Can delete todo',27,'delete_todo'),(108,'Can view todo',27,'view_todo'),(109,'Can add bookpool',28,'add_bookpool'),(110,'Can change bookpool',28,'change_bookpool'),(111,'Can delete bookpool',28,'delete_bookpool'),(112,'Can view bookpool',28,'view_bookpool'),(113,'Can add bookrecord',29,'add_bookrecord'),(114,'Can change bookrecord',29,'change_bookrecord'),(115,'Can delete bookrecord',29,'delete_bookrecord'),(116,'Can view bookrecord',29,'view_bookrecord');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `boards`
--

DROP TABLE IF EXISTS `boards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `boards` (
  `boardid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`boardid`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `boards`
--

LOCK TABLES `boards` WRITE;
/*!40000 ALTER TABLE `boards` DISABLE KEYS */;
INSERT INTO `boards` VALUES (3,'人員服務態度'),(2,'圖書館環境'),(4,'書籍薦購'),(1,'硬體設備');
/*!40000 ALTER TABLE `boards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookpool`
--

DROP TABLE IF EXISTS `bookpool`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bookpool` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bookname` varchar(145) NOT NULL,
  `author` varchar(140) NOT NULL,
  `issuedate` date NOT NULL,
  `buydate` date DEFAULT NULL,
  `publisher` varchar(30) NOT NULL,
  `bookid` varchar(30) DEFAULT NULL,
  `ISBN` varchar(45) NOT NULL,
  `description` varchar(200) DEFAULT NULL,
  `bookimage` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookpool`
--

LOCK TABLES `bookpool` WRITE;
/*!40000 ALTER TABLE `bookpool` DISABLE KEYS */;
INSERT INTO `bookpool` VALUES (1,'精通 Python：運用簡單的套件進行現代運算','Sam Python','2019-09-05',NULL,'THU','B1','978-957-448-441-6','“本書是 Bill Lubanovic 的傑作，先為你紮下深厚的程式設計基礎，再教你使用大量 Python 工具箱處理現實生活中的問題，本書絕對適合學習如何運用 Python 來解決問題。”',NULL),(2,'Python','NEWBOOK','2002-06-06',NULL,'OXFORD','B2','978-957-448-441-6','1',NULL),(3,'JAVA','STE','2005-05-06',NULL,'CAM','B3','978-957-448-441-6','2',NULL),(4,'RUBY','TUBY','2019-06-30',NULL,'BEJ','B4','978-957-448-441-6','3',NULL),(5,'JS','SAM','2018-09-09',NULL,'THU','B5','978-957-448-441-6','4',NULL),(6,'Python2','PAA','2018-08-30',NULL,'PeeGE','B6','978-957-448-441-6','5',NULL),(7,'Tales Around the World. ','Candy Tang','2018-08-01',NULL,'佳音','B7','978-957-448-441-6','6',NULL),(8,'與父親的漫長告別: 男人的照護手記','盛田隆二著; 蘇文淑譯','2018-09-01',NULL,'時報文化','B8','978-957-13-7519-9','5',NULL),(9,'天使遊戲【遺忘書之墓系列】','卡洛斯．魯依斯．薩豐','2018-09-01',NULL,'圓神','B9','9789861336633',NULL,NULL),(10,'Fantastic Beasts - the Crimes of Grindelwald Fantastic Beasts: The Crimes of Grindelwald - The Original Screenplay (Harry Potter)','Rowling, J. K.， MinaLima (ILT)','2018-11-16',NULL,'Arthur a Levine','B10','9781338263893',NULL,NULL),(11,'Portable Medieval Reader','Ross, James Bruce (EDT)， McLaughlin, Mary Martin (EDT)','1977-05-01',NULL,'Penguin Classics','B11','9780140150469',NULL,NULL),(12,'Meditations','Marcus Aurelius, Emperor of Rome， Gregoire, Carolyn (FRW)','2018-01-02',NULL,'Baker & Taylor Books','B12','9781945186240',NULL,NULL),(13,'AI新世界: 中國、矽谷和AI七巨人如何引領全球發展 ','李開復','2018-08-01',NULL,'遠見天下文化出版股份有限公司','B13','2681646684007',NULL,'AIn_bWZDrCp.jpg'),(14,'Bad Blood: Secrets and Lies in a Silicon Valley Startup','約翰．凱瑞魯 John Carreyrou','2018-09-20',NULL,'商業周刊','B14','2681646684007',NULL,'636722515440167188_1Mj7lDk.jpg'),(15,'TED脫稿說話術: 學賈伯斯、歐巴馬的3堂即興幽默力! ','李真順','2018-08-08',NULL,'大樂文化有限公司','B15','2681610664004',NULL,'12345.jpg');
/*!40000 ALTER TABLE `bookpool` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookrecord`
--

DROP TABLE IF EXISTS `bookrecord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bookrecord` (
  `terms` int(11) NOT NULL AUTO_INCREMENT,
  `borrowtime` datetime(6) NOT NULL,
  `returntime` datetime(6) NOT NULL,
  `note` longtext NOT NULL,
  `bookid` int(11) NOT NULL,
  `memberid` int(11) NOT NULL,
  PRIMARY KEY (`terms`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookrecord`
--

LOCK TABLES `bookrecord` WRITE;
/*!40000 ALTER TABLE `bookrecord` DISABLE KEYS */;
INSERT INTO `bookrecord` VALUES (1,'2018-10-30 00:00:00.000000','2018-11-13 00:00:00.000000','111',123,333),(2,'2018-10-05 07:01:23.383450','2018-10-09 16:00:00.000000','',1,7),(3,'2018-10-05 07:10:12.424524','2018-10-09 16:00:00.000000','',5,10),(4,'2018-10-05 07:52:50.238015','2018-10-09 16:00:00.000000','',7,10),(5,'2018-10-08 01:23:29.965453','2018-10-09 16:00:00.000000','',7,11),(6,'2018-10-08 01:42:46.139245','2018-10-09 16:00:00.000000','',7,11),(7,'2018-10-08 02:39:33.204514','2018-12-04 16:00:00.000000','',7,11),(8,'2018-10-08 02:43:22.078468','2018-10-08 02:43:22.076457','',7,11),(9,'2018-10-08 02:46:23.807927','2018-12-07 02:46:23.804927','',3,11),(10,'2018-10-08 06:44:57.977106','2018-12-07 06:44:57.977106','',3,11),(11,'2018-10-08 10:56:23.808532','2018-12-07 10:56:23.808532','',14,7),(12,'2018-10-08 11:15:44.513328','2018-12-07 11:15:44.513328','',14,7),(13,'2018-10-08 11:19:43.082013','2018-12-07 11:19:43.082013','',14,7),(14,'2018-10-08 11:25:55.019593','2018-12-07 11:25:55.019593','',3,7),(15,'2018-10-08 11:26:59.791512','2018-12-07 11:26:59.791512','',3,7),(16,'2018-10-08 11:27:02.012986','2018-12-07 11:27:02.012986','',3,7),(17,'2018-10-08 11:50:05.901716','2018-12-07 11:50:05.901716','',3,7),(18,'2018-10-08 11:51:26.549791','2018-12-07 11:51:26.549791','',3,7),(19,'2018-10-08 12:17:28.207484','2018-12-07 12:17:28.207484','',3,7),(20,'2018-10-08 12:18:18.187911','2018-12-07 12:18:18.187911','',10,7),(21,'2018-10-08 12:20:08.077767','2018-12-07 12:20:08.077767','',3,7),(22,'2018-10-08 12:20:54.765857','2018-12-07 12:20:54.765857','',10,7),(23,'2018-10-08 12:21:35.371387','2018-12-07 12:21:35.371387','',7,7),(24,'2018-10-08 12:22:52.816479','2018-12-07 12:22:52.816479','',6,7),(25,'2018-10-08 12:23:46.646033','2018-12-07 12:23:46.646033','',5,7),(26,'2018-10-08 12:25:21.025181','2018-12-07 12:25:21.025181','',3,7),(27,'2018-10-08 12:25:49.464273','2018-12-07 12:25:49.464273','',3,7),(28,'2018-10-08 12:26:17.289237','2018-12-07 12:26:17.289237','',3,7),(29,'2018-10-08 12:26:50.583253','2018-12-07 12:26:50.583253','',10,7),(30,'2018-10-08 12:27:24.829924','2018-12-07 12:27:24.829924','',10,7),(31,'2018-10-08 12:29:56.986135','2018-12-07 12:29:56.986135','',10,7),(32,'2018-10-08 12:30:49.261171','2018-12-07 12:30:49.261171','',10,7),(33,'2018-10-08 12:30:51.401252','2018-12-07 12:30:51.401252','',10,7),(34,'2018-10-08 12:32:09.285570','2018-12-07 12:32:09.285570','',10,7),(35,'2018-10-08 12:32:44.213489','2018-12-07 12:32:44.213489','',3,7),(36,'2018-10-08 12:33:53.537367','2018-12-07 12:33:53.537367','',3,7),(37,'2018-10-08 12:36:14.401680','2018-12-07 12:36:14.401680','',3,7),(38,'2018-10-08 12:37:03.341328','2018-12-07 12:37:03.341328','',3,7),(39,'2018-10-08 12:37:29.809022','2018-12-07 12:37:29.809022','',10,7),(40,'2018-10-08 12:37:40.312638','2018-12-07 12:37:40.312638','',10,7),(41,'2018-10-08 12:37:41.657599','2018-12-07 12:37:41.657599','',10,7),(42,'2018-10-08 12:38:19.468943','2018-12-07 12:38:19.468943','',10,7),(43,'2018-10-08 12:38:35.001052','2018-12-07 12:38:35.001052','',10,7),(44,'2018-10-08 12:38:48.553035','2018-12-07 12:38:48.553035','',10,7),(45,'2018-10-08 12:47:59.331372','2018-12-07 12:47:59.331372','',10,7),(46,'2018-10-09 01:12:07.555633','2018-12-08 01:12:07.555633','',7,7),(47,'2018-10-09 01:24:06.707640','2018-12-08 01:24:06.707640','',7,7),(48,'2018-10-08 16:00:00.000000','2018-12-07 16:00:00.000000','',6,17),(49,'2018-10-08 16:00:00.000000','2018-12-07 16:00:00.000000','',6,17);
/*!40000 ALTER TABLE `bookrecord` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categories` (
  `categoryid` int(11) NOT NULL AUTO_INCREMENT,
  `categoryname` varchar(45) NOT NULL,
  PRIMARY KEY (`categoryid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `conferance_conferoom`
--

DROP TABLE IF EXISTS `conferance_conferoom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `conferance_conferoom` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `num` varchar(5) NOT NULL,
  `img` varchar(5) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conferance_conferoom`
--

LOCK TABLES `conferance_conferoom` WRITE;
/*!40000 ALTER TABLE `conferance_conferoom` DISABLE KEYS */;
INSERT INTO `conferance_conferoom` VALUES (1,'1','1'),(2,'2','2');
/*!40000 ALTER TABLE `conferance_conferoom` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `conferance_order`
--

DROP TABLE IF EXISTS `conferance_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `conferance_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` date NOT NULL,
  `room_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `conferance_order_room_id_7e2780d1_fk_conferance_conferoom_id` (`room_id`),
  KEY `conferance_order_user_id_4939c175_fk_auth_user_id` (`user_id`),
  CONSTRAINT `conferance_order_room_id_7e2780d1_fk_conferance_conferoom_id` FOREIGN KEY (`room_id`) REFERENCES `conferance_conferoom` (`id`),
  CONSTRAINT `conferance_order_user_id_4939c175_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conferance_order`
--

LOCK TABLES `conferance_order` WRITE;
/*!40000 ALTER TABLE `conferance_order` DISABLE KEYS */;
/*!40000 ALTER TABLE `conferance_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(10,'boards','board'),(11,'boards','members'),(12,'boards','post'),(28,'bookbor','bookpool'),(29,'bookbor','bookrecord'),(5,'contenttypes','contenttype'),(13,'feedback','feedback'),(15,'home','authgroup'),(16,'home','authgrouppermissions'),(17,'home','authpermission'),(18,'home','authuser'),(19,'home','authusergroups'),(20,'home','authuseruserpermissions'),(26,'home','bookcate'),(21,'home','bookpool'),(22,'home','djangoadminlog'),(23,'home','djangocontenttype'),(24,'home','djangomigrations'),(25,'home','djangosession'),(27,'home','todo'),(9,'member','members'),(6,'sessions','session'),(7,'store','category'),(8,'store','product'),(14,'todo','todo');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-09-19 12:28:45.300712'),(2,'auth','0001_initial','2018-09-19 12:28:49.629058'),(3,'admin','0001_initial','2018-09-19 12:28:50.443511'),(4,'admin','0002_logentry_remove_auto_add','2018-09-19 12:28:50.443511'),(5,'admin','0003_logentry_add_action_flag_choices','2018-09-19 12:28:50.459138'),(6,'contenttypes','0002_remove_content_type_name','2018-09-19 12:28:51.256004'),(7,'auth','0002_alter_permission_name_max_length','2018-09-19 12:28:51.646639'),(8,'auth','0003_alter_user_email_max_length','2018-09-19 12:28:51.974748'),(9,'auth','0004_alter_user_username_opts','2018-09-19 12:28:51.990390'),(10,'auth','0005_alter_user_last_login_null','2018-09-19 12:28:52.256019'),(11,'auth','0006_require_contenttypes_0002','2018-09-19 12:28:52.318556'),(12,'auth','0007_alter_validators_add_error_messages','2018-09-19 12:28:52.365430'),(13,'auth','0008_alter_user_username_max_length','2018-09-19 12:28:52.923044'),(14,'auth','0009_alter_user_last_name_max_length','2018-09-19 12:28:53.235548'),(15,'boards','0001_initial','2018-09-19 12:28:54.563672'),(16,'member','0001_initial','2018-09-19 12:28:54.563672'),(17,'sessions','0001_initial','2018-09-19 12:28:54.938726'),(18,'store','0001_initial','2018-09-19 12:28:55.799628'),(20,'member','0002_auto_20180917_1914','2018-09-20 01:25:01.832429'),(21,'store','0002_product','2018-09-20 01:25:01.848104'),(22,'store','0003_auto_20180911_1413','2018-09-20 01:25:01.848104'),(23,'todo','0001_initial','2018-09-20 06:29:25.540214'),(24,'boards','0002_remove_board_description','2018-09-25 12:53:34.005912'),(25,'boards','0003_auto_20180925_2053','2018-09-25 12:53:34.022915'),(26,'MeetingRoom','0001_initial','2018-10-09 03:55:01.519726'),(27,'boards','0004_auto_20181001_2059','2018-10-09 03:55:01.535354'),(28,'home','0001_initial','2018-10-09 03:55:01.535354'),(29,'home','0002_bookcate','2018-10-09 03:55:01.535354'),(30,'home','0003_todo','2018-10-09 03:55:01.582260'),(31,'member','0002_auto_20181004_1756','2018-10-09 03:55:01.613516'),(32,'member','0003_auto_20181009_1153','2018-10-09 03:55:01.613516'),(33,'bookbor','0001_initial','2018-10-09 04:11:59.482017');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('ltx3zshkr6jod10eiz5s49826qbvq1ju','ZmQ0NDIwMTIyMTlmN2JiNWYzMDk1Y2FiYzdlZTBlMzA2ZjA0NTAxMDp7ImNhcHRjaGEiOiJGNjREMSJ9','2018-10-11 07:35:37.877930'),('n45122amjo3z3zdn36h46evlzf7wou27','YzcwNDA3NjY2MDZhYzk5MjU0NWQ3MGQzZWU1ZDFkYmU5ZWQ4ZTdkMTp7ImNhcHRjaGEiOiJGQUNCNiJ9','2018-10-25 01:08:41.836745');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `members`
--

DROP TABLE IF EXISTS `members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `members` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(45) NOT NULL,
  `age` int(11) DEFAULT NULL,
  `memberid` varchar(45) DEFAULT NULL,
  `joindate` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members`
--

LOCK TABLES `members` WRITE;
/*!40000 ALTER TABLE `members` DISABLE KEYS */;
INSERT INTO `members` VALUES (1,'Laven','Laven@gmail','1234',15,NULL,NULL),(2,'Kyle','Kyle@gmail','1234',16,NULL,NULL),(7,'Tina','Tina@gmail','12345',15,'M10709','2018-10-04 00:00:00'),(10,'Merry','merry@gmail.com','13515',35,'M10701','2018-10-04 00:00:00'),(11,'Tom','Tom@gmail.com','123456',15,'M10702','2018-10-04 00:00:00'),(12,'Joanna','Joanna@hotmail.com','abc',20,'M10703','2018-10-04 00:00:00'),(13,'Heidi','Heidi@gmail.com','sdf',1234,'M10704','2018-10-04 00:00:00'),(14,'Geoge','geoge@gmail.com','123456',15,'M10705','2018-10-04 00:00:00'),(15,'Rose','Rose@gmail','111',13,'M10706','2018-10-04 00:00:00'),(16,'Jay','Jay@gmail.com','Jayy',36,'M10707','2018-10-04 00:00:00'),(17,'Scott','Scott@gmail','1234',11,'M10710','2018-10-04 00:00:00'),(18,'Hito','Hito@gmail','1127',12,NULL,NULL);
/*!40000 ALTER TABLE `members` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `posts` (
  `postid` int(11) NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `createdat` datetime(6) NOT NULL,
  `boardid` int(11) NOT NULL,
  `memberid` int(11) DEFAULT NULL,
  PRIMARY KEY (`postid`),
  KEY `posts_boardid_baa749e8_fk_boards_boardid` (`boardid`),
  KEY `posts_memberid_08221fa3_fk_members_id` (`memberid`)
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
INSERT INTO `posts` VALUES (54,'5678','2018-10-04 01:52:56.546290',1,2),(55,'1321','2018-10-04 09:07:23.826400',2,2),(56,'1234','2018-10-04 09:51:38.124618',3,2),(69,'hahhaa','2018-10-08 12:51:32.305759',3,1),(70,'o hi yo','2018-10-08 12:51:42.675566',4,1),(71,'test123','2018-10-09 02:19:37.356867',2,1),(73,'1234','2018-10-09 04:05:53.507995',3,17),(78,'5678','2018-10-09 07:09:57.790464',3,17),(79,'123','2018-10-09 07:52:50.119440',3,17);
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products` (
  `productid` int(11) NOT NULL AUTO_INCREMENT,
  `modelnumber` varchar(45) NOT NULL,
  `modelname` varchar(45) NOT NULL,
  `productimage` varchar(45) NOT NULL,
  `unitcost` int(11) NOT NULL,
  `description` varchar(300) NOT NULL,
  `categoryid` int(11) NOT NULL,
  PRIMARY KEY (`productid`),
  KEY `products_categoryid_dd8a17ec_fk_categories_categoryid` (`categoryid`),
  CONSTRAINT `products_categoryid_dd8a17ec_fk_categories_categoryid` FOREIGN KEY (`categoryid`) REFERENCES `categories` (`categoryid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `todo`
--

DROP TABLE IF EXISTS `todo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `todo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `text` longtext NOT NULL,
  `last_modified_at` datetime(6) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `todo`
--

LOCK TABLES `todo` WRITE;
/*!40000 ALTER TABLE `todo` DISABLE KEYS */;
INSERT INTO `todo` VALUES (1,'firstpost','test567','2018-10-03 02:41:16.519745','2018-09-20 07:11:27.797523'),(7,'465','46546','2018-10-03 02:39:53.314251','2018-10-03 02:39:47.667575');
/*!40000 ALTER TABLE `todo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-11 13:48:58
