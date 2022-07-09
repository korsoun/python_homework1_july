# Напишите программу, которая принимает на вход координаты точки (X и Y) и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

coord_x = float(input('Введите координату Х: '))
coord_y = float(input('Введите координату Y: '))

if coord_x<0 and coord_y<0:
    print('3-я четверть')
if coord_x<0 and coord_y>0:
    print('2-я четверть')
if coord_x>0 and coord_y<0:
    print('4-я четверть')
if coord_x>0 and coord_y>0:
    print('1-я четверть')
if coord_x==0 and coord_y!=0:
    print('Ось Y')
if coord_x!=0 and coord_y==0:
    print('Ось Х')
