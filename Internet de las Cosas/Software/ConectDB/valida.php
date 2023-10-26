<?php 

require_once 'databaseconnect.php';

$usuario = $_POST['user'];
$pass = $_POST['password'];

$QUERY = "SELECT user_ID FROM usuario WHERE user = '".$usuario."' AND password='".$pass."'";


$RESULT = mysqli_query($conn,$QUERY);


if (mysqli_num_rows($RESULT) == 1) {
        echo 'Logged In!';
        header("Location: home.php");
        exit();
    } 
else {
    echo "<br>";
    echo "Usuario o contraseña incorrectos";
    echo "<br>";
}

?>
