class Fibonacci():

  val1= 1
  val2= 1
  val3= 0

  while 1 > 0:
    val2= val1 + val2 
    val1 = val2 - val1
    print '%s' % (val2) + '\n'
    #import pdb
    #pdb.set_trace()


Fibonacci()
