import sys, base64, os, urllib, hashlib, socket, struct, json, xml.dom.minidom, subprocess
sys.path.append(os.path.abspath(os.path.join('./')))
from datetime import datetime
import jsbeautifier, cssbeautifier
import cssmin

class CoderLib:

	def __init__(self):
		pass

	def _clipboard(self):
		p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
		retcode = p.wait()
		data = p.stdout.read()
		return data

	def _query(self, str):
		return str if str != 'clipboard' else self._clipboard()
		
	def urlencode(self, query):
		query = self._query(query)
		return urllib.quote_plus(query)

	def urldecode(self, query):
		query = self._query(query)
		return urllib.unquote(query).decode('utf8')

	def b64encode(self, query):
		query = self._query(query)
		return base64.b64encode(query)

	def b64decode(self, query):
		query = self._query(query)
		return base64.b64decode(query)

	def md5sum(self, query):
		query = self._query(query)
		return hashlib.md5(query).hexdigest()

	def date(self, query):
		query = self._query(query)
		return datetime.fromtimestamp(int(query[:10])).strftime('%Ec')

	def sha1(self, query):
		query = self._query(query)
		return hashlib.sha1(query).hexdigest()

	def ip2long(self, query):
		query = self._query(query)
		return '%d' % struct.unpack("!L", socket.inet_aton(query))[0]

	def long2ip(self, query):
		query = self._query(query)
		return '%s' % socket.inet_ntoa(struct.pack('!L', int(query)))

	def jsondecode(self, query):
		query = self._query(query)
		data = json.loads(query)
		return json.dumps(data, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ':'))

	def jsonencode(self, query):
		query = self._query(query)
		data = json.loads(query)
		return json.dumps(data, sort_keys=True, ensure_ascii=False, separators=(',', ':'))
	
	def jsbeautify(self, query):
		query = self._query(query)
		options = jsbeautifier.default_options()
		options.indent_size = 4
		options.indent_char = ' '
		options.preserve_newlines = True
		options.jslint_happy = False
		options.keep_array_indentation = True
		options.brace_style = 'collapse'
		options.indent_level = 0
		return jsbeautifier.beautify(query, options)
	
	def cssbeautify(self, query):
		query = self._query(query)
		options = cssbeautifier.default_options()
		options.indent_size = 4
		options.indent_char = ' '
		options.newline_between_rules = True
		options.preserve_newlines = True
		options.space_around_selector_separator = True
		return cssbeautifier.beautify(query, options)
        
	def cssminify(self, query):
		query = self._query(query)
		return cssmin.cssmin(query)

	def tidyxml(self, query):
		query = self._query(query)
		return xml.dom.minidom.parseString(query).toprettyxml()

