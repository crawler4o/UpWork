import json
import pandas as pd


def parse():
    with open('./input.txt', 'r', encoding='utf-8') as f:
        in_json = json.load(f)
        # print(in_json)
        in_json = data_multiplication(in_json)
        parsed_json_df = pd.io.json.json_normalize(in_json)
        # print(parsed_json_df)

    return parsed_json_df


def write(flat_df):
    flat_df.to_csv('output.csv', sep=',', encoding='utf-8')


def data_multiplication(initial_nested_data):
    out = [{}]

    def data_multiplication_(nested_data):
        if type(nested_data) == list and len(nested_data) > 0:
            n = 0
            base_dic = out[len(out) - 1]
            print('match')
            print(out)
            for _ in nested_data:
                data_multiplication_(nested_data[n])
                #breakpoint()
                out.append({})  # base_dic)
                #breakpoint()
                print(base_dic)
                n += 1

        elif type(nested_data) == dict or len(nested_data) == 0:

            for x in nested_data:
                if (type(nested_data[x]) == list or type(nested_data[x]) == dict) and len(nested_data[x]) > 0:
                    data_multiplication_(nested_data[x])

                else:
                    out[len(out) - 1][x] = nested_data[x]

    data_multiplication_(initial_nested_data)

    return out


if __name__ == '__main__':
    write(parse())
