<?php
	if(isset($_POST['registered']))
	{
		$mysqli = new mysqli($_SERVER['HTTP_HOST'],"root", "","reg_db");
    if ($mysqli->connect_error) {
          die('Ошибка подключения.');
          exit();
      }
    $pass = mysqli_real_escape_string($mysqli, stripslashes(strip_tags(trim($_POST['pass']))));
    $login = $_POST['login'];
    if(isChangingTableCode($login)){
      die("Don't try to change our database.");
      exit();
    }
    $query = $mysqli->query("SELECT * FROM  `users` WHERE  `login` = '$login' and `password` = '".strrev(md5($pass))."' LIMIT 1;");
    $mysqli->close();
    $row = $query->fetch_row();
    if(isset($row))
    {
      setcookie('USER-LOGGED', true, time()+86400, "/all_in");
      setcookie('USER-ID', $row[0], time()+86400, "/all_in");
      setcookie('USER-LOGIN', $row[1], time()+86400, "/all_in");
      setcookie('USER-PASS', $row[2], time()+86400, "/all_in");
      setcookie('USER-SEX', $row[3], time()+86400, "/all_in");
      header('location: http://'.$_SERVER['HTTP_HOST'].'/all_in/profile'); 
    }
	}
  function isChangingTableCode($code)
  {
    $banwords=array("CREATE ", "ALTER ", "SET ", "DROP ", "UPDATE ", "INSERT ", "DELETE ", "USE ", "PHP ", "ADD ", "RENAME ", "CHANGE ");
    foreach ($banwords as $variable) {
      if(stristr($code, $variable)) return true;
    }
    return false;
  }
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <title>Вход</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <h1 class="register-title">Вход</h1>
  <form class="register" method="post">
    <input name="login" type="text" class="register-input" placeholder="Логин" pattern="[A-Za-z0-9]{0,15}" title="Только латинские символы и/или цифры" required>
    <input name="pass" type="password" class="register-input" placeholder="Пароль" pattern="[A-Za-z0-9]{0,15}" title="Только латинские символы и/или цифры" required>
    <input name="registered" type="submit" value="Войти" class="register-button">
  </form>
</body>
</html>