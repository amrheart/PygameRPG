<?php
require_once __DIR__ . "/bootstrap.php";
?>
<!DOCTYPE html>
<html>

<head>
    <?php include __DIR__ . "/../main/app_head.php"; ?>
    <link href="css/app.css" rel="stylesheet">
</head>

<body>
    <?php include __DIR__ . "/app_navbar.php"; ?>
    <?php include __DIR__ . "/app_menu.php"; ?>
    <div class="container-fluid content">
        <h3 class="page-header">Selective Injury Illness Tags</h3>

        <form class="form-horizontal" id="clientForm">
            <div class="form-group">
                <div class="col-sm-1">
                    <label class="control-label">Client #</label>
                    <input type="text" name="txtClientNum" id="txtClientNum" class="form-control">
                </div>
                <div class="col-sm-2">
                    <label class="control-label">Injury Illness Name</label>
                    <input type="text" name="username" id="username" class="form-control">
                </div>
                <div class="col-sm-2" style="margin-top:27px">
                    <button type="button" class="btn btn-primary" id="filterBtn">Filter</button>
                    <button type="reset" class="btn btn-default" id="resetBtn">Reset</button>
                </div>
            </div>
        </form>
        <hr>
        <div id="clientInfo"></div>
        <hr>
        <div id="container"></div>
    </div>

    <?php include __DIR__ . "/../main/app_scripts.php"; ?>
    <script src="<?= Util::stampFile("../ia_dashboard/js/common.js"); ?>"></script>
    <script src="<?= Util::stampFile("js/selective_injury_tags.js"); ?>"></script>
</body>

</html>