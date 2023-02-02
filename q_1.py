import util

if __name__ == '__main__':
    data_dir_path = "data/data1"
    jsons = util.load_jsons(data_dir_path)
    texts = []
    for json_data in jsons:
        text = util.get_loaction(json_data)
        print(text)
