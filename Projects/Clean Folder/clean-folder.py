import os

dir = 'C:\\Users\\Rob\\Downloads\\'


class delFiles:
    def __init__(self, path):
        files = os.listdir(path)
        for file in files:
            if file.endswith(".zip"):
                os.remove(os.path.join(path, file))
                print(f"{file} deleted.")

delFiles(dir)
