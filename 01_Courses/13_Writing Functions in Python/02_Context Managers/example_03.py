from psycopg2 import connect


def copy(src,dst):
    """ Copy the contents of one file to another.

    Args: 
        src (str): File name of the file to be copied.
        dst (str): Where to write the new file.
    """

    # Open the source file and read in the contexts
    with open(src) as f_src:
        contents = f_src.read()
    
    # Open the destination file and write out the contents
    with open(dst,'w') as f_dst:
        f_dst.write(contents)


def copy(src,dst):
    """ Copy the contents of one file to another.

    Args: 
        src (str): File name of the file to be copied.
        dst (str): Where to write the new file.
    """

    # Open both files
    with open(src) as f_src:
        with open(dst,'w') as f_dst:
        # Read and write each line, one at a time
            for line in f_src:
                f_dst.write(line)


def get_printer(ip):
    p = connect_to_printer(ip)

    try:
        yield

    # This MUST be called or no one else will
    # be able to connect to the printer
    finally:
        p.disconnect()
        print('disconnected from printer')

doc = {'text': 'This is my text.'}
with get_printer('10.0.34.111') as printer:
    printer.print_page(doc['txt'])

"""
try:
    # code that might raise an error
except:
    # do something about the error
finally:
    # this code runs no matter what
"""