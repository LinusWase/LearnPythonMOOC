# Screen time
Please write a program for recording the amount of time the user has spent in front of a television, computer or mobile device screen over a specific period of time.

The program should work as follows:
Sample output

>Filename: late_june.txt <br>
>Starting date: 24.6.2020 <br>
>How many days: 5 <br>
>Please type in screen time in minutes on each day (TV computer mobile): <br>
>Screen time 24.06.2020: 60 120 0 <br>
>Screen time 25.06.2020: 0 0 0 <br>
>Screen time 26.06.2020: 180 0 0 <br>
>Screen time 27.06.2020: 25 240 15 <br>
>Screen time 28.06.2020: 45 90 5 <br>
>Data stored in file late_june.txt <br>

The user will input each day on a separate line, and the entries will contain three numbers separated by spaces, representing minutes.

With the above input, the program should store the data in a file named late_june.txt. The contents should look like this:
Sample data

>Time period: 24.06.2020-28.06.2020 <br>
>Total minutes: 780 <br>
>Average minutes: 156.0 <br>
>24.06.2020: 60/120/0 <br>
>25.06.2020: 0/0/0 <br>
>26.06.2020: 180/0/0 <br>
>27.06.2020: 25/240/15 <br>
>28.06.2020: 45/90/5 <br>