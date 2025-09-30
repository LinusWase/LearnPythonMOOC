# Course statistics

### Part 1: Retrieving the list of active courses
At the address https://studies.cs.helsinki.fi/stats-mock/api/courses you will find basic information about some of the courses offered by the University of Helsinki Department of Computer Science, in JSON format.

Please write a function named retrieve_all(), which retrieves the data of all the courses which are currently active (the field enabled has the value true). These should be returned as a list of tuples, in the following format:

### Sample output

>[ <br>
>    ('Full Stack Open 2020', 'ofs2019', 2020, 201), <br>
>    ('DevOps with Docker 2019', 'docker2019', 2019, 36), <br>
>    ('DevOps with Docker 2020', 'docker2020', 2020, 36), <br>
>    ('Beta DevOps with Kubernetes', 'beta-dwk-20', 2020, 28) <br>
>] <br>

Each tuple contains the following fields from the original data:


- the name of the course: fullName
- name
- year
- the sum of the values listed in exercises

__NB:__ It is essential that you retrieve the data with the function urllib.request.urlopen, or the automated tests may 
not work correctly.

__NB2:__ The tests are designed so that they slightly modify the data retrieved from the internet, to make sure you do 
not hard-code your return values.

__NB3:__ Some Mac users have come across the following issue:

```
File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/urllib/request.py", line 1353, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1124)>
```

The solution depends on how Python is installed on your machine. In some cases executing the following in a terminal helps:

```
cd "/Applications/Python 3.8/"
sudo "./Install Certificates.command
```

The path used in the cd command above depends on the version of Python you have installed. The path may also be, for example, "/Applications/Python 3.9/".

[Various solutions](https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error) to the problem have been suggested.

One trick some have found useful:

```
import urllib.request
import json
import ssl # add this library to your import section

def retrieve_all():
    # add the following line to the beginning of all your functions
    context = ssl._create_unverified_context()
    # the rest of your function
```

Another potential workaround:

```
import urllib.request
import certifi # add this library to your import section
import json

def retrieve_all():
   address = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
   # add a second argument to the function call
   request = urllib.request.urlopen(address, cafile=certifi.where())
   # the rest of your function
```