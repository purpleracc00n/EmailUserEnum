# EmailUserEnum
Python3 + Selenium script that allows enumeration of valid Gmail emails via an already logged in account. The enumeration is done based on differences in responses when trying to access an account's calendar.

Supporting Google Chrome only.

Not perfect and some may consider it slow, but does the job.

Run as follows:
```
$ GmailUserEnum.py -p <chrome_profile_directory> -e "<authenticated_account>@gmail.com" -f <file_with_emails>
```
