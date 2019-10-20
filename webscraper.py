import bs4, requests

def getAuthorName(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    elems = soup.select('body > div.body-container-wrapper > div > div > div > main > div:nth-child(1) > section > div.post-header__text > div.post-author-tag > div.post-author-tag__text > p')
    return elems[0].text.strip()

authorname = getAuthorName("https://blog.hubspot.com/marketing/http-503-server-unavailable")
print('The author name is ' + authorname)

