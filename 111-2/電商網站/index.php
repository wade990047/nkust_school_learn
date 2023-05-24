<?php 
  session_start();
  $account = $_POST["account"];
  $password = $_POST["password"];
  if ($account!="" && $password!="") {
    if ($account=="admin" && $password=="1234")
    {
        $_SESSION["user"] = "administrator";
    }
  }
?>
<?php include "bootstrap.php" ?>
<title>吳承瑋的入口網站</title>
</head>

<body>
    <div class="container">

        <h1>歡迎來到我的第一個網頁</h1>
        <?php include "header.php"; ?>
        <p>點擊上面的選項，執行更多的功能！</p>
        <?php
            if ($_SESSION["user"] !="administrator") {
        ?>
            <form action="index.php" method="POST">
            帳號：<input type=text size=10 name="account"><br>
            密碼：<input type=password size=10 name="password"><br>
            <input type=submit value="登入">
            <input type=reset value="清除">
            </form>
        <?php
            } else {
                echo '<a href="logout.php" class="btn btn-danger">登出</a>';
            }
        ?>  
    </div>
    <?php include "footer.php" ?>