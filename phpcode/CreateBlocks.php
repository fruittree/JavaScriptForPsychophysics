<?php
# a little php code that generate a random list of unique integers
# and create a JSON files of these indices. 
$filenames = array("block1.json", "block2.json", "block3.json", "block4.json");
$len = 160;   // total number of numbers
$min = 0;  // minimum
$max = 159;  // maximum
$range = []; // initialize array
foreach (range(0, $len - 1) as $i) {
    while(in_array($num = mt_rand($min, $max), $range));
    $range[] = $num;
}
$block1 = array_slice($range,0,40);
$block2 = array_slice($range,41,80);
$block3 = array_slice($range,81,120);
$block4 = array_slice($range,121,160);
$conditions = array($block1,$block2,$block3,$block4);
# save to files.
for ($x = 0; $x <= 3; $x++) {
    echo "The number is: $x <br>";
    $jsondata = json_encode($conditions[$x], JSON_PRETTY_PRINT);
	//write json data into data.json file
	if(file_put_contents($filenames[$x], $jsondata)) {
	    echo "file".$filenames[$x] . "saved<br>";
	}
	else 
	    echo "error";
}  
?>