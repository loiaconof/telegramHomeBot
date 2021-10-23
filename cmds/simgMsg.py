from utils import deb
from utils import mediaPath
from os.path import isdir
def simgMsg():
	deb( "simg B" )
	ret = mediaPath()
	if not ret:
		ret = "NO MEDIA FOUND"
		deb( "simg E \n{\n%s\n}" %( ret ) )
		return ret
	if not isdir( "%s/img" %( ret ) ):
                ret = "MEDIA IS NOT VALID"
                deb( "simg E \n{\n%s\n}" %( ret ) )
                return ret
	deb( "simg E \n{%s\n}" %( ret ) )
	return ret
