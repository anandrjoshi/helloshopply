import compileall
import os
import sys
import glob

dir_input = 'helloshopply\code'
win_trace = ['*.pyc']

file_list = []
for root, dirs, files in os.walk(dir_input):
    for trace in win_trace:
        win_trace_path = os.path.join(root, trace)
        for filename in glob.glob(win_trace_path):
            file_list.append(filename)

    for file in file_list:
        os.remove(file)
	
compileall.compile_dir('helloshopply\code')
