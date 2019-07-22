<?php

class Injection
{
    public function __construct($username){
        $this->user = 'admin';
    }

    public function __wakeup(){
        $this->user = 'admin';
    }

}

$ex = new Injection('admin');
$str = serialize($ex);
echo $str;

$user = unserialize($str);

    if ($user->user =='admin') {
        echo "gamers";
    } else {echo "Permission Denied";
    }

?>