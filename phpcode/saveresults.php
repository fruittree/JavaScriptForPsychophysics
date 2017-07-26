<?php
$stringData = $_POST["data"];
$myPostData = json_decode($stringData,true);
$subject = $myPostData["subject"];
$datafile = '_results.json';
$fh = fopen($subject.$datafile, 'w') or die("can't open file");
fwrite($fh, $stringData);
fclose($fh)
?>

