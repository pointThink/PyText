def read(file):
    open_file = open(file, 'r')
    return open_file.read()


def write(file, data):
    open_file = open(file, 'w')
    open_file.write(data)
