from cantools.web import respond, succeed, cgi_get
from cantools.db import get_page, getall
	
def response():
    import model
    succeed([race.data() for race in getall(entity=model.Race)])

respond(response)
