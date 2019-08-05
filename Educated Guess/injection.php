<?php

class User{
    public $admin = true;
    public function is_admin(){
        return $admin;
    }
}

$admin = new User();
echo urlencode(serialize($admin));
?>