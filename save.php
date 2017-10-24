<?php
header("Access-Control-Allow-Origin: *")

 $content = $_POST["content"];
  echo $content;
  if (!empty($content)){
   $myfile = fopen("img.jpg", "w");
   fwrite($myfile, $content);
   fclose($myfile);
 }
 echo "Saved";
 ?>



