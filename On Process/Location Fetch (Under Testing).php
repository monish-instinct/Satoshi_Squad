<?php
function getUserIP() {
    $ip = '';
    if (!empty($_SERVER['HTTP_CLIENT_IP']) && filter_var($_SERVER['HTTP_CLIENT_IP'], FILTER_VALIDATE_IP)) {
        $ip = $_SERVER['HTTP_CLIENT_IP'];
    } elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR']) && filter_var($_SERVER['HTTP_X_FORWARDED_FOR'], FILTER_VALIDATE_IP)) {
        $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
    } else {
        $ip = $_SERVER['REMOTE_ADDR'];
    }
    return $ip;
}

function getUserLocation($ip) {
    $location_data = null;
    $api_url = "http://ip-api.com/json/{$ip}";
    $response = file_get_contents($api_url);
    if ($response !== false) {
        $location_data = json_decode($response);
    }
    return $location_data;
}

$user_ip = getUserIP();
$location_data = getUserLocation($user_ip);

if ($location_data && $location_data->status == 'success') {
    $latitude = $location_data->lat;
    $longitude = $location_data->lon;
    echo "Latitude: $latitude, Longitude: $longitude";
} else {
    echo "Unable to fetch location data.";
}
?>