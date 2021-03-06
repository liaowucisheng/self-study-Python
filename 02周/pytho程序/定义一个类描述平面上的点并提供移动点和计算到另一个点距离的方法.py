#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: 了无此生
# DateTime: 2020/5/26 22:03
# File: 定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法

class Coordinate(object):
    def __init__(self, x=0, y=0):
        """
        初始化方法
        :param x: 横坐标值
        :param y: 纵坐标值
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """
        移动到指定位置
        :param x: 新的横坐标
        :param y: 新的纵坐标
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """
        移动指定的增量
        :param dx:
        :param dy:
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """
        计算与另一个点的距离
        :param other: 另一个点
        """
        dx = other.x - self.x
        dy = other.y - self.y
        return (dx ** 2 + dy ** 2) ** 0.5

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))


def main():
    p1 = Coordinate(1, 1)
    p2 = Coordinate()
    print(p1)
    print(p2)
    p1.move_to(3, 3)
    p2.move_by(-3, 3)
    print(p1.__str__())
    print(p2.__str__())
    print(p1.distance_to(p2))


if __name__ == '__main__':
    main()
