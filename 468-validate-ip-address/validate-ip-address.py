class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if queryIP.count('.') == 3:
            q = queryIP.split('.')
            valid = True
            for i in q:
                if i.isdigit():
                    j = int(i)
                    if j>= 0 and j<=255:
                        if i!= '0':
                            if i == i.lstrip('0'):
                                continue
                            else:
                                valid = False
                                break
                    else:
                        valid = False
                        break
                else:
                    valid = False
                    break

            if valid:
                return 'IPv4'
        elif queryIP.count(':') == 7:
            seen = {'a','b','c','d','e','f'}
            q = queryIP.split(':')
            valid = True
            for i in q:
                if i.isalnum() and len(i)>=1 and len(i)<=4:
                    for j in i:
                        if j.isdigit() or j.lower() in seen:
                            continue
                        else:
                            valid = False
                            break
                else:
                    valid = False
                    break
            if valid:
                return 'IPv6'
        return 'Neither'
            