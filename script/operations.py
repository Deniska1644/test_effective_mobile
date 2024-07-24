import json
from json import JSONDecodeError
from typing import Dict, List


from config import FILE_PATH
from models import ModelBoock

 
    

class BoockWorker: 
    file_path = FILE_PATH


    def add_boock(self, model:ModelBoock) -> dict|None:
        all_data = self.get_all_data()
        added_data = self.chek_added_book(model)
        if isinstance(added_data, dict):
            with open(self.file_path,'w', encoding='utf-8') as f:
                all_data.append(added_data)
                json.dump(all_data,f)
                return model()


    def del_boock(self, id:int) -> dict|None:
        all_data = self.get_all_data()
        delete_result:dict = {}
        for i in range(0,len(all_data)):
            if all_data[i]["id"] == id:
                delete_result = all_data[i]
                del all_data[i]
                with open(self.file_path,'w', encoding='utf-8') as f:
                    json.dump(all_data,f,ensure_ascii=False)
                return delete_result


    def find_boock(self, **kwargs) -> list[dict]:
        all_data = self.get_all_data()
        result_list = []
        filters = kwargs.keys()
        for book in all_data:
            for filter in filters:
                if book[filter] == kwargs[filter]:
                    result_list.append(book)
        return result_list


    def show_all_boocks(self)-> List[dict]:
        all_data = self.get_all_data()
        return all_data

    
    def change_status_boock(self,id:int, status:str) -> dict|None:
        all_data = self.get_all_data()
        all_data[id-1]["status"] = status
        with open(self.file_path,'w', encoding='utf-8') as f:
            json.dump(all_data,f,ensure_ascii=False)
            return all_data[id-1]


    def find_boock_by_id(self,id:int) -> dict|None:
        try:
            all_data = self.get_all_data()
            return all_data[id-1]
        except IndexError:
            return None


    @classmethod
    def chek_added_book(cls, model:ModelBoock) -> dict|int:
        data = cls.get_all_data()
        for book in data:
            if book['title'] == model.title and book['author'] == model.author:
                return book['id']
        return model()    
            

    @classmethod
    def get_all_data(cls) -> List[Dict[str,str]] | List:
        try:
            with open(cls.file_path,'r', encoding='utf-8') as f:
                return json.load(f)
        except JSONDecodeError:
            return []
        except FileNotFoundError:
            with open(cls.file_path,'w', encoding='utf-8') as f:
                return []
                 






    




    
