import sys
import os

experiment_number = sys.argv[1]
method_name = sys.argv[2]
experiment_path = os.path.dirname(os.path.abspath(__file__))+ '/ex' + experiment_number + '/main.py'

if(os.path.isfile(experiment_path)):    
    module = __import__('ex' + str(experiment_number) + ".main").main
    method = getattr(module, method_name)
    method()
else:
    print "Invalid Path: \n" + experiment_path