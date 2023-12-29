def dict_id(dict_entire, item):
    try:
        if item['id'] != '':
            dict_entire['id'].append(item['id'])
        else:
            dict_entire['id'].append(None)
    except KeyError:
        dict_entire['id'].append(None)

def dict_authors(dict_entire, item):
    auth = []
    try:
        if item['authors'] != '':
            for i in item['authors']:
                auth.append(i['name'])
            dict_entire['authors'].append(auth)
        else:
            dict_entire['authors'].append(None)
    except KeyError:
        dict_entire['authors'].append(None)

def dict_title(dict_entire, item):
    try:
        if item['title'] != '':
            dict_entire['title'].append(item['title'])
        else:
            dict_entire['title'].append(None)
    except KeyError:
        dict_entire['title'].append(None)

def dict_year(dict_entire, item):
    try:
        if item['year'] != '':
            dict_entire['year'].append(item['year'])
        else:
            dict_entire['year'].append(None)
    except KeyError:
        dict_entire['year'].append(None)

def dict_n_citation(dict_entire, item):
    try:
        if item['n_citation'] != '':
            dict_entire['n_citation'].append(item['n_citation'])
        else:
            dict_entire['n_citation'].append(None)
    except KeyError:
        dict_entire['n_citation'].append(None)

def dict_doc_type(dict_entire, item):
    try:
        if item['doc_type'] != '':
            dict_entire['doc_type'].append(item['doc_type'])
        else:
            dict_entire['doc_type'].append(None)
    except KeyError:
        dict_entire['doc_type'].append(None)

def dict_publisher(dict_entire, item):
    try:
        if item['publisher'] != '':
            dict_entire['publisher'].append(item['publisher'])
        else:
            dict_entire['publisher'].append(None)
    except KeyError:
        dict_entire['publisher'].append(None)

def dict_references(dict_entire, item):
    try:
        if item['references'] != '':
            dict_entire['references'].append(item['references'])
        else:
            dict_entire['references'].append(None)
    except KeyError:
        dict_entire['references'].append(None)