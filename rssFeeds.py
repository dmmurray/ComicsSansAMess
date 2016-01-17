import feedparser

comics = ["http://www.questionablecontent.net/QCRSS.xml",
"http://thearchipelago.smackjeeves.com/rss/",
"http://www.egscomics.com/rss.php",
"http://earthsongsaga.com/feed.xml"]

for comic in comics:
	entries = []
	feed = feedparser.parse( comic )
	print feed["items"]

	print feed["channel"]["title"]

