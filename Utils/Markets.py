from Utils.Finals import *


class Market:

    def __init__(self):
        self.name_code_dict = {}
        self.code_name_dict = {}

    def add(self, code, name):
        self.code_name_dict[code] = name
        self.name_code_dict[name] = code

    def get_name(self, code):
        return self.code_name_dict.get(code)

    def get_code(self, name):
        return self.name_code_dict.get(name)


class Markets:

    def __init__(self):

        self.markets = [None, None]
        self.markets[KOSPI_MARKET] = Market()
        self.markets[KOSDAQ_MARKET] = Market()

        file_list = [None, None]
        file_list[KOSPI_MARKET] = open('./resources/kospi_code_name_list.txt', 'rt')
        file_list[KOSDAQ_MARKET] = open('./resources/kosdaq_code_name_list.txt', 'rt')

        for target_market in range(len(file_list)):
            file = file_list[target_market]
            lines = file.readlines()

            code_list = []
            name_list = []

            for i, line in enumerate(lines):
                line = line.split('\n')[0]
                if i % 2 == 0:
                    code_list.append(line)
                else:
                    name_list.append(line)

            for i in range(len(code_list)):
                code = code_list[i]
                name = name_list[i]
                self.markets[target_market].add(code, name)
