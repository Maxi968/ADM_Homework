

def get_attr_number2(node, n_attr):
    n_attr += len(node.attrib)    
    for tag in node:
        n_attr+=get_attr_number(tag)
    return n_attr

def get_attr_number(node):
    return get_attr_number2(node, 0)
    

