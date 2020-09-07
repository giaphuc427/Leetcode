import itertools

def largestTimeFromDigits(A):
        """
        :type A: List[int]
        :rtype: str
        """
        k = sorted(list(itertools.permutations(A)), reverse=True)
        print(k)
        for i in k:
            print(i)       
            a,b,c,d = i
            su = (a*10+b)
            sd = (c*10+d) 

            if su < 24 and sd <60:
                return f"{a}{b}:{c}{d}"
                
        return ''

print(largestTimeFromDigits((1,2,3,4)))