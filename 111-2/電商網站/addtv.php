<?php
include("database.php");

$name = $_POST["name"];
$token = $_POST["token"];

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "INSERT INTO tv (name, token) VALUES ('" .
  $name . "','" . $token . "')";

$conn->query($sql);
$conn->close();
header("Location: tvinfo.php");
