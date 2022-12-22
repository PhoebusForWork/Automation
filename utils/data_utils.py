import os
import json
import json5
import copy


class JsonReader:

    def __init__(self):

        self.file_path = os.path.join(os.path.dirname(
            os.path.dirname(__file__)), 'resources')
        self.cs_file_path = os.path.join(os.path.dirname(
            os.path.dirname(__file__)), 'resources/client_side')
        self.case = None

    def read_json(self, json_file):
        test_data = []
        key_data = []
        data_path = os.path.join(self.file_path, json_file)

        with open(data_path, mode='r', encoding='utf8') as f:
            json_data = json.load(f)
            for l in json_data:
                value1 = []
                key1 = []
                for k1, v1 in l.items():
                    if k1 != "test_item":
                        value1.append(v1)
                        key1.append(k1)
                    else:
                        for l1 in v1:
                            value2 = []
                            key2 = []
                            for k2, v2 in l1.items():
                                value2.append(v2)
                                key2.append(k2)
                            test_data.append(tuple(value1+value2))
                            # key_data = key1+key2

        return test_data

    def read_json5(self, json_file, file_side='plt'):
        test_data = []
        key_data = []
        if file_side == 'cs':
            data_path = os.path.join(self.cs_file_path, json_file)
        else:
            data_path = os.path.join(self.file_path, json_file)

        with open(data_path, mode='r', encoding='utf8') as f:
            json_data = json5.load(f)
            for l in json_data:
                value1 = []
                key1 = []
                for k1, v1 in l.items():
                    if k1 != "test_item":
                        value1.append(v1)
                        key1.append(k1)
                    else:
                        for l1 in v1:
                            value2 = []
                            key2 = []
                            for k2, v2 in l1.items():
                                value2.append(v2)
                                key2.append(k2)
                            test_data.append(tuple(value1+value2))
                            key_data.append(tuple(key1+key2))  # 之後可能會用到
            test_case = []
            for i in range(len(key_data)):
                test_case.append(dict(zip(key_data[i], test_data[i])))
            self.case = test_case
        return test_case

    def get_case(self, target):
        if self.case is not None:
            testdata = []
            for i in self.case:
                if target == i["test_case"]:
                    testdata.append(i)
            return testdata
        else:
            raise ValueError("尚未載入Json檔案")

    @staticmethod
    def get_test_case(data, target):
        testdata = []
        for i in data:
            if target == i["test_case"]:
                testdata.append(i)
        return testdata

    @staticmethod
    def replace_json(json, target):
        json_copy = copy.deepcopy(json)  # 避免淺層複製導致case讀取有誤
        for key in list(target.keys()):

            value = target.get(key, "不存在")
            try:
                json_copy[key] = value
            except:
                json_copy[0][key] = value
        return json_copy


if __name__ == '__main__':
    ut = JsonReader()
    r = ut.read_json5('test_proxy.json5')

    td = ut.get_test_case(r, 'proxy_test')
    print(td)
