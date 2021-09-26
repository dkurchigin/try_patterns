"""EXAMPLE FOR ADAPTER IN PYTHON"""
import json
import bson
from typing import Dict, Union


class BsonPrinter:
    """Class for new fuctionality for our service"""
    def __init__(self, input_data: str):
        self.input_data = input_data
        self.converted_str: Union[bytes, ImportError] = self.convert_from_bson()

    def convert_from_bson(self) -> Union[bytes, ImportError]:
        """CONVERT STR FROM BSON"""
        try:
            return bson.loads(self.input_data)
        except Exception as excepted_err:
            return ImportError(f'CAN\'T PRINT BSON, BECAUSE {excepted_err}')

    def __repr__(self):
        return repr(self.converted_str)


class JsonPrinter:
    """Class for old fuctionality for our service"""
    def __init__(self, input_data: str):
        self.input_data = input_data
        self.converted_str: Union[bytes, ImportError] = self.convert_from_json()

    def convert_from_json(self) -> bytes:
        """CONVERT STR FROM JSON"""
        return json.loads(self.input_data)

    def __repr__(self):
        return repr(self.converted_str)


class BsonClassAdapter(JsonPrinter, BsonPrinter):
    """Class adapter. Inheritance from 2 classes"""
    def __init__(self, input_data: str):
        super().__init__(input_data)
        self.prepared_bson = self.prepare_bson()

    def prepare_bson(self) -> bytes:
        """CONVERT STR FROM BSON"""
        return bson.dumps(self.convert_from_json())

    def __repr__(self):
        return repr(self.prepared_bson)


class BsonObjectAdapter(JsonPrinter):
    """Class adapter. Inheritance from old functionality"""
    def __init__(self, bson_printer: BsonPrinter):
        super().__init__(bson_printer.input_data)

    def convert_from_json(self) -> bytes:
        return bson.dumps(super().convert_from_json())


if __name__ == '__main__':
    dict_: Dict[str, str] = {'username': 'usr88', 'password': 'qwerty123'}
    json_obj = json.dumps(dict_)
    print('1. source json object:', json_obj)
    print('2. old functionality JsonPrinter print this:', JsonPrinter(json_obj))
    print('3. new fuctionality BsonPrinter can\'t work with json: ', BsonPrinter(json_obj))
    print('4. via class adapter BsonAdapter:', BsonClassAdapter(json_obj))
    print('5. via object adapter BsonObjectAdapter:', BsonObjectAdapter(BsonPrinter(json_obj)))
