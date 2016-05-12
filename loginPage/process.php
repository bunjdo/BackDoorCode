<?php

error_reporting(E_ALL);
ini_set('display_errors', '1');

$login = $_POST['login'];
$pass = $_POST['pass'];

// echo $login . '<br><br>' . ;

if ($login == "admin" && $pass == "megapasssword") {
	echo '<br>Hello, ' . $login . '<br><br>';
	echo 'Your key is: "DvCTF{ThisIsKeyForLoginTask0284}<br>';
} else {
	echo 'Wrong login or password';
}

?>
