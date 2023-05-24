<?php
include "bootstrap.php";
include "database.php";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
?>
<div class="container">
  <h1 class="alert alert-warning">電視頻道管理</h1>
  <?php include "header.php"; ?>
  <form action="addtv.php" method="POST">
    電視台名稱：<input type=text name=name required><br>
    Token：<input type=text name=token required><br>
    <input type=submit value="新增">
  </form>
  <hr>
  <?php
  $sql = "SELECT * FROM tv order by token desc";
  $result = $conn->query($sql);

  if ($result->num_rows > 0) {
    echo "<table class='table table-striped'>";
    echo "<tr><td>編號</td><td>名稱</td><td>Token</td></tr>";
    while ($row = $result->fetch_assoc()) {
      echo "<tr>";
      echo "<td>" . $row["id"] . "</td>" .
        "<td>" . $row["name"] . "</td>" .
        "<td>" . $row["token"] . "</td>" .
        "<td><a href='deltv.php?id="
        . $row["id"] . "' class='btn btn-outline-danger btn-sm'>刪除</a></td>" .
        "</tr>";
    }
    echo "</table>";
  } else {
    echo "0 results";
  }
  $conn->close();
  ?>
</div>
<?php include "footer.php"; ?>