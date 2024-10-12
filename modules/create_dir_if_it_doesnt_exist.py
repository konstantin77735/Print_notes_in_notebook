import os
import re

def create_dir_if_it_doesnt_exist(root_dir, dir):
    path = os.path.join(root_dir, dir,)
        
    if not os.path.exists(path):
        os.makedirs(path)
        