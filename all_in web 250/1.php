<?php
  if(isset($_POST['registered']))
  {
    $mysqli = new mysqli($_SERVER['HTTP_HOST'],"root", "","reg_db");
    $login = mysqli_real_escape_string($mysqli, stripslashes(strip_tags(trim($_POST['login']))));
    $pass = mysqli_real_escape_string($mysqli, stripslashes(strip_tags(trim($_POST['pass']))));
    $sex = mysqli_real_escape_string($mysqli, stripslashes(strip_tags(trim($_POST['sex']))));
    if ($mysqli->connect_error) {
      die('Ошибка подключения. <a href="'.$_SERVER['HTTP_REFERER'].'">Назад</a>');
      exit();
    }
    else
    {
      if(isChangingTableCode($login)){
        die('Не стоит использовать служебные слова синтаксиса SQL. <a href="'.$_SERVER['HTTP_REFERER'].'">Назад</a>');
        exit();
      }
      if (preg_match('/[^A-Za-z0-9]+/',$login))
      {
                //запрещенные символы
                //если присутствует хоть что-то кроме цифры или латинской буквы
        die('Используйте в логине только латинские символы и/или цифры. <a href="'.$_SERVER['HTTP_REFERER'].'">Назад</a>');
        exit();
      }else{
        $query = $mysqli->query("SELECT `id` FROM `users` WHERE  `login` = '$login' LIMIT 1")->fetch_assoc();
        $mysqli->close();
        if($query["id"])      //проверка на существование
        {
          die('Пользователь с таким логином уже существует. <a href="'.$_SERVER['HTTP_REFERER'].'">Назад</a>');
          exit();
        }
        else
        {
          session_start();
          $_SESSION['login']=$login;
          $_SESSION['md5pass']=strrev(md5($pass));
          $_SESSION['sex']=$sex;
          $_SESSION['steps_completed']=1;
          $message = base64_encode("Yarrrr! You don't see that. Secret is %YOUR_NAME%.");
          header('location: 2?simple_token='.$message);
          exit();
        }
      }
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
  <title>Регистрация #1</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <h1 class="register-title">Регистрация #1</h1>
  <form class="register" method="post">
    <div class="register-switch">
      <input type="radio" name="sex" value="F" id="sex_f" class="register-switch-input" checked>
      <label for="sex_f" class="register-switch-label">Ж</label>
      <input type="radio" name="sex" value="M" id="sex_m" class="register-switch-input">
      <label for="sex_m" class="register-switch-label">М</label>
    </div>
    <input name="login" type="text" class="register-input" placeholder="Логин" pattern="[A-Za-z0-9]{0,15}" title="Только латинские символы и/или цифры" required>
    <input name="pass" type="password" class="register-input" placeholder="Пароль" pattern="[A-Za-z0-9]{0,15}" title="Только латинские символы и/или цифры" required>
    <input name="registered" type="submit" value="Создать аккаунт" class="register-button">
  </form>
</body>
</html>