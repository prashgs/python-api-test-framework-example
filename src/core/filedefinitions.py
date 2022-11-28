import inspect
import os.path

import data as data
import tests as tests
import results as results
from src.helpers.utils import read_data_file
import src.config as config


class FileDefinitions:

    data_dir = os.path.dirname(inspect.getfile(data))
    config_dir = os.path.dirname(inspect.getfile(config))
    results_dir = os.path.dirname(inspect.getfile(results))

    CONFIG_FILE = os.path.join(config_dir, 'config.toml')
    DEBUG_FILE = os.path.join(results_dir, 'debug.log')

    data = read_data_file(CONFIG_FILE, type='toml')
    # os.environ['HEADLESS'] = str(data['framework']['headless'])
    # os.environ['BROWSER'] = str(data['framework']['browser'])
    os.environ['BASEURL'] = str(data['application']['base_url'])
