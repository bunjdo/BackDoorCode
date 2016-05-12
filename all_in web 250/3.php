<?php
  session_start();
  if($_SESSION['steps_completed']==2)
  {
    $mysqli = new mysqli($_SERVER['HTTP_HOST'],"root", "","reg_db");
    $query = $mysqli->query("INSERT INTO `reg_db`.`users` (`id`, `login`, `password`, `sex`) VALUES (NULL, '".$_SESSION['login']."', '".$_SESSION['md5pass']."', '".$_SESSION['sex']."');");
    $mysqli->close();
    if (!$query) {
      die('Невозможно добавить пользователя. Возможно, пользователь уже был добавлен. <a href="'.$_SERVER['HTTP_REFERER'].'">Назад</a>');
    }
  }
  else
  {
    die('Необходимо пройти предшествующие шаги регистрации. <a href="'.$_SERVER['HTTP_REFERER'].'">Назад</a>');
  }
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <title>Регистрация #3</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <h1 class="register-title" style="width: 700px">Пользователь с логином <?=htmlspecialchars($_SESSION['login']);?> зарегистрирован.
    <br>
    Теперь вы можете войти в систему.
  </h1>
</body>
</html>