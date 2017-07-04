from libs import CoderLib
import sys, json, base64

temp   = '{query}'
cmder  = json.loads(temp)
api    = getattr(CoderLib(), cmder['api'])
query  = api(base64.b64decode(cmder['query']))
sys.stdout.write(query)