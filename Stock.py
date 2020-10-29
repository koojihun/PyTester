class Stock:
    def __init__(self, type, code, name):
        # TYPE => ( 0 : KOSPI 전체 종목, 1 : KOSDAQ 전체 종목, 2 : KOSPI 특정, 3 : KOSDAQ 특정 )
        self.type = type
        self.code = code
        self.name = name
