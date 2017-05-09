<?php
	$RETR=0;
	
	if (!defined('PHP_VERSION_ID')) {
		$version = explode('.', PHP_VERSION);
		define('PHP_VERSION_ID', ($version[0] * 10000 + $version[1] * 100 + $version[2]));
	}
	
	echo "Checking PHP version: ".PHP_VERSION.PHP_EOL; flush();
	
	//TEST pdo_sql
	echo "Checking PDO_sqlite extension... "; flush();
	if (class_exists('PDO') and in_array('sqlite', pdo_drivers())) {
		echo "ok\n";
		$DB_DATABASE = '/var/lib/fabui/fabtotum.db';
		if (file_exists($DB_DATABASE))
		{
			echo "Checking Database access... "; flush();
			$db = new PDO('sqlite:'.$DB_DATABASE, 'root', 'fabtotum');
			if ($db) {
				echo "ok\n";
				/*$r = $db->query($q);
				$count = (int)($r->fetchColumn());
				if ($count > 0) 
					$RETR=1*/
			} else {
				echo "FAILED\n";
				$RETR=2;
			}
		}
	} else {
		echo "MISSING\n";
		$RETR=2;
	}
	
	//TEST curl
	echo "Checking cURL extension... "; flush();
	if (function_exists('curl_init')) {
		echo "ok\n";
	} else {
		echo "MISSING\n";
		$RETR=2;
	}
	
	//TEST: ZipArchive
	echo "Checking Zip extension... ";
	if (class_exists('ZipArchive')) {
		echo "ok\n";
	} else {
		echo "MISSING\n";
		$RETR=2;
	}
	
	// TEST: DomDocument
	echo "Checking DOMDocument... ";
	if (class_exists('DOMDocument')) {
		echo "ok\n";
	} else {
		echo "MISSING\n";
		$RETR=2;
	}
	
	// TEST: GetText
	echo "Checking Gettext... ";
	if(function_exists('bindtextdomain')) {
		echo "ok\n";
	} else {
		echo "MISSING\n";
		$RETR=2;
	}
	
	// TEST: PHP settings
	/*echo "Checking PHP time zone... ";
	$timezone = ini_get('date.timezone');
	echo "{$timezone}: ";
	if ($timezone == 'UTC') {
		echo "ok\n";
	} else {
		echo "should be 'UTC'\n";
		$RETR=2;
	}*/
	
	echo "Checking PHP max size for POST requests... ";
	$post_max_size = ini_get('post_max_size');
	echo "{$post_max_size}: ";
	$megs = array_shift(explode('M', $post_max_size));
	if ($megs >= 128) {
		echo "ok\n";
	} else {
		echo "should be at least 128M\n";
		$RETR=2;
	}
	
	echo "Checking PHP max size for uploaded files... ";
	$upload_max_size = ini_get('upload_max_filesize');
	echo "{$upload_max_size}: ";
	$megs = array_shift(explode('M', $upload_max_size));
	if ($megs >= 128) {
		echo "ok\n";
	} else {
		echo "should be at least 128M\n";
		$RETR=2;
	}
	
	exit($RETR);
?>
