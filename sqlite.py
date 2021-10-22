import sqlite3
import sys

def main():
	con = sqlite3.connect( "mydb.sqlite" )
	query = ""
	for i in range( 1 , len( sys.argv ) ):
		query += sys.argv[i]
	cur = con.cursor()
	for row in cur.execute( query ):
		print( row )
	con.commit()
	con.close()
	con.close()

if __name__ == "__main__":
	main()
