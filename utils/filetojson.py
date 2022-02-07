import abc
import json


class FileConversion(abc.ABC):
    @abc.abstractmethod
    def convert_file(self, file: str) -> str:
        """ get the file to be converted """


class Convertor( FileConversion ):
    
    def convert_file(self, file: FileConversion) -> None:
        """ convert the file to json 
        
        ARGS:
            file: FileConversion: the file to be converted
        """
        
        if file != 'json':
            with open(file, 'r') as f:
                data = f.read()
                data = data.split('\n')
                data = [line.split(',') for line in data]
                return json.dumps(data)


def main() -> None:
    file_path = input('Enter the path of file: ')
    converter = Convertor
    converted_file = converter.convert_file(file_path)
    print('success')
    return converted_file


if __name__ == '__main__':
    main()