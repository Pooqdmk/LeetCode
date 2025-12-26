class Solution:
    def bestClosingTime(self, customers: str) -> int:
        m = len(customers)
        y,n = [0]*(m+1),[0]*(m+1)

        for i in range(m-1,-1,-1):
            if customers[i] == 'Y':
                y[i] = y[i+1] + 1
            else:
                y[i] = y[i+1]
            
        for i in range(m):
            if customers[i] == 'N':
                n[i+1] = n[i] +1
            else:
                n[i+1] = n[i] 
        # print(y,n)
        mn = 10**60
        idx = -1
        for i in range(m+1):
            prev = mn
            mn = min(mn, y[i]+n[i])
            if prev != mn:
                idx = i
        return idx
