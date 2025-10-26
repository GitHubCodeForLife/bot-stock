-- Adminer 5.4.1 MySQL 9.5.0 dump

SET NAMES utf8;
SET time_zone = '+07:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `apscheduler_jobs`;
CREATE TABLE `apscheduler_jobs` (
  `id` varchar(191) NOT NULL,
  `next_run_time` double DEFAULT NULL,
  `job_state` blob NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_apscheduler_jobs_next_run_time` (`next_run_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `job_opt_log`;
CREATE TABLE `job_opt_log` (
  `log_id` int NOT NULL AUTO_INCREMENT,
  `job_func` varchar(255) NOT NULL,
  `job_status` varchar(255) NOT NULL,
  `job_time` varchar(255) NOT NULL,
  `job_message` varchar(15000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`log_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `job_scheduler`;
CREATE TABLE `job_scheduler` (
  `job_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `job_func` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `job_data` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `trigger` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `job_interval` int NOT NULL,
  `cron_expression` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `create_time` varchar(255) NOT NULL,
  `misfire_grace_time` int NOT NULL,
  `max_instances` int NOT NULL,
  `coalesce` tinyint(1) DEFAULT '1',
  `source_type` varchar(255) DEFAULT NULL,
  `source_code` longblob,
  PRIMARY KEY (`job_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `job_scheduler` (`job_id`, `job_func`, `job_data`, `trigger`, `job_interval`, `cron_expression`, `create_time`, `misfire_grace_time`, `max_instances`, `coalesce`, `source_type`, `source_code`) VALUES
('fun_test',	'app.scheduler.schedulerTask:fun_test',	'[\"VND\", \"SSI\", \"VCI\"]',	'cron',	0,	'*/5 * * * *',	'',	0,	1,	1,	NULL,	NULL);

DROP TABLE IF EXISTS `notification_log`;
CREATE TABLE `notification_log` (
  `log_id` int NOT NULL AUTO_INCREMENT,
  `platform` varchar(255) NOT NULL,
  `channel` varchar(255) NOT NULL,
  `message` varchar(255) NOT NULL,
  `send_time` datetime NOT NULL,
  `stock_code` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  PRIMARY KEY (`log_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- 2025-10-26 02:37:10 UTC