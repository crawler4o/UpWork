import json
import pandas as pd


def parse():
    with open('./input.txt', 'r', encoding='utf-8') as f:
        in_json = json.load(f)
        in_json = data_multiplication(in_json)
        parsed_json_df = pd.io.json.json_normalize(in_json)

    return parsed_json_df


def write(flat_df):
    flat_df.to_csv('output.csv', sep=',', encoding='utf-8', index=False)


def data_multiplication(initial_nested_data):
    out = [{}]

    def data_multiplication_(nested_data, parent_key=''):
        if isinstance(nested_data, list) and len(nested_data) > 0:
            base_dic = out[-1]
            out.pop()
            for i, v in enumerate(nested_data):
                if isinstance(v, (list, dict)):
                    out.append({**base_dic})
                    data_multiplication_(v, parent_key)
                else:
                    if i == 0:
                        out.append({**base_dic})
                    out[-1][f'{parent_key}_{i}'] = v

        elif isinstance(nested_data, dict) or len(nested_data) == 0:
            for key, value in nested_data.items():
                if isinstance(value, (list, dict)) and len(value) > 0:
                    if parent_key:
                        data_multiplication_(value, f'{parent_key}_{key}')
                    else:
                        data_multiplication_(value, key)
                else:
                    if parent_key:
                        out[-1][f'{parent_key}_{key}'] = value
                    else:
                        out[-1][key] = value

    data_multiplication_(initial_nested_data)

    return out


if __name__ == '__main__':
    write(parse())
