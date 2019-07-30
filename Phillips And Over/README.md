# Philips And Over
Web Exploitation - 900 Points

## Question
>There is a website running at http://shell1.2019.peactf.com:10078. Try to log 
in the "admin" account.

### Hint
>A bucket can only fill with the volume of water the shortest plank allows.

## Solution
At first glance, the page seems like a regular login form with no obvious flaws.
However, looking at the source of the password reset form (result.html) we see
there is a hidden third field called 'debug', with value 0. Using a server state
editor, we can change our POST request to have a 'debug' value of 1. Doing so 
shows us an underlying SQL query being called. 

>username: blah
answer: blah
SQL query: SELECT password, answer FROM users WHERE username='blah'

While it would be wonderful to know an existing username / answer pair to write
some sort of UNION statement, we can't do that. However, this password retrieval
is still prone to leaking - notice how having a username 'blah' gives us the 
'user does not exist' message, and the username 'admin' gives us the 'wrong
security answer' message. 

The typical username ' OR '1'='1 never shows us the
'user does not exist' message, because the check always evaluates to true.
By changing the latter part of the OR statement to check substrings of the 
password, we can perform a blind SQL injection on this true-false state.

> example username: blah' OR SUBSTR(password, 1, 1) = 'a

Writing a script can help automate this, and help us find the password we need.
I've included a [working solution](blind-sql.py). The password for the admin
account I found was 45873291, but it may not be the same for you. Try it out!

### Flag
flag{peactf_E_>_A_4d7424757a1b776fe6c456bef727aad3}

