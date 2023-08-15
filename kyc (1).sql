-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 15, 2023 at 04:45 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kyc`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add contact', 7, 'add_contact'),
(26, 'Can change contact', 7, 'change_contact'),
(27, 'Can delete contact', 7, 'delete_contact'),
(28, 'Can view contact', 7, 'view_contact'),
(29, 'Can add person', 8, 'add_person'),
(30, 'Can change person', 8, 'change_person'),
(31, 'Can delete person', 8, 'delete_person'),
(32, 'Can view person', 8, 'view_person'),
(33, 'Can add income', 9, 'add_income'),
(34, 'Can change income', 9, 'change_income'),
(35, 'Can delete income', 9, 'delete_income'),
(36, 'Can view income', 9, 'view_income'),
(37, 'Can add family', 10, 'add_family'),
(38, 'Can change family', 10, 'change_family'),
(39, 'Can delete family', 10, 'delete_family'),
(40, 'Can view family', 10, 'view_family'),
(41, 'Can add address', 11, 'add_address'),
(42, 'Can change address', 11, 'change_address'),
(43, 'Can delete address', 11, 'delete_address'),
(44, 'Can view address', 11, 'view_address'),
(45, 'Can add captcha store', 12, 'add_captchastore'),
(46, 'Can change captcha store', 12, 'change_captchastore'),
(47, 'Can delete captcha store', 12, 'delete_captchastore'),
(48, 'Can view captcha store', 12, 'view_captchastore'),
(49, 'Can add municipality', 13, 'add_municipality'),
(50, 'Can change municipality', 13, 'change_municipality'),
(51, 'Can delete municipality', 13, 'delete_municipality'),
(52, 'Can view municipality', 13, 'view_municipality'),
(53, 'Can add province', 14, 'add_province'),
(54, 'Can change province', 14, 'change_province'),
(55, 'Can delete province', 14, 'delete_province'),
(56, 'Can view province', 14, 'view_province'),
(57, 'Can add district', 15, 'add_district'),
(58, 'Can change district', 15, 'change_district'),
(59, 'Can delete district', 15, 'delete_district'),
(60, 'Can view district', 15, 'view_district');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$lSlNf19YxjT7KusAKiKcqp$hO5h9wjmQQJLGXAePKa5I6VfT/GEfbarhBpp6qi4EgI=', '2023-08-07 05:02:06.492306', 1, 'admin', '', '', '', 1, 1, '2023-08-07 05:01:53.497254');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `captcha_captchastore`
--

CREATE TABLE `captcha_captchastore` (
  `id` int(11) NOT NULL,
  `challenge` varchar(32) NOT NULL,
  `response` varchar(32) NOT NULL,
  `hashkey` varchar(40) NOT NULL,
  `expiration` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `captcha_captchastore`
--

INSERT INTO `captcha_captchastore` (`id`, `challenge`, `response`, `hashkey`, `expiration`) VALUES
(1, 'FLCD', 'flcd', '5c83c59f730a8fe5ac04f5f1e1920caaf144523a', '2023-08-03 13:24:34.160693'),
(2, 'CWHM', 'cwhm', 'bb22957447faabd2f0501add4927c9ddadd7cd77', '2023-08-03 13:41:56.781724'),
(3, 'OEQF', 'oeqf', 'a94b6e3429e621516583a4e4a80ae95d2b006118', '2023-08-03 13:49:18.288175'),
(4, 'VMUC', 'vmuc', '27c35b48aaaa78265861d91832fc64d46a691a20', '2023-08-04 05:25:11.316399'),
(5, 'ZJLU', 'zjlu', 'e530dbd26a3a3288c8ebf15acf410972bc90cf2c', '2023-08-04 06:43:14.284313'),
(6, 'NERW', 'nerw', '124048a87e92a413de1466ee4b488eb299708f1e', '2023-08-04 07:47:51.012788'),
(7, 'KZRB', 'kzrb', '85c4da177e4cca7917c5aa50c90b10a51de1c9b6', '2023-08-05 03:38:44.259045');

-- --------------------------------------------------------

--
-- Table structure for table `djangonepal_district`
--

CREATE TABLE `djangonepal_district` (
  `id` bigint(20) NOT NULL,
  `district` varchar(100) NOT NULL,
  `province_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `djangonepal_municipality`
--

