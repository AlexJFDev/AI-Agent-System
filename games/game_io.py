import time
import sys

class GameIO:
    """
    This class allows you to hook simple text based games up to an environment. The games should be set to print and get input from GameIO objects.
    """
    def __init__(self, filepath):
        self.filepath = filepath
        with open(self.filepath, "w"): pass # We want to clear out the file

    def write(self, s):
        with open(self.filepath, 'a') as file:
            file.write(s)
        return len(s)
    
    def flush(self):
        return
    
    def read(self):
        while True:
            with open(self.filepath, 'r+') as file:
                file.seek(0)
                contents = file.read()
                if contents:
                    file.seek(0)
                    file.truncate()
                    return contents
            time.sleep(0.1)

    def readline(self):
        return self.read()