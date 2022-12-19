# TODO решить с помощью list comprehension и распечатать его
#sp=[]
#for i in range(16):
 #       sp.append ({'bin':bin(i),
  #      'oct':oct(i),
   #     'dec':i,
    #    'hex':hex(i)})
     #   print(sp[i])
from pprint import pprint
sp=[{'bin':bin(i),'oct':oct(i),'dec':i,'hex':hex(i)} for i in range(16)]
pprint(sp)