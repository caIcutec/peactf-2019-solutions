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

>username: admin
answer: blah
SQL query: SELECT password, answer FROM users WHERE username='admin'


