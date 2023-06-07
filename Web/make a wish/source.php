<?php 
	if(isset($_GET['wish'])) {
		 if (preg_match("/.*/i", $_GET['wish'], $match))  {
	    echo "<h1>No, try something else!</h1>"; 
    } else {
	    echo "<h1>cc{REDACTED}</h1>";
    } 
	} else {
 	  echo "<h1>Make a wish and maybe I will fulfill it</h1>";
	}
?>