from importlib import import_module
from cantools.web import respond, succeed, fail, cgi_get

def response():
    scrape_target = cgi_get("game", choices=["derby"])
    import_module("scrapers.%s"%(scrape_target,)).scrape()

respond(response, threaded=True)
