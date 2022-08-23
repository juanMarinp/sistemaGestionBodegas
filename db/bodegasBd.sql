-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Aug 23, 2022 at 03:13 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bodegasBd`
--

-- --------------------------------------------------------

--
-- Table structure for table `AUTOR`
--

CREATE TABLE `AUTOR` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `AUTOR`
--

INSERT INTO `AUTOR` (`ID`, `NOMBRE`) VALUES
(1, 'ISAAC ASIMOV'),
(2, 'EDGAR ALLAN POE'),
(3, 'ERNESTO SABATO'),
(4, 'SPINOZA'),
(5, 'DESCARTES'),
(6, 'STEPHEN KING');

-- --------------------------------------------------------

--
-- Table structure for table `AUTOR_PRODUCTO`
--

CREATE TABLE `AUTOR_PRODUCTO` (
  `ID_PRODUCTO` varchar(30) NOT NULL,
  `ID_AUTOR` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `AUTOR_PRODUCTO`
--

INSERT INTO `AUTOR_PRODUCTO` (`ID_PRODUCTO`, `ID_AUTOR`) VALUES
('1212AB', 1),
('4435JJ', 1),
('4545TT', 3);

-- --------------------------------------------------------

--
-- Table structure for table `BODEGA`
--

CREATE TABLE `BODEGA` (
  `ID` int(11) NOT NULL,
  `CALLE` varchar(30) NOT NULL,
  `ID_COMUNA` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `BODEGA`
--

INSERT INTO `BODEGA` (`ID`, `CALLE`, `ID_COMUNA`) VALUES
(1, 'Los Copihues 1565', 1),
(2, 'Las Carmelias 334', 2),
(3, 'Los presidentes 8584', 3),
(4, 'Los Consejales 345', 3),
(5, 'los obeliscos 999', 2),
(6, 'las camarera 444', 1),
(7, 'las calles falsas 123', 2);

-- --------------------------------------------------------

--
-- Table structure for table `CARGO`
--

CREATE TABLE `CARGO` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `CARGO`
--

INSERT INTO `CARGO` (`ID`, `NOMBRE`) VALUES
(1, 'ADMIN'),
(2, 'JEFE'),
(3, 'BODEGUERO');

-- --------------------------------------------------------

--
-- Table structure for table `COMUNA`
--

CREATE TABLE `COMUNA` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `COMUNA`
--

INSERT INTO `COMUNA` (`ID`, `NOMBRE`) VALUES
(1, 'LO PRADO'),
(2, 'SANTIGO'),
(3, 'ÑUÑOA');

-- --------------------------------------------------------

--
-- Table structure for table `DOCUMENTO_MOVIMIENTO`
--

CREATE TABLE `DOCUMENTO_MOVIMIENTO` (
  `ID` int(11) NOT NULL,
  `BODEGA_ORIGEN` int(11) NOT NULL,
  `BODEGA_DESTINO` int(11) NOT NULL,
  `ID_PRODUCTO` varchar(30) NOT NULL,
  `CANTIDAD` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `EDITORIAL`
--

CREATE TABLE `EDITORIAL` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(30) NOT NULL,
  `CALLE` varchar(30) NOT NULL,
  `ID_COMUNA` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `EDITORIAL`
--

INSERT INTO `EDITORIAL` (`ID`, `NOMBRE`, `CALLE`, `ID_COMUNA`) VALUES
(1, 'GALAXIA', 'BANDERA 2526', 2);

-- --------------------------------------------------------

--
-- Table structure for table `EMPLEADO`
--

CREATE TABLE `EMPLEADO` (
  `RUT` char(10) NOT NULL,
  `NOMBRE` varchar(30) NOT NULL,
  `APELLIDO` varchar(30) NOT NULL,
  `RUT_JEFE` char(10) DEFAULT NULL,
  `ID_BODEGA` int(11) NOT NULL,
  `USUARIO` varchar(30) NOT NULL,
  `CONTRASENIA` varchar(110) DEFAULT NULL,
  `ID_CARGO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `EMPLEADO`
--

