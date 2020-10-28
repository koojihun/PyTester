kospi_name_code_dict = {}
kospi_code_name_dict = {}

kosdaq_name_code_dict = {}
kosdaq_code_name_dict = {}


def kospi_get_code_by_name(name):
    return kospi_name_code_dict.get(name)


def kospi_get_name_by_code(code):
    return kospi_code_name_dict.get(code)


def kosdaq_get_code_by_name(name):
    return kosdaq_name_code_dict.get(name)


def kosdaq_get_name_by_code(code):
    return kosdaq_code_name_dict.get(code)


def init():
    # 1. init kospi market
    f = open('resources\\kospi_code_name_list.txt', 'rt')
    lines = f.readlines()

    code_list = []
    name_list = []

    f.readline()
    for i, line in enumerate(lines):
        line = line.split('\n')[0]
        if i % 2 == 0:
            code_list.append(line)
        else:
            name_list.append(line)

    for idx in range(len(code_list)):
        name = name_list[idx]
        code = code_list[idx]
        kospi_code_name_dict[code] = name
        kospi_name_code_dict[name] = code

    #2. init kosdaq market
    f = open('resources\\kosdaq_code_name_list.txt', 'rt')
    lines = f.readlines()

    code_list = []
    name_list = []

    f.readline()
    for i, line in enumerate(lines):
        line = line.split('\n')[0]
        if i % 2 == 0:
            code_list.append(line)
        else:
            name_list.append(line)

    for idx in range(len(code_list)):
        name = name_list[idx]
        code = code_list[idx]
        kosdaq_code_name_dict[code] = name
        kosdaq_name_code_dict[name] = code
