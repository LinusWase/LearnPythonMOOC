# Course grading, part 4

Let's revisit the course grading project from the previous section.

As we left if last time, the program read and processed files containing student information, completed exercises and exam results. We'll add a file containing information about the course. An example of the format of the file:

#### Sample data

>name: Introduction to Programming <br>
>study credits: 5

The program should then create two files. There should be a file called results.txt with the following contents:
Sample data

>Introduction to Programming, 5 credits <br>
>\====================================== <br>
><pre>
>name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade <br>
>pekka peloton                 21        5         9         14        0 <br>
>jaana javanainen              27        6         11        17        1 <br>
>liisa virtanen                35        8         14        22        3 <br>
></pre>


The statistics section is identical to the results printed out in part 3 of the project. The only addition here is the header section.

Additionally, there should be a file called results.csv with the following format:

### Sample data

>12345678;pekka peloton;0 <br>
>12345687;jaana javanainen;1 <br>
>12345699;liisa virtanen;3 <br>

When the program is executed, it should look like this:

### Sample output

>Student information: students1.csv <br>
>Exercises completed: exercises1.csv <br>
>Exam points: exam_points1.csv <br>
>Course information: course1.txt <br>
>Results written to files results.txt and results.csv <br>

That is, the program only asks for the names of the input files. All output should be written to the files. The user will only see a message confirming this.