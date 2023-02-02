import util

if __name__ == '__main__':
    point_New_York = (-74.023746, 40.674324)
    point_London = (0.137842, 51.450798)
    dis = util.calc_distance(point_New_York, point_London)
    print(dis, "km")
