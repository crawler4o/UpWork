# https://medium.com/@gis10kwo/converting-nested-json-data-to-csv-using-python-pandas-dc6eddc69175

import json
import pandas as pd


def parse():
    with open('./input.txt', 'r', encoding='utf-8') as f:
        in_json = json.load(f)
        print(in_json)
        in_json = data_multiplication(in_json)
        parsed_json_df = pd.io.json.json_normalize(in_json)
        print(parsed_json_df)

    return parsed_json_df


def write(flat_df):
    flat_df.to_csv('output.csv', sep=',', encoding='utf-8')


def data_multiplication(initial_nested_data):
    out = [{}]

    def data_multiplication_(nested_data):
        if type(nested_data) == list:
            n = 0
            base_dic = out[len(out) - 1]
            for _ in nested_data:
                data_multiplication_(nested_data[n])
                out.append(base_dic)
                n += 1

        elif type(nested_data) == dict:

            for x in nested_data:
                if type(nested_data[x]) == list or type(nested_data[x]) == dict:
                    # base_dic = out[len(out) - 1]
                    # out.append(base_dic)
                    data_multiplication_(nested_data[x])

                else:
                    out[len(out)-1][x] = nested_data[x]

        # else:
        #    out[0].append(nested_data)

    data_multiplication_(initial_nested_data)

    return out


if __name__ == '__main__':
    write(parse())
