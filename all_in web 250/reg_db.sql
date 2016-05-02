-- phpMyAdmin SQL Dump
-- version 3.5.1
-- http://www.phpmyadmin.net
--
-- Хост: 127.0.0.1
-- Время создания: Мар 28 2016 г., 17:03
-- Версия сервера: 5.5.25
-- Версия PHP: 5.3.13

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- База данных: `reg_db`
--

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `login` varchar(64) NOT NULL,
  `password` varchar(32) NOT NULL,
  `sex` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `login` (`login`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=10 ;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id`, `login`, `password`, `sex`) VALUES
(1, 'admin', '8621ffdbc5698829397d97767ac13db3', 'M'),
(2, 'what', '05d3180e6a4cd0ec8c9d8751998561b2', 'F'),
(3, 'do', '5df2e589a33bb3c4cf005a5904dc7f4f', 'F'),
(4, 'you', '2624b354900da66a284fb1f08186e203', 'F'),
(5, 'want', '91fa68006f445a0688f67864e7de014f', 'M'),
(6, 'to', 'a75936ac759502b5e5af00190a211515', 'F'),
(7, 'see', '6c6d107ff53f32f5bfeee5a6d7ddeee3', 'M'),
(8, 'here', 'b8c63e612f5ea8f0fd5e65c9e8f4f103', 'F'),
(9, '?', 'b670b9fc6f33406723c7f7fd89c1a6c7', 'M');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
