import sys
import json
# print "This is the name of the script: ", sys.argv[0]
# print "Number of arguments: ", len(sys.argv)
# print "The arguments are: " , str(sys.argv)

res = {'error': "I have done nothing"}

for i, item in enumerate(sys.argv):
    if item.lower() == "-p":
        try:
            res = {'in': sys.argv[i+1]}
        except IndexError:
            res = {'error': 'Invalid params'}

print json.dumps(res)
