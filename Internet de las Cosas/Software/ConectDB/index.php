<!DOCTYPE html>
<html>

<head>
    <title>Login</title>
</head>


<body>


<div class="loginForm">
    <form method = 'post', action = "valida.php", action="registro.php">
        <table>
            <tr>
                <td colspan="2", align="center", class="title">
                    <p>Login</p>
                </td>
            </tr>
            
            <tr>
                <td>
                    <p>User</p>
                </td>
                <td>
                    <input type="text" id = "user" name="user">
                </td>
            </tr>
    
            <tr>
                <td>
                    <p>Password</p>
                </td>
                <td>
                    <input type="password" id="password" name="password">
                </td>
            </tr>
    
            <tr>
                <td>
                    <button>Entrar</button>
                </td>

                <td>
                    <a href="registro.php">
                    Registro
                    </a>
                </td>
                
            </tr>
        </table>
    </form>
</div>


<?php

?>

</body>
</html>
