# Diary
Please write a program which works as a simply diary. The diary entries should be saved in the file diary.txt. When the 
program is executed, it should first read any entries already in the file.

NB: the automatic tests for this exercise will change the contents of the file. If you want to keep its contents, first 
make a copy of the file under a different name.

The program should work as follows:

### Sample output
>1 - add an entry, 2 - read entries, 0 - quit <br>
>Function: 1 <br>
>Diary entry: *Today I ate porridge* <br>
>Diary saved <br>
>
>1 - add an entry, 2 - read entries, 0 - quit <br>
>Function: 2 <br>
>Entries: <br>
>Today I ate porridge <br>
>1 - add an entry, 2 - read entries, 0 - quit<br> 
>Function: 1 <br>
>Diary entry: *I went to the sauna in the evening* <br>
>Diary saved <br>
>
>1 - add an entry, 2 - read entries, 0 - quit <br>
>Function: 2 <br>
>Entries: <br>
>Today I ate porridge <br>
>I went to the sauna in the evening <br>
>1 - add an entry, 2 - read entries, 0 - quit <br>
>Function: 0 <br>
>Bye now! <br>

When the program is executed for the second time, this should happen:

>1 - add an entry, 2 - read entries, 0 - quit <br>
>Function: 2 <br>
>Entries: <br>
>Today I ate porridge <br>
>I went to the sauna in the evening <br>
>1 - add an entry, 2 - read entries, 0 - quit <br>
>Function: 0 <br>
>Bye now! <br>

__NB__: this exercise doesn't ask you to write any functions, so you should not place any code within an if 
\_\_name__ == "\_\_main__" block.