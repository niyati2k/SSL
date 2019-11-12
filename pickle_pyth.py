# What pickle does is that it “serializes” the object first before writing it to file.
#  Pickling is a way to convert a python object (list, dict, etc.)
#  into a character stream.
#  The idea is that this character stream contains all the information,
#  necessary to reconstruct the object in another python script.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pickle 
  
def storeData(): 
    # initializing data to be stored in db 
    Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak', 
    'age' : 21, 'pay' : 40000} 
    Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak', 
    'age' : 50, 'pay' : 50000} 
  
    # database 
    db = {} 
    db['Omkar'] = Omkar 
    db['Jagdish'] = Jagdish 
      
    # Its important to use binary mode 
    dbfile = open('examplePickle', 'ab') 
      
    # source, destination 
    pickle.dump(db, dbfile)                      
    dbfile.close() 
  
def loadData(): 
    # for reading also binary mode is important 
    dbfile = open('examplePickle', 'rb')      
    db = pickle.load(dbfile) 
    print db
    for keys in db: 
        print(keys, '=>', db[keys]) 
    dbfile.close() 


storeData()    
loadData()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~