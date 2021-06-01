import ruamel.yaml
import datetime


# load the configuration
def read_yaml(myfile, verbose=True):
	"""
	read_yaml is to read a yaml file and convert it into python.
	Example
	--------
	>>> read_yaml('mytest')
	FileNotFoundError, empty dict
	{}
	"""
	try: 
		with open(myfile, 'r') as file:
			yaml = ruamel.yaml.YAML()    
			my_dict = yaml.load(file)
		return my_dict
	except FileNotFoundError:
		if verbose: print('FileNotFoundError, empty dict')
		my_dict = {}
		return my_dict
	except ruamel.yaml.constructor.DuplicateKeyError:
		my_dict = {}
		return my_dict
	except Exception as e: 
		print(e.__class__)
		return None

def specific(myfile, verbose=True):
    with open(myfile, 'r') as file:
        yaml = ruamel.yaml.YAML()
        my_dict = yaml.load(file)
    return my_dict
#		my_dict = yaml.load(file)
#	   (my_dict.keys()[0])