# Choose Your Pokemon
Forensics - 150 Points

## Question
>Just a simple type of recursive function. [master-ball](master-ball)

### Hint
>Flag is formatted as {plain_text}

## Solution
Calling this a 'recursive function' might make you think master-ball is a 
binary, but it's actually a .RAR archive, as evidenced by the 'file' command. 
Opening the archive we find a folder, 'roshambo', and a PDF file, [inDesign](inDesign). 
Opening the PDF in Adobe Acrobat gives us a link to an online [pastebin](https://pastebin.com/AWTDEb9j), 
which in turn contains a [raw RTF file](paste). 

Copying the RTF text into a file and opening it in Microsoft Word lets us see 
the flag, which, as the hint reminds us, is formatted as plain text.

### Flag
{wild_type}
