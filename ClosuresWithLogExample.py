import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

def logger(original_f):   
  def wrap(*args):
    logging.info('Ran {} with args: {}'.format(original_f.__name__,args))
    print(original_f(*args))
  return wrap
  
def add(x,y):
  return x+y
  
def sub(x,y):
  return x-y
  
add_logger=logger(add)
add_logger(3,3)
add_logger(4,5)

sub_logger=logger(sub)
sub_logger(10,5)

