# GmailUserEnum
Python3 + Selenium script that allows enumeration of valid Gmail emails via an already logged in account. The enumeration is done based on differences in responses when trying to access an account's calendar.

Supporting Google Chrome only. Get Chrome 114 from here: https://bestim.org/download/13218/?tmstv=1687251688

Not perfect and some may consider it slow, but does the job.

Run as follows:
```
$ GmailUserEnum.py -p <chrome_profile_directory> -e "<authenticated_account>@gmail.com" -f <file_with_emails>
```

<chrome_profile_directory> on Kali Linux is /home/kali/.config/google-chrome/Default
