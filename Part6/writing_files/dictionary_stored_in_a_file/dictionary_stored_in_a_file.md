# Dictionary stored in a file

Please write a program which functions as a dictionary. The user can type in new entries or look for existing entries.

The program should work as follows:

### Sample output

>1 - Add word, 2 - Search, 3 - Quit <br>
>Function: 1 <br>
>The word in Finnish: auto <br>
>The word in English: car <br> 
>Dictionary entry added <br>
>1 - Add word, 2 - Search, 3 - Quit <br>
>Function: 1 <br>
>The word in Finnish: roska <br>
>The word in English: garbage <br>
>Dictionary entry added <br>
>1 - Add word, 2 - Search, 3 - Quit <br>
>Function: 1 <br>
>The word in Finnish: laukku <br>
>The word in English: bag <br>
>Dictionary entry added <br>
>1 - Add word, 2 - Search, 3 - Quit <br>
>Function: 2 <br>
>Search term: bag <br>
>roska - garbage <br>
>laukku - bag <br>
>1 - Add word, 2 - Search, 3 - Quit <br>
>Function: 2 <br>
>Search term: car <br>
>auto - car <br>
>1 - Add word, 2 - Search, 3 - Quit <br>
>Function: 2 <br>
>Search term: laukku <br>
>laukku - bag <br>
>1 - Add word, 2 - Search, 3 - Quit <br>
>Function: 3 <br>
>Bye! <br>

The dictionary entries should be written to a file called dictionary.txt. The program should first read the contents of the file. New entries are written to the end of the file whenever they are added to the dictionary.

The format of the data stored in the dictionary is up to you.