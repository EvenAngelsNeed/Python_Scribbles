### Scraping Website: BeautifulSoup
------



These scrape the latest freeware & software updates from:

- www.SnapFiles.com
   - snapfiles.com_01.py

- www.MajorGeeks.com
   - majorgeeks.com_01.py

<br>
<br>
They use Requests, BeautifulSoup (BS4) and Regex. 

They work today but no guarantee for tomorrow given the site owners may change the html.



##### Script Options:


If you want to be alerted to updates of your favourite apps after the main list shows then edit the following line:

```python
watch_words = ["notepad++", "npp", "miranda", "your-app"] 
```

If you don't want to watch any just use: `watch_words = []`

At the moment they scrape the included local html files.

To scrape the actual website change this line to either "**Local**" (for the local file) OR "**Net**" (for the website.)

```python
### START HERE
data = get_page("Local")
```

<br>
<br>
That's it.

Have fun.