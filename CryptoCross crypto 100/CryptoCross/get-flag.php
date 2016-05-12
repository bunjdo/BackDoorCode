<?php
	session_start();
	$answers = array("CARDANO","ACROSTIC","ROT","KRYPTOS","VOYNICH","HAGELIN","BACON","BEALE","ATBASH","POLYBIUS","SCYTALE","VIGENERE","BRAILLE","MORSE","SCHILLING");
	if(isset($_POST['removewords']))
	{
		unset($_SESSION['entered']);
		header('location:'.$_SERVER['HTTP_REFERER']);
	}
	if(isset($_POST['word']))
	{
		if(empty($_SESSION['entered']))
		{
			$_SESSION['entered'] = array();
		}
		if(in_array($_POST['word'], $answers))
		{
			if(!in_array($_POST['word'], $_SESSION['entered']))
			{
				array_push($_SESSION['entered'], $_POST['word']);
				$message = "Верно";
			}
			else
			{
				$message = "Уже засчитано";
			}
		}
		else
		{
			if(strlen($_POST['word']) != 0) $message = "Не верно";
		}
		if(isset($_SESSION['entered']) && !array_diff($answers, $_SESSION['entered']))
		{
			$flag = "<h4>DvCTF{r1y_gR3at_cRypt0_erud1T10n}</h4>";
			$message = "";
		}
	}
	function get_entered_string()
	{
		if(count($_SESSION['entered'])>1) return implode(", ", $_SESSION['entered']);
		else return $_SESSION['entered'][0];
	}
	$head ="";
	if(count($_SESSION['entered']) == 0)
	{
		$head.= '<h3>Введите отгаданные слова по одному</h3>';
	}
	else
	{
		$head.='<h3>Вы отгадали: '.count($_SESSION['entered']).' из '.count($answers).':</h3><h4>';
		$head.=get_entered_string();
		$head.='</h4>';
	}
?>
<!DOCTYPE html>
<html>
<head>
	<title>Get the flag</title>
</head>
<body>
<?=$head;?> 
<form method="POST">
	<input name="word" type="text" placeholder="Введите отгаданные слова..." style="width:200px;" autofocus>
	<input name="getword" type="submit">
	<input name="removewords" type="submit" value="Удалить слова">
</form>
<?=$message;?>
<?=$flag;?>
</body>
</html>