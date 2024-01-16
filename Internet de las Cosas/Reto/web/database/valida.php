<?php 

require_once 'databaseconnect.php';

$email = $_POST['email'];
$pass = $_POST['password'];

$QUERY = "SELECT userID FROM users WHERE email = '".$email."' AND password='".$pass."'";


$RESULT = mysqli_query($conn,$QUERY);


if (mysqli_num_rows($RESULT) == 1) {
        echo 'Logged In!';
        header("Location: /ioroots/main.html");
        exit();
    } 
else {
    echo "<br>";
    echo "Usuario o contraseña incorrectos";
    echo "<br>";
}

?>
