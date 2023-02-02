import json
import math
import os

from haversine import haversine


def load_jsons(dir_path):
    jsons = []
    for file in os.listdir(dir_path):
        if file.endswith(".json"):
            jsons.append(json.load(open(os.path.join(dir_path, file), encoding='UTF-8')))

    return jsons


def extract_enabled(json_data):
    geo_enabled = json_data["user"]["geo_enabled"]

    return geo_enabled


def extract_location(json_data):
    location = json_data["user"]["location"]

    return location


def extract_place(json_data):
    place = json_data["place"]

    return place


def extract_coordinate(json_data):
    coordinate = json_data["coordinates"]

    return coordinate


def calc_distance_bbox(bbox):
    R = 6373.0
    lon_1, lat_1, lon_2, lat_2 = bbox

    phi_1 = lat_1 * (math.pi / 180)
    phi_2 = lat_2 * (math.pi / 180)

    delta_1 = (lat_2 - lat_1) * (math.pi / 180)
    delta_2 = (lon_2 - lon_1) * (math.pi / 180)

    a = math.sin(delta_1 / 2) ** 2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_2 / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    dis = R * c

    return dis


def calc_distance_point(city1, city2):
    dis = haversine(city1, city2)

    return dis
