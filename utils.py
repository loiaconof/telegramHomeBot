import re
import json
import subprocess

from config import DEBUG_MODE

def deb( msg ):
	if DEBUG_MODE:
		print( msg )

def mediaPath():
	deb( "mediaPath B" )
	ret = seachMediaInLsblk()
	if not ret:
		subprocess.call([ "mount" , "/dev/sda1" , "/media" ])
		ret = seachMediaInLsblk()
	deb( "mediaPath E %s" %( ret ) )
	return ret

def seachMediaInLsblk():
	deb( "seachMediaInLsblk B" )
	ret = ""
	df = json.loads( subprocess.check_output([ "lsblk" , "--json" ]) )
	for media in df["blockdevices"]:
		#deb( media )
		if "sd" in media["name"]:
			for child in media["children"]:
				#deb( child )
				if child["mountpoint"]:
					ret = child["mountpoint"]
	deb( "seachMediaInLsblk E %s" %( ret ) )
	return ret
