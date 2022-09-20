import os,json,json5

class Utils :

    def __init__(self):

        self.file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'resources')

    def read_json(self,json_file): 
        test_data = []
        key_data = []
        data_path = os.path.join(self.file_path,json_file)

        with open(data_path,mode='r',encoding='utf8') as f :
            json_data = json.load(f)
            for l in json_data:
                value1 = []
                key1 = []
                for k1,v1 in l.items():
                    if k1 != "test_item":
                        value1.append(v1)
                        key1.append(k1)
                    else : 
                        for l1 in v1:
                            value2 = []
                            key2 = []
                            for k2,v2 in l1.items():
                                # print(v2)
                                value2.append(v2)
                                key2.append(k2)
                            test_data.append(tuple(value1+value2))
            key_data=key1+key2
            print(key_data)
            
        return test_data

    def read_json5(self,json_file): 
        test_data = []
        key_data = []
        data_path = os.path.join(self.file_path,json_file)

        with open(data_path,mode='r',encoding='utf8') as f :
            json_data = json5.load(f)
            for l in json_data:
                value1 = []
                key1 = []
                for k1,v1 in l.items():
                    if k1 != "test_item":
                        value1.append(v1)
                        key1.append(k1)
                    else : 
                        for l1 in v1:
                            value2 = []
                            key2 = []
                            for k2,v2 in l1.items():
                                value2.append(v2)
                                key2.append(k2)
                            test_data.append(tuple(value1+value2))
            # key_data=key1+key2    #之後可能會用到
            
        return test_data

    def get_test_case(self,data,target):
        testdata =[]
        for i in data :
            if target in i :
                # print(i)
                testdata.append(i)
        return testdata


if __name__ == '__main__':
    ut = Utils()
    r = ut.read_json5('test_proxy.json5')
    
    td = ut.get_test_case(r,'proxy_test')
    print(td)