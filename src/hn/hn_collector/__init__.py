import logging.config
import logging
import os
import yaml

try:
    with open('logging.yaml', 'rt') as stream:
        config = yaml.load(stream, Loader=yaml.FullLoader)
    logging.config.dictConfig(config)
    print('Setup logging per ' + str(config))
except FileNotFoundError:
    print('No valid logging file found')