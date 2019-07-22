# Hide and Seek
General Skills - 50 Points

## Question
>Try to find to the flag file located somewhere in the folders located in: 
/problems/hide-and-seek_33_921c0f8b37da0fb54cf24d720d412bc3

### Hint
>Some tools get handy when files get disorganized.
What does the command "find" do?

## Solution 
The chief problem with finding the flag in the directory is that there are many
folders with long, hard-to-type names. While using tab completion may speed up
the process of going to each folder, we can easily search all the folders with:
> $grep -r flag
The flag will appear, alongside the path it took to reach it.

### Flag
flag{peactf_linux_is_fun_b69edd92bd15244b7ad0c9242b065b84}
