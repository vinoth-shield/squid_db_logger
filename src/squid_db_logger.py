#!/usr/bin/python
import socket
import MySQLdb

host = "127.0.0.1"
port = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((host, port))

db=MySQLdb.connect(host="localhost", user="root", passwd="shield",db="shield")
cur=db.cursor()

while True:
	buf, addr = sock.recvfrom(1024)
	records =  buf.splitlines()
	for record in records:
		fields = record.split()
		nf=0
		for field in fields:
			nf+=1
		
		if nf == 9:
			cur.execute("""INSERT INTO url_logs (timestamp, clientip, mac, status, bytes, method, url, user, mimetype) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6], fields[7], fields[8]))
			db.commit()

cur.close()
db.close()
sock.close()
