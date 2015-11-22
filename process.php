<?php

error_reporting(E_ALL);
ini_set('display_errors', '1');

$login = $_POST['login'];
$pass = $_POST['pass'];

echo '<br>Hello, ' . $login . '<br><br>';

$link = mysql_connect('46.37.146.33:7306', 'user', 'qwerty123');
if (!$link) {
    die('Cannot connect: ' . mysql_error());
}


$selected = mysql_select_db("test", $link)
  or die('No such db');
echo 'Connection: OK' . '<br><br>';

$sql = "SELECT data FROM users WHERE login='" . $login . "' AND pass='" . $pass . "';";
echo 'Trying ' . $sql . '<br><br>';
$result = mysql_query($sql);

if (!$result) die("Login failed. No data will be shown");
$row = mysql_fetch_array($result);

if ($row)
    echo "Data: ".$row{'data'} . "<br>";
else
    echo "Login failed. No data will be shown";


mysql_close($link);

/*


*/

?>
