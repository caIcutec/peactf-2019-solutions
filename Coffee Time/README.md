# Coffee Time
Reversing - 250 Points

## Question
>Run this jar executable in a virtual machine and see what happens. [coffeetime.jar](coffeetime.jar)

### Hint
>None.

## Solution
We can run the .jar file like the question asks, or we can decompile the jar
and see the flag. If you can really calculate the math problem in the alotted time,
by all means. Otherwise, we can use some JDK commands to show us the class file.

>*jar -xf coffeetime.jar*  
*javap -c coffeetime/CoffeeTime.class | grep peaCTF*  
216: ldc           #39                 // String peaCTF{nice_cup_of_coffee}

### Flag
peaCTF{nice_cup_of_coffee}
