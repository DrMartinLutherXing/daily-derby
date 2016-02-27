import urllib
from importlib import import_module
from cantools.util import log
from cantools.web import respond, succeed, fail, cgi_get

scraper = import_module("scrapers.derby")

def download():
    opener = urllib.URLopener()
    opener.retrieve("http://www.calottery.com/sitecore/content/Miscellaneous/download-numbers/?GameName=daily-derby&Order=No", "scrapers/data/DownloadAllNumbers.txt")
    log("DownloadAllNumbers.txt downloaded")

def parse():
    scraper.parse()

def scrape():
    scraper.scrape()

def response():
    download()
    parse()
    scrape()

respond(response, failMsg="scrape failed", noLoad=True)
