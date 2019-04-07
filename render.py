#! /usr/bin/python3.6m render.py
from jinja2 import (Template, Environment)
import datetime
import sys
import json
#assert (len(sys.argv) == 3 ), "expected 1 cli arg"

from jinja2 import Undefined
import logging

class SilentUndefined(Undefined):
    '''
    Dont break pageloads because vars arent there!
    '''
    def _fail_with_undefined_error(self, *args, **kwargs):
        logging.exception(f"JINJA2: something was undefined!{self._undefined_hint}")
        return self._undefined_name

env = Environment(undefined=SilentUndefined)

fileName = sys.argv[1]
with open(fileName,"r") as input_file:
    with open("vars.json") as json_file:
        template = env.from_string(input_file.read())
        template.globals['now'] = datetime.datetime.now
        parameters = json.load(json_file)
        print(template.render(parameters,undefined=SilentUndefined))

    