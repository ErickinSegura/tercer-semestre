<?php 

require_once 'databaseconnect.php';

$f_name = $_POST['f_name'];
$m_name = $_POST['m_name'];
$fl_name = $_POST['fl_name'];
$sl_name = $_POST['sl_name'];
$email = $_POST['email'];
$password = $_POST['password'];


$QUERY = "INSERT INTO users (f_name, m_name, fl_name, sl_name, email ,password) VALUES ('".$f_name."','".$m_name."','".$fl_name."','".$sl_name."','".$email."','".$password."')";

$RESULT = mysqli_query($conn,$QUERY);

if ($RESULT) {
    
    echo '<script>alert("Usuario Registrado");</script>';
    header("Location: /ioroots/register.php");
    exit();
    
} 
else {
    echo "<br>";
    echo "Usuario no registrado";
    echo "<br>";
}

?>
