<?php
  if(isset($_POST['agreed'])&&isset($_POST['agree']))
  {
    session_start();
    if(isset($_SESSION['steps_completed']))
    {
      $message=base64_decode(htmlspecialchars(trim($_GET['simple_token'])));
      preg_match("/Yarrrr! You don't see that\. Secret is (.*)\./", $message, $match);
      if(($_SESSION['login'])==$match[1])
      {
        $_SESSION['steps_completed']=2;
        header('location: http://'.$_SERVER['HTTP_HOST'].'/all_in/3');
        exit();
      }
    }
    else
    {
      die('Необходимо пройти предшествующие шаги регистрации. <a href="'.$_SERVER['HTTP_REFERER'].'">Назад</a>');
      exit();
    }
  }
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <title>Регистрация #2</title>
  <link rel="stylesheet" href="css/bootstrap.min.css">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <div class="register-title" style="text-align: left; width: 900px">
      <div style="margin-left: 20px; line-height: 1.5">
          <div style="font-size: 30px;"><p>Добро пожаловать</p></div>
          <p>Прежде чем продолжить регистрацию на нашем замечательном сайте, вы должны кое что знать:</p>
          <li><p>Мы не несем ответственности за операции с введенными вами данными</p></li>
          <li><p>Никаких гарантий надёжности и защищённости</p></li>
          <li><p>Багоюз, эксплойтоюз жестоко караются</p></li>
          <li><p>Наши одмены - самые ленивые существа в мире</p></li>
          <li><p>…прогуливающие пары и не только</p></li>
          <li><p>На все вопросы мы все равно не ответим</p></li>
          <li><p>Любим играть в слова паролями пользователей</p></li>
          <li><p>Считаем эту вёрстку эталонной</p></li>
          <li><p>Не терпим критику</p></li>
          <p>Как говорится: &quot;Принимая данное соглашение, вы берёте всю ответственность на себя&quot;.</p>
          <br>
      </div>
  </div>
  <form class="register" method="post" style="text-align: left; width: 900px;">
    <label style="font-size: 18px;"><input name="agree" type="checkbox">Подтверждаю</label>
    <input name="agreed" type="submit" value="Продолжить" class="register-button">
  </form>
</body>
</html>