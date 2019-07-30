# We Are E.xtr
Forensics - 350 Points

## Question
>[E.xtr](E.xtr)

### Hint
>None.

## Solution
The file command doesn't give us much info on the extension .xtr, but running 
strings on the file shows us some interesting results.

>IHDR  
sRGB  
gAMA  
fPLTE  
@@@(((  
   xxx  

The IHDR block is an integral part of PNG encoding, so it's likely we're dealing
with a corrupted image of some sort. Opening the file in a hex editor shows us
that rather than the standard .PNG opening, we have .XTR, which prevents us from
reading the image as a PNG. Just edit those opening bytes and the [image](E.png) 
should be viewable.

### Flag
{read_banned_it}
