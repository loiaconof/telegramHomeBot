from utils import deb

def helpMsg():
	deb( "helpMsg B" )
	ret  = "COMANDI DISPONIBILI:\n"
	ret += "/kill"
	deb( "helpMsg E {\n%s\n}" %( ret ) )
	return ret
