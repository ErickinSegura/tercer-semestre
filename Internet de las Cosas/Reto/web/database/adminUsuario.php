<!DOCTYPE html>
<html>
<head>
    <title>Usuarios</title>
    <link rel="stylesheet" type="text/css" href="/ioroots/css/style.css">
</head>

<body>
    <div class="usuarios">
        <h1>Altas de Usuarios</h1>
        <table>
        <?php
        require_once 'databaseconnect.php';


        echo "<tr>
            <td>ID</td>
            <td>Name</td>
            <td>Middle Name</td>
            <td>First Last Name</td>
            <td>Second Last Name</td>
            <td>e-Mail</td>
            <td>Password</td>
            <td>Delete</td>
            </tr>";


        $QUERY = "SELECT * FROM users";
        $RESULT = mysqli_query($conn,$QUERY);
        while ($row = mysqli_fetch_array($RESULT)) {
            echo "<tr>
            <td>".$row['userID']."</td>
            <td>".$row['f_name']."</td>
            <td>".$row['m_name']."</td>
            <td>".$row['fl_name']."</td>
            <td>".$row['sl_name']."</td>
            <td>".$row['email']."</td>
            <td>".$row['password']."</td>
            <td><a href='delete.php?id=".$row['userID']."'>X</a></td>
            </tr>";
        }
        ?></table>
        <a href='/ioroots/main.html'>Back</a>

    </table>
</div>


</body>
</html>