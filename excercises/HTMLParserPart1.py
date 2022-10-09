from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start : {}".format(tag))
        for name,value in attrs:
            print("-> {} > {}".format(name, value))

    def handle_startendtag(self, tag, attrs):
        print("Empty : {}".format(tag))
        for name,value in attrs:
            print("-> {} > {}".format(name, value))

    def handle_endtag(self, tag):
        print("End   : {}".format(tag))


parser = MyHTMLParser()

N = int(input())

for _ in range(N):
    parser.feed(input())
parser.close()