INSERT INTO `EMPLEADO` (`RUT`, `NOMBRE`, `APELLIDO`, `RUT_JEFE`, `ID_BODEGA`, `USUARIO`, `CONTRASENIA`, `ID_CARGO`) VALUES
('20560123-1', 'Juan', 'Gonzales', NULL, 1, 'admin', '$2b$12$BPLqzNlRpyQtmViNsix8huZe28V9bQVvY4oezmlLeT7HgxgSNH5uu', 1),
('7546609-9', 'Jose', 'Milei', '9300029-3', 2, 'josemilei333', '$2b$12$034e5cV7tXfqrWIT3FSgVeXzssloMANJ64rcLjLaUQQvXPyBfZJPW', 3),
('9300029-3', 'Ricardo', 'Fort', NULL, 2, 'ricardofort123', '$2b$12$UvvJ0YoRzdkeHTnkO2yD9uiWhZ6C1Lmsb6hnNlZVqeOmUS4of11pW', 2);

-- --------------------------------------------------------

--
-- Table structure for table `PRODUCTO`
--

CREATE TABLE `PRODUCTO` (
  `ID` varchar(30) NOT NULL,
  `ID_TIPO` int(11) NOT NULL,
  `ID_EDITORIAL` int(11) NOT NULL,
  `DESCRIPCION` varchar(100) DEFAULT NULL,
  `TITULO` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `PRODUCTO`
--

INSERT INTO `PRODUCTO` (`ID`, `ID_TIPO`, `ID_EDITORIAL`, `DESCRIPCION`, `TITULO`) VALUES
('1212AB', 1, 1, 'Libro de programacion', 'Clean Code'),
('4435JJ', 1, 1, 'libro de literatura', 'Las caminatas nocturnas'),
('4545TT', 1, 1, 'Libro de literatura', 'Los caballos');

-- --------------------------------------------------------

--
-- Table structure for table `PRODUCTO_BODEGA`
--

CREATE TABLE `PRODUCTO_BODEGA` (
  `ID_PRODUCTO` varchar(30) NOT NULL,
  `ID_BODEGA` int(11) NOT NULL,
  `CANTIDAD` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `PRODUCTO_BODEGA`
--

INSERT INTO `PRODUCTO_BODEGA` (`ID_PRODUCTO`, `ID_BODEGA`, `CANTIDAD`) VALUES
('1212AB', 1, 20),
('1212AB', 2, 20),
('1212AB', 3, 15);

-- --------------------------------------------------------

--
-- Table structure for table `TIPO_PRODUCTO`
--

CREATE TABLE `TIPO_PRODUCTO` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `TIPO_PRODUCTO`
--

INSERT INTO `TIPO_PRODUCTO` (`ID`, `NOMBRE`) VALUES
(1, 'LIBRO'),
(2, 'REVISTA'),
(3, 'ENCICLOPEDIA');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `AUTOR`
--
ALTER TABLE `AUTOR`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `AUTOR_PRODUCTO`
--
ALTER TABLE `AUTOR_PRODUCTO`
  ADD PRIMARY KEY (`ID_PRODUCTO`,`ID_AUTOR`),
  ADD KEY `FK_A_AUTOR_PRODUCTO` (`ID_AUTOR`);

--
-- Indexes for table `BODEGA`
--
ALTER TABLE `BODEGA`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `FK_COMUNA_BODEGA` (`ID_COMUNA`);

--
-- Indexes for table `CARGO`
--
ALTER TABLE `CARGO`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `COMUNA`
--
ALTER TABLE `COMUNA`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `DOCUMENTO_MOVIMIENTO`
--
ALTER TABLE `DOCUMENTO_MOVIMIENTO`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `FK_BODEGA_ORIGEN` (`BODEGA_ORIGEN`),
  ADD KEY `FK_BODEGA_DESTINO` (`BODEGA_DESTINO`),
  ADD KEY `FK_PRODUCTO_MOVIMIENTO` (`ID_PRODUCTO`);

--
-- Indexes for table `EDITORIAL`
--
ALTER TABLE `EDITORIAL`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `FK_COMUNA` (`ID_COMUNA`);

--
-- Indexes for table `EMPLEADO`
--
ALTER TABLE `EMPLEADO`
  ADD PRIMARY KEY (`RUT`),
  ADD KEY `FK_JEFE_EMPLEADO` (`RUT_JEFE`),
  ADD KEY `FK_BODEGA_EMPLEADO` (`ID_BODEGA`),
  ADD KEY `FK_CARGO_EMPLEADO` (`ID_CARGO`);

--
-- Indexes for table `PRODUCTO`
--
ALTER TABLE `PRODUCTO`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `FK_TIPO_PRODUCTO` (`ID_TIPO`),
  ADD KEY `FK_EDITORIAL_PRODUCTO` (`ID_EDITORIAL`);

--
-- Indexes for table `PRODUCTO_BODEGA`
--
ALTER TABLE `PRODUCTO_BODEGA`
  ADD PRIMARY KEY (`ID_PRODUCTO`,`ID_BODEGA`),
  ADD KEY `FK_BODEGA_PB` (`ID_BODEGA`);

--
-- Indexes for table `TIPO_PRODUCTO`
--
ALTER TABLE `TIPO_PRODUCTO`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `AUTOR`
--
ALTER TABLE `AUTOR`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `BODEGA`
--
ALTER TABLE `BODEGA`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `CARGO`
--
ALTER TABLE `CARGO`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `COMUNA`
--
ALTER TABLE `COMUNA`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `DOCUMENTO_MOVIMIENTO`
--
ALTER TABLE `DOCUMENTO_MOVIMIENTO`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `EDITORIAL`
--
ALTER TABLE `EDITORIAL`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `TIPO_PRODUCTO`
--
ALTER TABLE `TIPO_PRODUCTO`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `AUTOR_PRODUCTO`
--
ALTER TABLE `AUTOR_PRODUCTO`
  ADD CONSTRAINT `FK_A_AUTOR_PRODUCTO` FOREIGN KEY (`ID_AUTOR`) REFERENCES `AUTOR` (`ID`),
  ADD CONSTRAINT `FK_P_AUTOR_PRODUCTO` FOREIGN KEY (`ID_PRODUCTO`) REFERENCES `PRODUCTO` (`ID`);

--
-- Constraints for table `BODEGA`
--
ALTER TABLE `BODEGA`
  ADD CONSTRAINT `FK_COMUNA_BODEGA` FOREIGN KEY (`ID_COMUNA`) REFERENCES `COMUNA` (`ID`);

--
-- Constraints for table `DOCUMENTO_MOVIMIENTO`
--
ALTER TABLE `DOCUMENTO_MOVIMIENTO`
  ADD CONSTRAINT `FK_BODEGA_DESTINO` FOREIGN KEY (`BODEGA_DESTINO`) REFERENCES `BODEGA` (`ID`),
  ADD CONSTRAINT `FK_BODEGA_ORIGEN` FOREIGN KEY (`BODEGA_ORIGEN`) REFERENCES `BODEGA` (`ID`),
  ADD CONSTRAINT `FK_PRODUCTO_MOVIMIENTO` FOREIGN KEY (`ID_PRODUCTO`) REFERENCES `PRODUCTO` (`ID`);

--
-- Constraints for table `EDITORIAL`
--
ALTER TABLE `EDITORIAL`
  ADD CONSTRAINT `FK_COMUNA` FOREIGN KEY (`ID_COMUNA`) REFERENCES `COMUNA` (`ID`);

--
-- Constraints for table `EMPLEADO`
--
ALTER TABLE `EMPLEADO`
  ADD CONSTRAINT `FK_BODEGA_EMPLEADO` FOREIGN KEY (`ID_BODEGA`) REFERENCES `BODEGA` (`ID`),
  ADD CONSTRAINT `FK_CARGO_EMPLEADO` FOREIGN KEY (`ID_CARGO`) REFERENCES `CARGO` (`ID`),
  ADD CONSTRAINT `FK_JEFE_EMPLEADO` FOREIGN KEY (`RUT_JEFE`) REFERENCES `EMPLEADO` (`RUT`);

--
-- Constraints for table `PRODUCTO`
--
ALTER TABLE `PRODUCTO`
  ADD CONSTRAINT `FK_EDITORIAL_PRODUCTO` FOREIGN KEY (`ID_EDITORIAL`) REFERENCES `EDITORIAL` (`ID`),
  ADD CONSTRAINT `FK_TIPO_PRODUCTO` FOREIGN KEY (`ID_TIPO`) REFERENCES `TIPO_PRODUCTO` (`ID`);

--
-- Constraints for table `PRODUCTO_BODEGA`
--
ALTER TABLE `PRODUCTO_BODEGA`
  ADD CONSTRAINT `FK_BODEGA_PB` FOREIGN KEY (`ID_BODEGA`) REFERENCES `BODEGA` (`ID`),
  ADD CONSTRAINT `FK_PRODUCTO_PB` FOREIGN KEY (`ID_PRODUCTO`) REFERENCES `PRODUCTO` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
