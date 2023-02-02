import util

if __name__ == '__main__':
    bouding_box = [-74.255653, 40.495682, -73.689484, 40.917622]
    distance = util.compute_distance(bouding_box)
    print(distance)
