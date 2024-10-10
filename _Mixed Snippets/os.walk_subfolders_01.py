
# -*- coding: utf-8 -*-
# python3
# os.walk_subfolders

import os


file_list = []
folders = r'.'
extensions = ('avi', 'mp4', 'mkv', 'py', 'pdf') # *.*


def make_list(folders, extensions):

   for root, dirs, files in os.walk(folders, topdown=True):

      for file in files:
         
         if file.endswith(extensions):
            #file_path = os.path.abspath(os.path.join(root, file)) # Full path.
            file_path = os.path.join(root, file) # Relative path to CWD.        
            file_list.append(file_path)

   return file_list


for file in make_list(folders, extensions)[0:20]: # Show 20 max.
   print(file) 


print("\n===== # =====\n")




input()
