import json

from config import FILE_PATH



class ModelBoock: 
    def __init__(self,**kwargs) -> None:
        self.id:int = self.get_id()
        self.title = kwargs.get('title')
        self.author = kwargs.get('author') 
        self.year = kwargs.get('year')
        if kwargs.get('status'):
            self.status = kwargs.get('status')
        self.status = 'в наличии'


    def __call__(self):
        return self.__to_dict()
    
    
    def __to_dict(self) -> dict:
        result_dict ={
            'id':self.id,
            'title':self.title,
            'author':self.author,
            'year':self.year,
            'status':self.status
        }
        return result_dict
    
    @staticmethod
    def get_id():
        try:
            with open(FILE_PATH,'r', encoding='utf-8') as f:
                all_data = json.load(f)
                try_get_id = all_data[-1].get("id")
                if try_get_id:
                    return int(try_get_id)+1
                return 1

        except:
            return 1