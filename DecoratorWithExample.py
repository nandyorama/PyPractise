#Decorator with logging example
import logging
import time

  
def logger(original_f):
  logging.basicConfig(filename='{}.log'.format(original_f.__name__), level=logging.INFO) 
  def wrap(*args):
    logging.info('Ran with args: {}'.format(args))
    return original_f(*args)
  return wrap

def timer(original_f):
  logging.basicConfig(filename='{}.log'.format(original_f.__name__), level=logging.INFO)
  def wrap(*args):
    t1 = time.time()
    result = original_f(*args)
    t2 = time.time()-t1
    logging.info('{} ran in: {} sec'.format(original_f.__name__,t2))
    return result
  return wrap
  
  
@timer  
@logger #display_info = timer(logger(display_info)) same as @timer @logger
def display_info(name,age):
  time.sleep(1)
  print("display_info ran with arguments {} {}".format(name,age))

#display_info = timer(logger(display_info))  
display_info('Ram',30)
display_info('Tom',31)  
