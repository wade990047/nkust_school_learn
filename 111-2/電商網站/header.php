<?php 
  session_start();
?>
<nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">選單</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="index.php">首頁</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="https://ccet.nkust.edu.tw/">不分系</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="rate.php">匯率換算</a>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        所有功能
                    </a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="bmi.php">BMI計算</a></li>
                        <li><a class="dropdown-item" href="lotto.php">樂透預測</a></li>
                        <li><a class="dropdown-item" href="bodyinfo.php">健康管理</a></li>
<<<<<<< HEAD
                        <li><a class="dropdown-item" href="tv.php">電視選台器</a></li>
                        <li><a class="dropdown-item" href="tvinfo.php">電視頻道管理</a></li>
=======
                        <li><a class="dropdown-item" href="js-example/index.html">JS練習</a></li>
>>>>>>> 219d9cb2ae5d3d1abab2eab1b6b3c093931f7320
                    </ul>
                <?php
                    if ($_SESSION["user"] != "administrator") {
                    } else {
                        echo "</li>";
                        echo "<li class=\"nav-item\">";
                        echo "<a class=\"nav-link\" href=\"logout.php\">登出</a>";
                        echo "</li>";
                    }
                ?>  
            </ul>
        </div>
    </div>
</nav>