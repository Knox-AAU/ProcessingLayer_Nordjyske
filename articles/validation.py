from console import print_warning

def is_valid(data):
    if (check_paragraphs(data) and
        check_for_attribute(data, 'headline') and
        check_byline(data) and
        check_for_attribute(data, 'publication') and
        check_for_attribute(data, 'published_at') and
        check_publisher(data) and
        check_len_for_all(data)):
        return True
    else:
        return False

def check_paragraphs(data):
    if 'paragraphs' not in data:
        return False
    elif len(data['paragraphs']) < 2:
        return False
    for par in data['paragraphs']:
        if 'kind' in par and par['kind'] == 'paragraph' and is_valid_str(par['value']):
            return True
    return False

def check_for_attribute(data, attribute):
    if attribute not in data or not is_valid_str(data[attribute]):
        return False
    return True

def check_byline(data):
    if 'byline' not in data:
        return False
    elif 'name' not in data['byline']:
        return False
    elif not is_valid_str(data['byline']['name']):
        return False
    return True

def check_publisher(data):
    if 'publisher' not in data or data['publisher'] != 'Nordjyske Medier':
        data = 'Headline: "' + data['headline'] + '", Published date: ' + data['published_at']
        print_warning('Article is skipped. Not from Nordjyske Medier. ' + data)
        return False
    return True

def is_valid_str(var):
    return (isinstance(var, str) and len(var) > 0)

def check_len_for_all(data):
    max_len = 100
    data_list = []
    data_list.append(data['headline'])
    data_list.append(data['byline']['name'])
    data_list.append(data['published_at'])
    for d in data_list:
        if len(d) > max_len:
            return False
    return True
