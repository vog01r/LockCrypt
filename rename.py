import os

for path, subdirs, files in os.walk('./test'):
    for name in files:
        print(os.path.join(path, name))
        filepath = os.path.join(path, name)

        filepath2=filepath.replace('.zooky','')
        os.rename(filepath, filepath2)