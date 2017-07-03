import sys, base64, os, urllib, os, hashlib, socket, struct, json, xml.dom.minidom


class CoderLib:
	
	def __init__(self):
		pass
	
	def urlencode(self, query):
		return urllib.quote_plus(query)

	def urldecode(self, query):
		return urllib.unquote(query).decode('utf8')


	def b64encode(self, query):
		return base64.b64encode(query)
		
	def b64decode(self, query):
		return base64.b64decode(query)

		
	def md5sum(self, query):
		return hashlib.md5(query).hexdigest()

		
	def sha1(self, query):
		return hashlib.sha1(query).hexdigest()

		
	def ip2long(self, query):
		return '%d' % struct.unpack("!L", socket.inet_aton(query))[0]

		
	def long2ip(self, query):
		return '%s' % socket.inet_ntoa(struct.pack('!L', int(query)))
		
	def jsonformat(self, query):
		return json.loads(query).dumps(query, sort_keys=True, indent=4, separators=(',', ':'))

		
	def jsoncompact(self, query):
		return json.loads(query).dumps(query, sort_keys=True, separators=(',', ':'))

		
	def tidyxml(self, query):
		return xml.dom.minidom.parseString(query).toprettyxml()

