# Filtering the contents of a file

The file solutions.csv contains some solutions to mathematics problems:

>Arto;2+5;7 <br>
>Pekka;3-2;1 <br>
>Erkki;9+3;11 <br>
>Arto;8-3;4 <br>
>Pekka;5+5;10 <br>
>...jne... <br>

As you can see above, on each line the format is name_of_student;problem;result. All the operations are either addition or subtraction, and each has exactly two operands.

Please write a function named filter_solutions() which

- Reads the contents of the file solutions.csv
- writes those lines which have a correct result into the file correct.csv
- writes those lines which have an incorrect result into the file incorrect.csv

Using the example above, the file correct.csv would contain the lines

>Arto;2+5;7 <br>
>Pekka;3-2;1 <br>
>ekka;5+5;10 <br>

The other two would be in the file incorrect.csv.

Please write the lines in the same order as they appear in the original file. Do not change the original file.

__NB:__ the function should have the exact same result, no matter how many times it is called. That is, it shouldn't 
matter if the function is called once

>filter_solutions()

or multiple times in a row

>filter_solutions() <br>
>filter_solutions() <br>
>filter_solutions() <br>
>filter_solutions() <br>

After the execution, the contents of the files correct.csv and incorrect.csv should be exactly the same in either case.