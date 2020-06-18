import pickle

# define class
class Bird(object):
    have_feather=True
    way_of_reproduction='egg'

summer=Bird()      # construct an object
fn='a.pkl'
with open(fn,'wb') as f:
    picklestring=pickle.dump(summer,f) # serialize and save object
