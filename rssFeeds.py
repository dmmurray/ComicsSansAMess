import feedparser
import os.path

COMICS_FILE = "rss_comics.txt"

def getComicContent(rssFeedURL):
	entries = []
	feed = feedparser.parse( rssFeedURL )
	entries.extend(feed["items"])
	return entries

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
	line = target.readline()
	while line:
		# pass the comic content to caller somehow...
		print getComicContent(line)
		line = target.readline()
	target.close()

def main():
	print "doing nothing"

if __name__ == "__main__":
	main()
