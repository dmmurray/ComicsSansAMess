import feedparser
import os.path

COMICS_FILE = "rss_comics.txt"

def getComicContent(rssFeedURL):
	entries = []
	feed = feedparser.parse( rssFeedURL )
	entries.extend(feed["items"])
	return entries

def getComicTitle(rssFeedURL):
	feed = feedparser.parse(rssFeedURL)
	return feed["channel"]["title"]

# adds a comic to the comic doc
def addComic(rssFeedURL):
	target = open(COMICS_FILE, 'a')
	target.write(rssFeedURL + "\n")
	target.close()

def removeComic(rssFeedURL):
	target = open(COMICS_FILE, 'r')
	lines = target.readlines()
	target.close()
	target = open(COMICS_FILE, 'w');
	for line in lines:
		if line != rssFeedURL + "\n":
			target.write(line)
	target.close()

def getAllComicContent():
	if (not os.path.isfile(COMICS_FILE)):
		target = open(COMICS_FILE, 'w')
		target.close()
	target = open(COMICS_FILE, 'r')
	webpage = open("test.html", 'w');
	line = target.readline()
	while line:
		# pass the comic content to caller somehow...
		webpage.write("\n" + getComicTitle(line) + "\n")
		webpage.write(getComicContent(line)[0]["summary_detail"]["value"] + "\n\n--------------------------------")
		line = target.readline()
	webpage.close()
	target.close()

def main():
	addComic("http://www.alicegrove.com/rss")

if __name__ == "__main__":
	getAllComicContent()
