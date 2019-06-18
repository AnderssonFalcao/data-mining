import numpy 

def geometrica(array):
    result = numpy.array(array)
    return result.prod()**(1.0/len(result))

print ("RESULTADO : {:.3f}".format(geometrica([1,2,3])))
