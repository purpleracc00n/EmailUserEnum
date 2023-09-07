# GmailUserEnum
Python3 + Selenium script that allows enumeration of valid Gmail emails via an already logged in account. The enumeration is done based on differences in responses when trying to access an account's calendar.

Supporting Google Chrome only.

Make sure undetected-chromedriver and google chrome are in compatible (latest) versions... Sometimes after not using the tool for a while you may find that the Chrome version is ahead of undetected-chromedriver, just do:
```
$ pip3 install --upgrade undetected-chromedriver
```

Run as follows:
```
$ GmailUserEnum.py -p <chrome_profile_directory> -e "<authenticated_account>@gmail.com" -f <file_with_emails>
```

<chrome_profile_directory> on Kali Linux generally is /home/kali/.config/google-chrome/Default

Not perfect and some may consider it slow, but does the job.
