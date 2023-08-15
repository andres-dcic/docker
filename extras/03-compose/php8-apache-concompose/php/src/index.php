<?php
//These are the defined authentication environment in the db service

// The MySQL service named in the docker-compose.yml.
$host = 'db';

// Database use name
$user = 'mysql_user';

//database user password
$pass = 'mysql_password';


$mydatabase = 'database';
// check the mysql connection status

$conn = new mysqli($host, $user, $pass, $mydatabase);

// check the MySQL connection status
$sql = 'SELECT * FROM users';

if ($result = $conn->query($sql)) {
    while ($data = $result->fetch_object()) {
        $users[] = $data;
    }
}

foreach ($users as $user) {
    echo "<h1>";
    echo $user->username . ": " . $user->password;
    echo "</h1>";
    echo "\n";

}

?>
