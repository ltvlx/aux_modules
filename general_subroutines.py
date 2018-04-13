"""
Useful subroitines often used in my work.

"""

def idx(_list, _el):
    """
    If _el is in the _list, returns its index.  
    Otherwise returns -1
    """
    try:
        return _list.index(_el)
    except:
        return -1


def apnd(_list, _el):
    """
    Appends _el to the _list if it is not in this list.
    Returns _list
    """
    try:
        _list.index(_el)
    except:
        _list.append(_el)
    return _list


def get_fnames(path, extension=''):
    """
    Returns list of files with input extension from the input path.
    """
    import os
    files_all = os.listdir(path)
    page_names = []
    for x in files_all:
        if (x.find(extension) != -1):
            page_names.append(x)
    return page_names


def find_all(data_line, substr):
    """
    Finds all 'substr' in 'data_line'
    Returns a list of indexes
    """
    i_list = []
    a = 0
    b = 0
    while True:
        b = data_line[a:].find(substr)
        if(b == -1):
            break
        i_list.append(b+a)
        a = i_list[-1]+1
    return i_list
    
