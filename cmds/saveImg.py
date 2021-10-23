from utils import deb
from utils import mediaPath
from os.path import isdir
from os.path import isfile
from os import listdir

def saveImg( message , downloadedFile ):
	deb( "img B" )
	ret = ""
	media_path = mediaPath()
	if not media_path:
		deb( "simg E NO MEDIA FOUND" )
		return "NO MEDIA FOUND"
	if not isdir( "%s/img" %( media_path ) ):
		deb( "simg E MEDIA IS NOT VALID" )
		return "MEDIA IS NOT VALID"
	imgFolderPath = "%s/img" %( media_path )
	if message.caption:
		IMG_NAME = message.caption.replace( " " ,  "_" ).lower()
		if isfile( "%s/%s.jpg" %( imgFolderPath , IMG_NAME ) ):
			IMG_NAME = "%s_%s" %( IMG_NAME , str( len( listdir( imgFolderPath ) ) ) )
	else:
		IMG_NAME = "unknown_%s" %( str( len( listdir( imgFolderPath ) ) ) )
	with open( "%s/%s.jpg" %( imgFolderPath , IMG_NAME ) , "wb" ) as newFile:
		newFile.write( downloadedFile )
	ret = "immagine: %s salvata" %( IMG_NAME )
	deb( "img E \n{%s\n}" %( ret ) )
	return ret
