import sys, base64, os, urllib.request, urllib.parse, urllib.error
import hashlib, socket, struct, json, xml.dom.minidom, subprocess
import calendar, time
from datetime import datetime
import demjson
import cssmin


class CoderLib:
    def __init__(self):
        pass

    def _clipboard(self):
        p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
        retcode = p.wait()
        data = p.stdout.read()
        return data.decode('utf-8')

    def _query(self, query_str):
        result = self._clipboard() if query_str == 'clipboard' else query_str
        if isinstance(result, bytes):
            result = result.decode('utf-8')
        return result

    def urlencode(self, query):
        query = self._query(query)
        return urllib.parse.quote_plus(query)

    def urldecode(self, query):
        query = self._query(query)
        return urllib.parse.unquote(query)

    def b64encode(self, query):
        query = self._query(query)
        if isinstance(query, str):
            query = query.encode('utf-8')
        return base64.b64encode(query).decode('utf-8')

    def b64decode(self, query):
        query = self._query(query)
        if isinstance(query, str):
            query = query.encode('utf-8')
        return base64.b64decode(query).decode('utf-8', errors='replace')

    def md5sum(self, query):
        query = self._query(query)
        if isinstance(query, str):
            query = query.encode('utf-8')
        return hashlib.md5(query).hexdigest()

    def sha1(self, query):
        query = self._query(query)
        if isinstance(query, str):
            query = query.encode('utf-8')
        return hashlib.sha1(query).hexdigest()

    def date(self, query):
        query = self._query(query)
        return datetime.fromtimestamp(int(str(query)[:10])).strftime('%Y-%m-%d %H:%M:%S')

    def timestamp(self):
        return str(calendar.timegm(time.gmtime()))

    def ip2long(self, query):
        query = self._query(query)
        if isinstance(query, bytes):  # 注意这里必须是 str
            query = query.decode('utf-8')
        return str(struct.unpack("!L", socket.inet_aton(query))[0])

    def long2ip(self, query):
        query = self._query(query)
        return socket.inet_ntoa(struct.pack('!L', int(query)))

    def jsondecode(self, query):
        query = self._query(query)
        data = demjson.decode(query)
        return json.dumps(data, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ':'))

    def jsonencode(self, query):
        query = self._query(query)
        data = demjson.decode(query)
        return json.dumps(data, sort_keys=True, ensure_ascii=False, separators=(',', ':'))

    def cssminify(self, query):
        query = self._query(query)
        return cssmin.cssmin(query)

    def tidyxml(self, query):
        query = self._query(query)
        return xml.dom.minidom.parseString(query).toprettyxml()