<?php

require "config.php";

function error($status_code, $message) {
	http_response_code($status_code);
	echo json_encode(array("success" => false, "error" => $message));
	die();
}

if(!isset($_POST["key"]) || $_POST["key"] != $key) {
	error(403, "Invalid key.");
}

$target_dir = "files/";
if(!file_exists($target_dir)) {
	mkdir($target_dir, 0777);
}

$temp_name = tempnam($target_dir, '');
$target_file =  $temp_name . "." . pathinfo($_FILES["file"]["name"], PATHINFO_EXTENSION);;
unlink($temp_name);
$upload_status = 0;

if($_FILES["file"]["size"] > $max_file_size) {
	error(413, "File too large.");
}

if(move_uploaded_file($_FILES["file"]["tmp_name"], $target_file)) {
	$file_url = "https://" . $_SERVER['SERVER_NAME'] . substr($_SERVER['REQUEST_URI'], 0, strrpos($_SERVER['REQUEST_URI'], "/")) . "/" . $target_dir . basename($target_file);
	echo json_encode(array("success" => true, "url" => $file_url));
	exit();
} else {
	error(500, "Error uploading file.");
}

?>