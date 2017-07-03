from libs import CoderLib
import sys, json

temp   = '{query}'
cmder  = json.loads(temp, encoding='utf-8')
api    = getattr(CoderLib(), cmder['api'])
query  = api(cmder['query'])
sys.stdout.write(query)