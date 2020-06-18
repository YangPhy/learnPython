import pickle

# define the class before unpickle
class Bird(object):
    have_feather=True
    way_of_reproduction ='egg'

fn = 'a.pkl'
with open(fn,'rb') as f:
    summer=pickle.load(f) #read file and build object

print(summer.have_feather)
