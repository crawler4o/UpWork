test_json = {"records": "563",
             "campaign": [{"id":"2027698","title":"OMFM Client Jet Charter 3 - Smart Inbox intro (average) GLOCKTEST alignable","status":"Completed","scheduledate":"December 13, 2018, 11:23:00 am","starttime":"December 13, 2018, 11:24:24 am","endtime":"December 13, 2018, 11:26:12 am","lastupdate":{},"sent":"41","views":"4","clicks":"3","optouts":"0","conversions":"0"},
                         {"id":"2027689","title":"OMFM Client Jet Charter 3 - Smart Inbox intro (average) GLOCKTEST no links","status":"Completed","scheduledate":"December 13, 2018, 10:29:00 am","starttime":"December 13, 2018, 10:30:24 am","endtime":"December 13, 2018, 10:32:10 am","lastupdate":{},"sent":"41","views":"1","clicks":"0","optouts":"0","conversions":"0"}]
             }


def data_multiplication(initial_nested_data):
    out = [{}]

    def data_multiplication_(nested_data):
        if isinstance(nested_data, list) and len(nested_data) > 0:
            base_dic = out[-1]
            print('match')
            print(base_dic)
            for x in nested_data:
                data_multiplication_(x)
                print(base_dic)
                out.append(base_dic)

        elif isinstance(nested_data, dict) or len(nested_data) == 0:
            for x in nested_data:
                if (isinstance(nested_data[x], list) or isinstance(nested_data[x], dict)) and len(nested_data[x]) > 0:
                    data_multiplication_(nested_data[x])
                else:
                    out[-1][x] = nested_data[x]

    data_multiplication_(initial_nested_data)

    return out


if __name__ == '__main__':
    data_multiplication(test_json)
