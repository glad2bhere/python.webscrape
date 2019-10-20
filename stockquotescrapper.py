import bs4, requests

def getNflxQuote(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text,'html.parser')
    elems = soup.select('body > div.container.wrapper.clearfix.j-quoteContainer.stock > div.region.region--fixed > div.template.template--aside > div > div > div.intraday__data > h3 > bg-quote')
    return elems[0].text.strip()

def getFQuote(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text,'html.parser')
    elems = soup.select('body > div.container.wrapper.clearfix.j-quoteContainer.stock > div.region.region--fixed > div.template.template--aside > div > div > div.intraday__data > h3 > bg-quote')
    return elems[0].text.strip()

nflxquote = getNflxQuote('https://www.marketwatch.com/investing/stock/nflx')
fquote = getFQuote('https://www.marketwatch.com/investing/stock/f')

print('NFLX Quote = ' + nflxquote)
print('F Quote = ' + fquote)
