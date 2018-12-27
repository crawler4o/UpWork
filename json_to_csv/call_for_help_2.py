"""
The expected output is:

[{'records': '563'},
{'records': '563', 'id': '1111111', 'title': 'alignable', 'status': 'Completed'},
{'records': '563', 'id': '2222222', 'title': ' no links', 'status': 'something'}]


"""


test_json = {"records": "563",
             "campaign": [{"id": "1111111", "title": "alignable", "status": "Completed"},
                         {"id": "2222222", "title": " no links", "status": "something"}]
             }


def data_multiplication(initial_nested_data):
    out = [{}]

    def data_multiplication_(nested_data):
        if isinstance(nested_data, list) and len(nested_data) > 0:
            base_dic = out[-1]
            for x in nested_data:
                print(f'The base_dictionary before the desired append is: {base_dic}')
                out.append({1: 'This here should be the basic dictionary'})  # Works like a breeze.
                #  out.append(base_dic)  # Comment the previous line, uncomment this one and the party will start.
                print(f'The base_dictionary after the desired append is: {base_dic}')
                data_multiplication_(x)

        elif isinstance(nested_data, dict) or len(nested_data) == 0:
            for x in nested_data:
                if (isinstance(nested_data[x], list) or isinstance(nested_data[x], dict)) and len(nested_data[x]) > 0:
                    data_multiplication_(nested_data[x])
                else:
                    out[-1][x] = nested_data[x]

    data_multiplication_(initial_nested_data)

    return out


if __name__ == '__main__':
    result = data_multiplication(test_json)
    print(result)

