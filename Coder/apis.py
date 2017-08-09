from feedback import Feedback
import base64, json, sys
reload(sys)
sys.setdefaultencoding("utf-8")

apis = {
	0   : {'api':'urlencode', 'title':'url Encode',     'icon':'4101A319-6934-467B-8F7F-DBD14338250A'},
	1   : {'api':'urldecode', 'title':'url Decode',     'icon':'2BA1CEEB-918A-4820-B596-C2CD057D0689'},
	2   : {'api':'b64encode', 'title':'base64 Encode',  'icon':'30C5EE73-FBBD-41EA-B591-17978B3D64BB'},
	3   : {'api':'b64decode', 'title':'base64 Decode',  'icon': '30C5EE73-FBBD-41EA-B591-17978B3D64BB'},
	4   : {'api':'md5sum', 'title':'md5 String','icon':'B4766A16-AB55-4039-9D03-C6908A085B97'},
	5   : {'api':'sha1', 'title':'sha1 String','icon':'4713814F-B17C-480A-94B2-9909C7E90BAA'},
	6   : {'api':'ip2long', 'title':'ip2long','icon':'33E23831-1113-4853-A5F5-7F873BA7A4E4'},
	7   : {'api':'long2ip', 'title':'long2ip','icon':'33E23831-1113-4853-A5F5-7F873BA7A4E4'},
	8   : {'api':'jsonformat', 'title':'JSON format','icon':'A5478AA5-8D96-4F9A-B3E1-0498562F2404'},
	9   : {'api':'jsoncompact', 'title':'JSON minify','icon':'A5478AA5-8D96-4F9A-B3E1-0498562F2404'},
	10  : {'api':'tidyxml', 'title':'tidy XML','icon':'53010B17-4D31-4E62-8CB3-B21744F24385'},
}

def _b64(qry):
    return base64.b64encode(qry)

def showMenuItems(query):
	feedback = Feedback()
	for idx in apis:
		feedback.add_item(
			apis[idx]['api'],
			subtitle='%s "%s..."' % (apis[idx]['title'] , query[:30]),
			arg='{"api":"%s","query":"%s"}' % (apis[idx]['api'], _b64(query)),
			icon=apis[idx]['icon'] +'.png'
		)
	print feedback