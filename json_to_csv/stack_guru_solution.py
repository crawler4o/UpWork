"""
This code was suggested by cdlane - a stackoverflow guy who made my day.
"""

test_json = {
    "records": "563",
    "campaign": [
        {"id": "1111111", "title": "alignable", "status": "Completed"},
        {"id": "2222222", "title": " no links", "status": "something"}
    ]
}

def data_multiplication(initial_nested_data):
    out = [{}]

    def data_multiplication_recursive(nested_data):

        if isinstance(nested_data, dict):
            for key, value in nested_data.items():
                if isinstance(value, list):
                    data_multiplication_recursive(value)
                else:
                    out[0][key] = value

        elif isinstance(nested_data, list):
            base_dic = out[0]

            for dictionary in nested_data:
                out.append({**base_dic, **dictionary})

    data_multiplication_recursive(initial_nested_data)

    return out

if __name__ == '__main__':
    result = data_multiplication(test_json)
    print(result)