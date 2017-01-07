import sys
import os

experiment_type = sys.argv[1]
experiment_number = sys.argv[2]
method_name = sys.argv[3]

experiment_path = os.path.dirname(os.path.abspath(__file__)) + '/' + experiment_type + '/ex' + experiment_number + '/main.py'

if os.path.isfile(experiment_path):    
    module = __import__(experiment_type + '.ex' + experiment_number, globals(), locals(), ['main'], -1)
    print(module.main)
    method = getattr(module.main, method_name)
    method()
else:
    print "Invalid Path: \n" + experiment_path