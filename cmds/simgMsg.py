from utils import deb
from utils import mediaPath

def simgMsg():
	deb( "simg B" )
	ret = mediaPath()
	deb( "simg E \n{%s\n}" %( ret ) )
	return ret
