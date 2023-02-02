import json
import math
import os

from haversine import haversine


def compute_distance(box):
    R = 6373.0
    lat_1 = box[1]
    lon_1 = box[0]
    lat_2 = box[3]
    lon_2 = box[2]

    phi1 = lat_1 * (math.pi / 180)
    phi2 = lat_2 * (math.pi / 180)

    detal1 = (lat_2 - lat_1) * (math.pi / 180)
    detal2 = (lon_2 - lon_1) * (math.pi / 180)

    a = math.sin(detal1 / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(detal2 / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c
    return d


def load_jsons(dir_path):
    jsons = []
    for file in os.listdir(dir_path):
        if file.endswith(".json"):
            jsons.append(json.load(open(os.path.join(dir_path, file), encoding='UTF-8')))
    return jsons


def get_geo_enabled(json_data):
    geo_enabled = json_data["user"]["geo_enabled"]
    return geo_enabled


def get_loaction(json_data):
    loaction = json_data["user"]["location"]
    return loaction


def get_place(json_data):
    place = json_data["place"]
    return place


def get_coordinates(json_data):
    coordinates = json_data["coordinates"]
    return coordinates


def get_distance(city1, city2):
    dis = haversine(city1, city2)
    return dis
