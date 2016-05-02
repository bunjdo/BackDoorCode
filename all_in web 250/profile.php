<?php
	if(!isset($_COOKIE['USER-LOGGED']))
	{
		die("Необходимо войти.");
		exit();
	}
	if(isset($_POST['getFlag']))
	{
		if($_COOKIE['USER-LOGIN']=="admin")
		{
	  		$form = '<form method="post" id="form1">
	  		<br>Введите пароль для подтверждения:
	  		<br><input name="pass" type="password" placeholder="Пароль"><input name="accept" type="submit" value="Получить">
	  		</form>';
		}
		else
		{
			$form='<div style="color:red;">You must be an admin</div>';
		}	
	}
  	
  	if(isset($_POST['accept']))
  	{
  		if(strrev(md5(htmlspecialchars($_POST['pass'])))=='3bd31ca76779d7939288965cbdff1268')
  		{
  			$message2 = '<br><div style="color: green;">Congratulations!</div><br>Flag: DvCTF{g3t_e@sy_i}';	
  		}
  		else
  		{
  			$message2 = "<div style=\"color: red; line-height:25px;\">Invalid password";
  			if(strrev(md5(htmlspecialchars($_POST['pass'])))==$_COOKIE['USER-PASS'])
  			{
  				$message2.="<br>You need a superuser's password";
  			}
  			$message2.="</div>";
  		}
  	}
  	#detect browser
  	$user_agent = $_SERVER["HTTP_USER_AGENT"];
  	if (strpos($user_agent, "Firefox") !== false) $browser = "Firefox";
  	elseif (strpos($user_agent, "Opera") !== false) $browser = "Opera";
  	elseif (strpos($user_agent, "Chrome") !== false) $browser = "Chrome";
  	elseif (strpos($user_agent, "MSIE") !== false) $browser = "Internet Explorer";
  	elseif (strpos($user_agent, "Safari") !== false) $browser = "Safari";
  	else $browser = "Неизвестный";
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <title>Профиль</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <div class="register" style="width: 500px; margin-top: 100px;">
  	<li>Пользователь: <?=$_COOKIE['USER-LOGIN']?> (<a href="logout.php">Выйти</a>)</li>
  	<li>Пол: <?=$_COOKIE['USER-SEX']?></li>
  	<li>IP: <?=$_SERVER['REMOTE_ADDR']?></li>
  	<li>Браузер: <?=$browser?></li>
  	<form method="post">
  	<input name="getFlag" type="submit" value="Получить флаг">
  	</form>
  	<?=$form?>
  	<?=$message2?>
  </div>
</body>
</html>