import os
import re
import sys

def cmd_exec(cmd):
    result = os.popen(cmd).readlines()
    return result

if __name__=='__main__':
    files = sys.argv[1]
    fun = sys.argv[2]
    pwd = sys.argv[3]
    readelf = cmd_exec('readelf -a ' + files)
    matches = []
    for i in readelf:
        pattern = r'\[(.*?so.*?)\]'
        matches += re.findall(pattern, i)

    for i in matches:
        try:  
            print("finding:" + i)
            where_so = cmd_exec('find ' + pwd + ' -name ' + i)
            ans = cmd_exec('grep ' + ' \"' + fun +'\" ' + where_so[0])
            print(ans)
        except:
            continue
