-- --------------------------------------------------------
-- Host:                         
-- Server version:               8.0.25 - Source distribution
-- Server OS:                    Linux
-- HeidiSQL Version:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for db_membership
CREATE DATABASE IF NOT EXISTS db_membership/*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE db_membership

-- Dumping structure for table db_membership.tbl_certs
CREATE TABLE IF NOT EXISTS `tbl_certs` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `CertID` varchar(50) NOT NULL,
  `MemberID` varchar(50) NOT NULL,
  `Issued` date NOT NULL,
  `Expires` date NOT NULL,
  `Description` varchar(500) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `CertID` (`CertID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Data exporting was unselected.

-- Dumping structure for table db_membership.tbl_members
CREATE TABLE IF NOT EXISTS `tbl_members` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `MemberID` varchar(50) NOT NULL,
  `Image` varchar(50) DEFAULT NULL,
  `SurName` varchar(50) NOT NULL,
  `OtherNames` varchar(50) NOT NULL,
  `Gender` varchar(1) NOT NULL,
  `NationalID` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `MemberID` (`MemberID`,`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Data exporting was unselected.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
