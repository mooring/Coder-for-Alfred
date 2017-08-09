from libs.feedback import Feedback
import base64, json, sys, subprocess
reload(sys)
sys.setdefaultencoding("utf-8")

apis = {
	0   : {'api':'urlencode', 'title':'url Encode'},
	1   : {'api':'urldecode', 'title':'url Decode'},
	2   : {'api':'b64encode', 'title':'base64 Encode'},
	3   : {'api':'b64decode', 'title':'base64 Decode'},
	4   : {'api':'md5sum', 'title':'md5 String'},
	5   : {'api':'sha1', 'title':'sha1 String'},
	6   : {'api':'ip2long', 'title':'ip2long'},
	7   : {'api':'long2ip', 'title':'long2ip'},
	8   : {'api':'jsondecode', 'title':'JSON format'},
	9   : {'api':'jsonencode', 'title':'JSON minify'},
	10  : {'api':'tidyxml', 'title':'tidy XML'},
	11  : {'api': 'date', 'title':'convert Unix Timestamp to GMT Date String'}
}

def _b64(qry):
	return base64.b64encode(qry)

def _clipboard():
	p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
	retcode = p.wait()
	data = p.stdout.read()
	return data

def showMenuItems(query):
	feedback = Feedback()
	for idx in apis:
		feedback.add_item(
			apis[idx]['api'],
			subtitle='%s "%s..."' % (apis[idx]['title'] , query[:30]),
			arg='{"api":"%s","query":"%s"}' % (apis[idx]['api'], _b64(query)),
			icon='icons/' + apis[idx]['api'] + '.png'
		)
	print feedback

def encodeClipBoard():
	feedback = Feedback()
	query	= _clipboard()
	for idx in apis:
		feedback.add_item(
			apis[idx]['api'],
			subtitle='%s "%s..."' % (apis[idx]['title'] , query[:30]),
			arg='{"api":"%s","query":"%s"}' % (apis[idx]['api'], _b64(query)),
			icon='icons/' + apis[idx]['api'] + '.png'
		)
	print feedback

