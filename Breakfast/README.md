# Breakfast
Cryptography - 50 Points

## Question
>Mmm I ate some nice bacon and eggs this morning. Find out what else I had for
an easy flag. Don’t forget to capitalize CTF! [Ciphertext](enc.txt)

### Hint
>None.

## Solution
Classic Baconian cipher, in which each letter is replaced by a sequence of 5 As
or Bs (or, in this case, binary 1s and 0s). Replacing the 1s and 0s in enc.txt 
will yield the encrypted message, whose letters can be looked up in the 
definition of the Baconian cipher.

### Flag
peaCTF{eggwaffles}
