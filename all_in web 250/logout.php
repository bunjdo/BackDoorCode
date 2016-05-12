<?php
setcookie('USER-LOGGED', false, time()-86400, "/all_in");
setcookie('USER-ID', '', time()-86400, "/all_in");
setcookie('USER-LOGIN', '', time()-86400, "/all_in");
setcookie('USER-PASS', '', time()-86400, "/all_in");
setcookie('USER-SEX', '', time()-86400, "/all_in");
header("Location: sign-in");
exit();
?>