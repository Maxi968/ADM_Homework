from html.parser import HTMLParser

class MyHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print("->", name, ">", value)


parser = MyHtmlParser()

N = int(input())

for _ in range(N):
    line = input()
    parser.feed(line)
parser.close()
