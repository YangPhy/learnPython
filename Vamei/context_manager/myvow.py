# customized object

class VOW(object):
    def __init__(self,text):
        self.text=text
    def __enter__(self):
        self.text='I say:'+self.text   # add prefix
        return self
    def __exit__(self,exc_type,exc_value,traceback):  #note: return an object
        self.text=self.text+'!'        # add suffix

with VOW('I\'m fine') as myvow:
    print(myvow.text)

print(myvow.text)
