<?php
$celsius = 0; 

echo "--- ตารางแปลงค่า เซลเซียส เป็น ฟาเรนไฮต์ ---\n";

while ($celsius <= 5) {
    $fahrenheit = ($celsius * 1.8) + 32; 
    
    echo "$celsius °C = $fahrenheit °F\n";
    
    $celsius += 10;
}
?>