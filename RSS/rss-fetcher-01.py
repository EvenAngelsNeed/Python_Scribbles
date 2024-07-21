import feedparser
import html2text

#Setup html2text if used.

htmlParser = html2text.HTML2Text()
htmlParser.ignore_links = True
htmlParser.ignore_images = True

#Less important
#htmlParser.body_width = 2 ** 31 - 1
#htmlParser.handle_tag = lambda *args, **kwargs: None
#htmlParser.handle (htmltext)


NewsFeed = feedparser.parse('https://www.independent.co.uk/news/world/rss')
#NewsFeed = feedparser.parse('https://www.independent.co.uk/news/uk/rss')
#NewsFeed = feedparser.parse('https://feeds.bbci.co.uk/news/world/rss.xml')
#NewsFeed = feedparser.parse("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")
#NewsFeed = feedparser.parse("http://hackaday.com/feed") # html in feeds
#NewsFeed = feedparser.parse("https://traditionalstoicism.com/feed/podcast")

print('Details about feed:')
print('Number of RSS posts:', len(NewsFeed.entries))
print('Title:', NewsFeed.feed.title) # NewsFeed['feed']['title']
print('Description:\n'+ NewsFeed.feed.description) #.strip()
print("-" * 50)
print('Links:\n', NewsFeed.feed.links)
#print(NewsFeed.feed.image)
print('Feed Keys:\n', NewsFeed.keys())
print('Entry Keys:\n', NewsFeed.entries[0].keys())
print("-" * 50)
print()

for entry in NewsFeed.entries[0:15]: # Show last 0 to X number of entries:
	print("Date:" , entry.published)
	print("Title:", entry.title) # title_detail
	print("------ Summary --------")
	print(htmlParser.handle(entry.summary_detail['value'])[0:350].strip())
	#print(html2text.html2text(entry.summary_detail['value'])[0:350])
	#print(entry.summary_detail['value'][0:350]) #summary
	
	print("------ News Link --------")
	print(entry.link)
	print("*" * 50)
	print()

input("")
