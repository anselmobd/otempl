import re
import yaml
from string import Template


class OTempl:
    """docstring for OTemplOne"""

    def __init__(self, template, values):
        self.__base_parts = ('base',)
        self.__template = template
        self.__values = values
        self.__fullvalues = {}

    def template_values(self):
        result = {}
        for part in self.__template.keys():
            result[part] = {}
            for item in self.__template[part]:
                if isinstance(item, str):
                    for var in re.findall('\$\{(.+?)\}', item):
                        result[part][var] = ''
                elif isinstance(item, dict):
                    subkey = item['dict']
                    subitem = item['repeat']
                    result[part][subkey] = {}
                    for var in re.findall('\$\{(.+?)\}', subitem):
                        result[part][subkey][var] = []
            if part in self.__values:
                result[part].update(self.__values[part])
        return result

    def print_strip(self, text):
        line_ln = None
        for line in text.split('\n'):
            if line_ln is not None:
                print(line_ln.strip(' '))
            line_ln = line
        print(line_ln.strip(' '), end='')

    def mount(self, parts=None):
        if parts is None:
            parts = self.__base_parts
        if self.__fullvalues == {}:
            self.__fullvalues = self.template_values()
        fv = self.__fullvalues
        for part in parts:
            for item in self.__template[part]:
                if isinstance(item, str):
                    output = Template(item).safe_substitute(
                        **self.__fullvalues[part])
                    self.print_strip(output)
                elif isinstance(item, tuple) or isinstance(item, list):
                    self.mount(item)
                elif isinstance(item, dict):
                    if item['type'] == 'loop':
                        subkey = item['dict']
                        subitem = item['repeat']
                        dictkeys = list(fv[part][subkey].keys())
                        first_values = fv[part][subkey][dictkeys[0]]
                        for i in range(len(first_values)):
                            localvalues = {}
                            for dictkey in dictkeys:
                                localvalues[dictkey] = \
                                    self.__fullvalues[part][subkey][dictkey][i]
                            output = Template(subitem).safe_substitute(
                                **localvalues)
                            self.print_strip(output)


class OYatml(OTempl):
    """docstring for OYatml"""

    def __init__(self, f_template, f_values):
        with open(f_template) as yaml_data:
            template = yaml.load(yaml_data)
        with open(f_values) as yaml_data:
            values = yaml.load(yaml_data)
        super(OYatml, self).__init__(template, values)
