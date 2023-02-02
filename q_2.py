import util

if __name__ == '__main__':
    Newyork = (-74.023746, 40.674324)
    London = (0.137842, 51.450798)
    distance = util.get_distance(Newyork, London)
    print(distance, "km")
