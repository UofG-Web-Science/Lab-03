import util

if __name__ == '__main__':
    data_dir_path = "data/data1"
    jsons = util.load_jsons(data_dir_path)
    texts = []
    for json_data in jsons:
        location = util.extract_location(json_data)
        geo_enabled = util.extract_enabled(json_data)
        coordinate = util.extract_coordinate(json_data)
        place = util.extract_place(json_data)
        print(location, geo_enabled, coordinate, place)
