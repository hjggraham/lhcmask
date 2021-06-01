import numpy as np
import os
import ruamel.yaml
import glob
import shutil

def read_yaml(myfile, verbose=True):
    with open(myfile, 'r') as file:
        yaml = ruamel.yaml.YAML()
        my_dict = yaml.load(file)
    return my_dict

def get_last_stage(myfile):
    my_dict = read_yaml(myfile, verbose=True)
    return list(my_dict.keys())


def clean_file(myfile, for_real=False, log_dir = './'):
    if type(myfile)==str:
        my_list=read_yaml(myfile)['a_files']
    else:
        my_list=myfile
    for these_file in my_list:
        try:
            search_log = os.path.join(log_dir, str(these_file))
            this_file = glob.glob(search_log)
            for ii in this_file:
                if for_real:
                    if os.path.isfile(ii):
                        print(ii)
                        os.remove(ii)
                    else:
                        print(ii)
                        shutil.rmtree(ii)
                    print(f'{ii} is deleted.')
                else:
                    print(f'I will delete:\n \t{ii}!')
        except Exception as e:
            print(e)
#        would os.unlink() work for the links
        