CREATE TABLE `djangonepal_municipality` (
  `id` bigint(20) NOT NULL,
  `municipality` varchar(200) NOT NULL,
  `district_id` bigint(20) NOT NULL,
  `province_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `djangonepal_province`
--

CREATE TABLE `djangonepal_province` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-08-07 05:08:15.346414', '1', 'Person object (1)', 1, '[{\"added\": {}}]', 8, 1),
(2, '2023-08-07 05:12:53.912521', '2', 'Family details for Yubraj', 1, '[{\"added\": {}}]', 10, 1),
(3, '2023-08-07 05:13:41.629030', '1', 'Income details for Yubraj', 1, '[{\"added\": {}}]', 9, 1),
(4, '2023-08-07 05:14:38.190612', '1', 'permanent Address for Yubraj', 1, '[{\"added\": {}}]', 11, 1),
(5, '2023-08-07 05:15:57.390652', '2', 'temporary Address for Yubraj', 1, '[{\"added\": {}}]', 11, 1),
(6, '2023-08-09 06:11:12.386521', '2', 'Person object (2)', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 8, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(12, 'captcha', 'captchastore'),
(5, 'contenttypes', 'contenttype'),
(15, 'djangonepal', 'district'),
(13, 'djangonepal', 'municipality'),
(14, 'djangonepal', 'province'),
(11, 'know', 'address'),
(7, 'know', 'contact'),
(10, 'know', 'family'),
(9, 'know', 'income'),
(8, 'know', 'person'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-08-03 13:19:17.468444'),
(2, 'auth', '0001_initial', '2023-08-03 13:19:17.778108'),
(3, 'admin', '0001_initial', '2023-08-03 13:19:17.850816'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-08-03 13:19:17.861640'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-08-03 13:19:17.869783'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-08-03 13:19:17.912925'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-08-03 13:19:17.957290'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-08-03 13:19:17.969330'),
(9, 'auth', '0004_alter_user_username_opts', '2023-08-03 13:19:17.976720'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-08-03 13:19:18.008677'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-08-03 13:19:18.012869'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-08-03 13:19:18.019789'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-08-03 13:19:18.041979'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-08-03 13:19:18.060916'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-08-03 13:19:18.073873'),
(16, 'auth', '0011_update_proxy_permissions', '2023-08-03 13:19:18.080217'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-08-03 13:19:18.094137'),
(18, 'captcha', '0001_initial', '2023-08-03 13:19:18.114214'),
(19, 'captcha', '0002_alter_captchastore_id', '2023-08-03 13:19:18.121570'),
(20, 'know', '0001_initial', '2023-08-03 13:19:18.278885'),
(21, 'sessions', '0001_initial', '2023-08-03 13:19:18.300872'),
(22, 'know', '0002_person_email_person_number', '2023-08-03 17:32:35.638206'),
(23, 'know', '0003_person_other_card_back_person_other_card_front', '2023-08-03 17:51:21.293614'),
(24, 'djangonepal', '0001_initial', '2023-08-04 04:01:24.422983'),
(25, 'know', '0004_address_l_image', '2023-08-04 04:51:15.671435'),
(26, 'know', '0005_alter_person_middlename_alter_person_other_card_and_more', '2023-08-06 15:54:59.404683'),
(27, 'know', '0006_alter_person_back_photo_alter_person_front_photo_and_more', '2023-08-09 05:14:57.847014'),
(28, 'know', '0007_alter_person_back_photo_alter_person_front_photo_and_more', '2023-08-10 04:03:23.522261');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('1vc2f13z7cuhliwndiwnirjtjqvxndze', '.eJxVjDsOwjAQBe_iGln-JV5T0nMGy95d4wBypDipEHeHSCmgfTPzXiKmba1x67zEicRZaHH63XLCB7cd0D212yxxbusyZbkr8qBdXmfi5-Vw_w5q6vVbswoBgvZgPRNYw1zYDc5ZMDQgaXCmjIiZdS7KKjcGNlgIVNbFG3Ti_QHXRDfk:1qSsNa:IaAiNcOcxXKuxtWrmnTvB1N7SiBbUDMpQQBfu7c9Ujw', '2023-08-21 05:02:06.499629');

-- --------------------------------------------------------

--
-- Table structure for table `know_address`
--

CREATE TABLE `know_address` (
  `id` bigint(20) NOT NULL,
  `address_type` varchar(10) NOT NULL,
  `zone` varchar(40) NOT NULL,
  `provience` varchar(50) NOT NULL,
  `district` varchar(75) NOT NULL,
  `muni_vdc` varchar(75) NOT NULL,
  `house_no` varchar(10) NOT NULL,
  `ward_no` varchar(10) NOT NULL,
  `street` varchar(100) NOT NULL,
  `tel_n0` varchar(10) NOT NULL,
  `post_box` varchar(20) NOT NULL,
  `person_id` bigint(20) NOT NULL,
  `l_image` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `know_contact`
--

CREATE TABLE `know_contact` (
  `id` bigint(20) NOT NULL,
  `name` varchar(250) NOT NULL,
  `email` varchar(100) NOT NULL,
  `subject` varchar(100) NOT NULL,
  `number` varchar(10) NOT NULL,
  `message` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `know_family`
--

CREATE TABLE `know_family` (
  `id` bigint(20) NOT NULL,
  `f_relation` varchar(100) NOT NULL,
  `f_fullname` varchar(100) NOT NULL,
  `f_remarks` varchar(150) NOT NULL,
  `person_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `know_income`
--

CREATE TABLE `know_income` (
  `id` bigint(20) NOT NULL,
  `organization` varchar(60) NOT NULL,
  `address` varchar(100) NOT NULL,
  `designation` varchar(20) NOT NULL,
  `person_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `know_person`
--

CREATE TABLE `know_person` (
  `id` bigint(20) NOT NULL,
  `firstname` varchar(250) NOT NULL,
  `middlename` varchar(255) NOT NULL,
  `lastname` varchar(255) NOT NULL,
  `image` varchar(100) NOT NULL,
  `fathername` varchar(255) NOT NULL,
  `grandfather` varchar(255) NOT NULL,
  `dateofbirth` date NOT NULL,
  `gender` varchar(50) NOT NULL,
  `married_status` varchar(50) NOT NULL,
  `pannum` varchar(20) NOT NULL,
  `nationality` varchar(50) NOT NULL,
  `citizenshipnumber` varchar(50) NOT NULL,
  `citizen_issued_district` varchar(50) NOT NULL,
  `citizen_issued_date` date NOT NULL,
  `front_photo` varchar(100) NOT NULL,
  `back_photo` varchar(100) NOT NULL,
  `passport_number` varchar(20) NOT NULL,
  `passport_issued_date` date NOT NULL,
  `passport_issued_place` varchar(100) NOT NULL,
  `pass_front_photo` varchar(100) NOT NULL,
  `pass_back_photo` varchar(100) NOT NULL,
  `other_card` varchar(100) NOT NULL,
  `other_card_number` varchar(20) NOT NULL,
  `other_card_issued_date` date NOT NULL,
  `other_card_issued_authority` varchar(100) NOT NULL,
  `email` varchar(25) NOT NULL,
  `number` varchar(10) NOT NULL,
  `other_card_back` varchar(100) NOT NULL,
  `other_card_front` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `captcha_captchastore`
--
ALTER TABLE `captcha_captchastore`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `hashkey` (`hashkey`);

--
-- Indexes for table `djangonepal_district`
--
ALTER TABLE `djangonepal_district`
  ADD PRIMARY KEY (`id`),
  ADD KEY `djangonepal_district_province_id_fce96d02_fk_djangonep` (`province_id`);

--
-- Indexes for table `djangonepal_municipality`
--
ALTER TABLE `djangonepal_municipality`
  ADD PRIMARY KEY (`id`),
  ADD KEY `djangonepal_municipa_district_id_f305c35c_fk_djangonep` (`district_id`),
  ADD KEY `djangonepal_municipa_province_id_ec09542b_fk_djangonep` (`province_id`);

--
-- Indexes for table `djangonepal_province`
--
ALTER TABLE `djangonepal_province`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `know_address`
--
ALTER TABLE `know_address`
  ADD PRIMARY KEY (`id`),
  ADD KEY `know_address_person_id_848eb147_fk_know_person_id` (`person_id`);

--
-- Indexes for table `know_contact`
--
ALTER TABLE `know_contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `know_family`
--
ALTER TABLE `know_family`
  ADD PRIMARY KEY (`id`),
  ADD KEY `know_family_person_id_fd986b47_fk_know_person_id` (`person_id`);

--
-- Indexes for table `know_income`
--
ALTER TABLE `know_income`
  ADD PRIMARY KEY (`id`),
  ADD KEY `know_income_person_id_6ef70b64_fk_know_person_id` (`person_id`);

--
-- Indexes for table `know_person`
--
ALTER TABLE `know_person`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `captcha_captchastore`
--
ALTER TABLE `captcha_captchastore`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `djangonepal_district`
--
ALTER TABLE `djangonepal_district`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `djangonepal_municipality`
--
ALTER TABLE `djangonepal_municipality`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `djangonepal_province`
--
ALTER TABLE `djangonepal_province`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `know_address`
--
ALTER TABLE `know_address`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `know_contact`
--
ALTER TABLE `know_contact`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `know_family`
--
ALTER TABLE `know_family`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `know_income`
--
ALTER TABLE `know_income`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `know_person`
--
ALTER TABLE `know_person`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `djangonepal_district`
--
ALTER TABLE `djangonepal_district`
  ADD CONSTRAINT `djangonepal_district_province_id_fce96d02_fk_djangonep` FOREIGN KEY (`province_id`) REFERENCES `djangonepal_province` (`id`);

--
-- Constraints for table `djangonepal_municipality`
--
ALTER TABLE `djangonepal_municipality`
  ADD CONSTRAINT `djangonepal_municipa_district_id_f305c35c_fk_djangonep` FOREIGN KEY (`district_id`) REFERENCES `djangonepal_district` (`id`),
  ADD CONSTRAINT `djangonepal_municipa_province_id_ec09542b_fk_djangonep` FOREIGN KEY (`province_id`) REFERENCES `djangonepal_province` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `know_address`
--
ALTER TABLE `know_address`
  ADD CONSTRAINT `know_address_person_id_848eb147_fk_know_person_id` FOREIGN KEY (`person_id`) REFERENCES `know_person` (`id`);

--
-- Constraints for table `know_family`
--
ALTER TABLE `know_family`
  ADD CONSTRAINT `know_family_person_id_fd986b47_fk_know_person_id` FOREIGN KEY (`person_id`) REFERENCES `know_person` (`id`);

--
-- Constraints for table `know_income`
--
ALTER TABLE `know_income`
  ADD CONSTRAINT `know_income_person_id_6ef70b64_fk_know_person_id` FOREIGN KEY (`person_id`) REFERENCES `know_person` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
