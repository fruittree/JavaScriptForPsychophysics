<?php
$stringData = $_POST["data"];
$myPostData = json_decode($stringData,true);
$subject = $myPostData["subject"];
$block = $myPostData["blocknumber"];
$datafile = '_results.json';
$fh = fopen($subject.'_block_'.$block.$datafile, 'w') or die("can't open file");
fwrite($fh, $stringData);
fclose($fh)
?>

