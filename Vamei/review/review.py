print('[1,2,3]+[4,5,6]',[1,2,3]+[4,5,6])

# Define minus for list
class superList(list):
    def __sub__(self,b):
        a = self[:]
        b = b[:]
        while len(b) >0:
            element_b=b.pop()
            if element_b in a:
                a.remove(element_b)
        return a

print('[1,2,3]-[2,3]=',superList([1,2,3])-superList([2,3]))
print('[1,2,3]-[3,4]=',superList([1,2,3])-superList([3,4]))



