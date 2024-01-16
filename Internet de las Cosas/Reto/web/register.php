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
        <form method = 'post', action = "/ioroots/database/validaRegister.php">
            <h1 class="LoginTitle">Registrate</h1>
            <div class="name">
                <label for="f_name">Primer Nombre</label>
                <input type="text" name="f_name" id="f_name" placeholder="Primer Nombre">
                <label for="m_name">Segundo Nombre</label>
                <input type="text" name="m_name" id="m_name" placeholder="Segundo Nombre">
            </div>
            <div class="lastname">
                <label for="lastname">Primer Apellido</label>
                <input type="text" name="f_lastname" id="f_lastname" placeholder="Primer Apellido">
                <label for="lastname">Segundo Apellido</label>
                <input type="text" name="m_lastname" id="m_lastname" placeholder="Segundo Apellido">
            </div>
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
                <p>¿Ya tienes cuenta? <a href="login.php">Inicia Sesión</a></p>
                <br>
                <a href="index.html">Volver al Inicio</a>
            </div>
        </form>
    </div>
</div>


</body>
</html>