# Educated Guess
Web Exploitation - 600 Points

## Question
>There is a secured system running at [http://shell1.2019.peactf.com:1428/query.php](http://shell1.2019.peactf.com:1428/query.php). You have obtained the [source code](query.phps).

### Hint
>Good programmers follow naming conventions.

## Solution
Looking at the source code, we can glimpse what happens when a user queries the website. 
The program looks for the user's 'user' cookie, which it unserializes, then calls the is_admin() funcion.  

The use of serialize()/unserialize() on user input is notoriously prone to php object injection, and the user
cookie is apparently our point of entry. The 'educated guess' portion of this question relates to guessing how
the php object might be named and how we might write our own is_admin() function to always return true.  

Following 'good programming conventions', we might guess that the class denoted $user might be named User, and that
$admin is a stored boolean state. And after a little messing around, I found a working solution [here](injection.php).

### Flag
flag{peactf_follow_conventions_4022940cb27774f618aa62fe8be202bc}