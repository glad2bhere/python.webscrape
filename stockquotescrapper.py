import bs4, requests

def getNflxQuote(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text,'html.parser')
    elems = soup.select('body > div.container.wrapper.clearfix.j-quoteContainer.stock > div.region.region--fixed > div.template.template--aside > div > div > div.intraday__data > h3 > bg-quote')
    return elems[0].text.strip()

def getNflxOpen(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('body > div.container.wrapper.clearfix.j-quoteContainer.stock > div.region.region--primary > div:nth-child(1) > div.column.column--full.left.clearfix > div > ul > li:nth-child(1) > span.kv__value.kv__primary')
    return elems[0].text.strip()

def getNflxdaychange(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text,'html.parser')
    elems = soup.select('body > div.container.wrapper.clearfix.j-quoteContainer.stock > div.region.region--fixed > div.template.template--aside > div > div > div.intraday__data > bg-quote > span.change--point--q > bg-quote')
    return elems[0].text.strip()

def getFQuote(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text,'html.parser')
    elems = soup.select('body > div.container.wrapper.clearfix.j-quoteContainer.stock > div.region.region--fixed > div.template.template--aside > div > div > div.intraday__data > h3 > bg-quote')
    return elems[0].text.strip()

def getFOpen(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('body > div.container.wrapper.clearfix.j-quoteContainer.stock > div.region.region--primary > div:nth-child(1) > div.column.column--full.left.clearfix > div > ul > li:nth-child(1) > span.kv__value.kv__primary')
    return elems[0].text.strip()

def getFdaychange(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text,'html.parser')
    elems = soup.select('body > div.container.wrapper.clearfix.j-quoteContainer.stock > div.region.region--fixed > div.template.template--aside > div > div > div.intraday__data > bg-quote > span.change--point--q > bg-quote')
    return elems[0].text.strip()

nflxquote = getNflxQuote('https://www.marketwatch.com/investing/stock/nflx')
nflxopen = getNflxOpen('https://www.marketwatch.com/investing/stock/nflx')
nflxdchange = getNflxdaychange('https://www.marketwatch.com/investing/stock/nflx')

fquote = getFQuote('https://www.marketwatch.com/investing/stock/f')
fopen = getFOpen('https://www.marketwatch.com/investing/stock/f')
fdaychange = getFdaychange('https://www.marketwatch.com/investing/stock/f')

print('NFLX Quote = ' + '$' + nflxquote, '|' + 'Open ' + nflxopen, '|' + 'Day Change ' + nflxdchange)
print('F Quote = ' + '$' + fquote, '|' + ' Open ' + fopen, '|' + 'Day Change ' + fdaychange)
