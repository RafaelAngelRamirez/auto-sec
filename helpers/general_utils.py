
import sys

class GeneralUtils:

    data:str = None

    def tool_name(self, name:str) -> GeneralUtils:
        self.print('*'*20)
        self.print(name.center(20, ''))
        self.print('*'*20)


    def print(self, c) -> GeneralUtils:
        """Print to standar output directly in the buffer. 
        Use this when call some action. 
        """
        sys.stdout.buffer.write(c)
        return self

    
    def open(self, process,  name="file.log", mode="wb") -> GeneralUtils:
        with open(name, mode) as file:
            for content in iter(lambda: process.stdout.read(1), b""):
                # This is for show the result in a more clear form 
                self.print(content)
                # We use this file to get the data. 
                file.write(content)
        
        data = None
        with open("test.log", "r") as file_log:
            data = file_log.read()
        
        self.data = data
        return self


    def run(self) -> GeneralUtils:
        raise "Not defined"

    




    

