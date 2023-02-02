import util

if __name__ == '__main__':
    bbox = [-74.255653, 40.495682, -73.689484, 40.917622]
    dis = util.calc_distance(bbox)
    print(dis, "km")
