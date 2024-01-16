<!DOCTYPE html>
<html>

<head>
    <title>Login</title>
    <link rel="stylesheet" href="css/style.css">
</head>


<body class="logreg">



<div class="loginForm">
    <div class="brandLogin">
        <img src="src/image.png" alt="logo">
        <h1>IoRoots</h1>
    </div>
    <div class="loginContent" >
        <form method = 'post', action = "/ioroots/database/valida.php">
            <h1 class="LoginTitle">Inicia Sesión</h1>
            <div class="email">
                <label for="email">e-mail</label>
                <input type="text" name="email" id="email" placeholder="e-mail">
            </div>
            <div class="password">
                <label for="password">Contraseña</label>
                <input type="password" name="password" id="password" placeholder="Contraseña">
            </div>
            <div class="submit">
                <button>Entrar</button>
            </div>
            <div class="logregister">
                <p>¿No tienes cuenta? <a href="register.php">Registrate</a></p>
                <br>
                <a href="index.html">Volver al Inicio</a>
            </div>
        </form>
    </div>
</div>


</body>
</html>