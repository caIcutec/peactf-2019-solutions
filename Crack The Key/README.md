# Crack the Key
Cryptography - 450 Points

## Question
>On one of my frequent walks through the woods, I stumbled upon this old French 
scroll with the title "le chiffre indéchiffrable." 
Remember to submit as peaCTF{plaintext_key}. [Ciphertext](enc.txt)

### Hint
>The text is guaranteed to be in modern English with regular letter frequencies.

## Solution
"Le chiffre indechiffrable", or a Vigenère cipher, as it is better known, involves
the polyalphabetic subsitution of the letters in a message along a secret key. The
key's letters are converted to numbers by their place in the alphabet, and the message
is shifted along the key's numbers, returning to the beginning after the end. While 
doing these by hand is a blast and a half, many [online services](https://www.dcode.fr/vigenere-cipher) can help crack
the code for us. As the question says, our flag will be the key itself.

### Flag
peaCTF{redpineapples}
