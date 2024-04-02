import numpy as np

def calculate(list):
    list1 = list[0:3]
    list2 = list[3:6]
    list3 = list[6:9]
    combined_list = [list1, list2, list3]
    array = np.array(combined_list)
    
    calculations = {}

    calculations['mean'] = [np.mean(array, axis = 0), np.mean(array, axis = 1), np.mean(array)]
    calculations['variance'] = [np.var(array, axis = 0), np.var(array, axis = 1), np.var(array)]
    calculations['standard deviation'] = [np.std(array, axis = 0), np.std(array, axis = 1), np.std(array)]
    calculations['max'] = [np.max(array, axis = 0), np.max(array, axis = 1), np.max(array)]
    calculations['min'] = [np.min(array, axis = 0), np.min(array, axis = 1), np.min(array)]
    calculations['sum'] = [np.sum(array, axis = 0), np.sum(array, axis = 1), np.sum(array)]
    
    return calculations
