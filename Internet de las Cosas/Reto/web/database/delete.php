<?php
require_once 'databaseconnect.php';

$ID = $_GET['id'];
$QUERY = "DELETE FROM users where userID = ".$ID;

mysqli_query($conn,$QUERY);
header("Location: adminUsuario.php");

?>

