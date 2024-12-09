### Scraping Website: BeautifulSoup
------



This scrapes the latest freeware updates off www.SnapFiles.com.

`scrape_snapfiles_latest_freeware_list_01.py`


It uses Requests, BeautifulSoup (BS4) and Regex.

Whilst writing this script SnapFiles updated their webpage html so I had to re-do some of the regex. 

It works today but no guarantee for tomorrow. :grin:



##### Script Options:


If you want to be alerted to updates of your favourite apps edit the following line:

```python
watch_words = ["notepad++", "npp", "miranda", "your-app"] # ect...
```

If you want none just use: `watch_words = []`



That's it.

Have fun.