class Stock:

    def __init__(self, type, code, name):

        # TYPE => ( 0 : KOSPI 특정, 1 : KOSDAQ 특정, 2 : KOSPI 전체, 3 : KOSDAQ 전체 )
        self.type = type
        
        self.code = code
        self.name = name
