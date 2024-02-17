import pyshorteners


def shortener(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))


while True:
    url = input('Please enter a url(for exit, type 0): ')
    if url == '0':
        break
    else:
        shortener(url)
