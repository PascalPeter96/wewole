-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 26, 2024 at 11:00 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `wewoleloans`
--

-- --------------------------------------------------------

--
-- Table structure for table `borrowers`
--

CREATE TABLE `borrowers` (
  `brower_id` int(11) NOT NULL,
  `fullname` varchar(250) NOT NULL,
  `address` varchar(250) NOT NULL,
  `occupation` varchar(250) NOT NULL,
  `salary` float NOT NULL,
  `deposits` float NOT NULL,
  `contact` varchar(250) NOT NULL,
  `next_kin` varchar(200) NOT NULL,
  `relationship` varchar(250) NOT NULL,
  `kin_contact` varchar(250) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `borrowers`
--

INSERT INTO `borrowers` (`brower_id`, `fullname`, `address`, `occupation`, `salary`, `deposits`, `contact`, `next_kin`, `relationship`, `kin_contact`, `group_id`) VALUES
(1, 'Hamid kalanzi', 'Gayaza', 'IT', 30000, 399800, '0773456567', 'Ham', '', '77777777', 1),
(2, 'James Oluka', 'kawempe', 'IT', 60000, 0, '0773456567', 'Jimmy', '', '77777777', 1);

-- --------------------------------------------------------

--
-- Table structure for table `groups`
--

CREATE TABLE `groups` (
  `group_id` int(11) NOT NULL,
  `group_name` varchar(250) NOT NULL,
  `g_address` varchar(250) NOT NULL,
  `number` varchar(250) NOT NULL,
  `gcontact` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `groups`
--

INSERT INTO `groups` (`group_id`, `group_name`, `g_address`, `number`, `gcontact`) VALUES
(1, 'Bugagga', 'Kawaala', '10', '0772788654');

-- --------------------------------------------------------

--
-- Table structure for table `loans`
--

CREATE TABLE `loans` (
  `loan_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `amount` float NOT NULL,
  `interest` float NOT NULL,
  `rate` float NOT NULL,
  `total` float NOT NULL,
  `paid` float NOT NULL,
  `duration` varchar(250) NOT NULL,
  `monthly` float NOT NULL,
  `balance` float NOT NULL,
  `due_date` date NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `loans`
--

INSERT INTO `loans` (`loan_id`, `date`, `amount`, `interest`, `rate`, `total`, `paid`, `duration`, `monthly`, `balance`, `due_date`, `group_id`) VALUES
(1, '2024-02-26', 500000, 20, 100000, 600000, 6000, '3', 200000, 594000, '2024-02-29', 1);

-- --------------------------------------------------------

--
-- Table structure for table `payment_records`
--

CREATE TABLE `payment_records` (
  `Pay_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `paid` float NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `payment_records`
--

INSERT INTO `payment_records` (`Pay_id`, `date`, `paid`, `group_id`) VALUES
(1, '2024-02-22', 300000, 4),
(2, '2024-02-22', 100000, 4),
(4, '2024-02-26', 6000, 1);

-- --------------------------------------------------------

--
-- Table structure for table `savings`
--

CREATE TABLE `savings` (
  `saving_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `deposit` float NOT NULL,
  `banked` varchar(250) NOT NULL,
  `brower_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `savings`
--

INSERT INTO `savings` (`saving_id`, `date`, `deposit`, `banked`, `brower_id`) VALUES
(3, '2024-02-22', 60000, '0', 1),
(4, '2024-02-22', 50000, '0', 1),
(5, '2024-02-22', 500000, 'hamk', 1),
(6, '2024-02-22', 1000000, 'James', 2),
(7, '2024-02-22', 600000, 'hamk', 4),
(8, '2024-02-22', 600000, 'James', 2),
(9, '2024-02-22', 600000, 'hamk', 1),
(10, '2024-02-22', 20000, 'Benjamin', 6),
(11, '2024-02-22', 500000, 'hamk', 1),
(12, '2024-02-22', 50000, 'hamk', 1),
(13, '2024-02-22', 1000000, 'hamk', 7),
(14, '2024-02-22', 2000000, 'James', 5),
(15, '2024-02-22', 500000, 'hamk', 7),
(16, '2024-02-26', 400000, 'hamk', 1);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL,
  `name` varchar(250) NOT NULL,
  `username` varchar(250) NOT NULL,
  `password` varchar(250) NOT NULL,
  `retype` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `name`, `username`, `password`, `retype`) VALUES
(1, 'hamid', 'hamk', '8cb2237d0679ca88db6464eac60da96345513964', '12345'),
(2, 'jack meli', 'ham', 'pbkdf2:sha256:260000$rwDwaAHaaA3ERxPX$a59faaa48384e2f7dd7612ed07edc4eba9603f87b4637983b3dae5709f090376', '');

-- --------------------------------------------------------

--
-- Table structure for table `withdrawal`
--

CREATE TABLE `withdrawal` (
  `with_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `withdrawal_amount` float NOT NULL,
  `brower_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `withdrawal`
--

INSERT INTO `withdrawal` (`with_id`, `date`, `withdrawal_amount`, `brower_id`) VALUES
(1, '2024-02-22', 500000, 1),
(2, '2024-02-22', 1000000, 2),
(3, '2024-02-22', 200000, 2),
(4, '2024-02-22', 10000, 6),
(5, '2024-02-22', 4000000, 1),
(7, '2024-02-26', 200, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `borrowers`
--
ALTER TABLE `borrowers`
  ADD PRIMARY KEY (`brower_id`),
  ADD KEY `relationship` (`relationship`,`kin_contact`),
  ADD KEY `salary` (`salary`,`contact`,`next_kin`),
  ADD KEY `brower_id` (`brower_id`,`fullname`,`address`,`occupation`),
  ADD KEY `deposit` (`deposits`),
  ADD KEY `group_id` (`group_id`);

--
-- Indexes for table `groups`
--
ALTER TABLE `groups`
  ADD PRIMARY KEY (`group_id`),
  ADD KEY `group_id` (`group_id`,`group_name`,`g_address`),
  ADD KEY `number` (`number`,`gcontact`);

--
-- Indexes for table `loans`
--
ALTER TABLE `loans`
  ADD PRIMARY KEY (`loan_id`),
  ADD KEY `monthly` (`monthly`,`due_date`,`group_id`),
  ADD KEY `interest` (`interest`,`total`,`duration`),
  ADD KEY `loan_id` (`loan_id`,`amount`),
  ADD KEY `date` (`date`),
  ADD KEY `rate` (`rate`),
  ADD KEY `balance` (`balance`),
  ADD KEY `paid` (`paid`);

--
-- Indexes for table `payment_records`
--
ALTER TABLE `payment_records`
  ADD PRIMARY KEY (`Pay_id`),
  ADD KEY `Pay_id` (`Pay_id`,`paid`),
  ADD KEY `brower_id` (`group_id`),
  ADD KEY `date` (`date`);

--
-- Indexes for table `savings`
--
ALTER TABLE `savings`
  ADD PRIMARY KEY (`saving_id`),
  ADD KEY `saving_id` (`saving_id`,`date`,`deposit`,`banked`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `user_id` (`user_id`,`name`),
  ADD KEY `userame` (`username`,`password`,`retype`);

--
-- Indexes for table `withdrawal`
--
ALTER TABLE `withdrawal`
  ADD PRIMARY KEY (`with_id`),
  ADD KEY `with_id` (`with_id`,`date`,`withdrawal_amount`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `borrowers`
--
ALTER TABLE `borrowers`
  MODIFY `brower_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `groups`
--
ALTER TABLE `groups`
  MODIFY `group_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `loans`
--
ALTER TABLE `loans`
  MODIFY `loan_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `payment_records`
--
ALTER TABLE `payment_records`
  MODIFY `Pay_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `savings`
--
ALTER TABLE `savings`
  MODIFY `saving_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `withdrawal`
--
ALTER TABLE `withdrawal`
  MODIFY `with_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
