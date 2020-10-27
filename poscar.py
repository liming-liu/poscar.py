#!/usr/env/python
'''
To decompse POSCAR to:
1. latt (containing lattice constance)
2. element (coordinates of each element)
'''

import numpy as np
import matplotlib.pyplot as plt


poscar = open('POSCAR', 'r')
head = []
for i in range(9):
  head.append(poscar.readline())
scale_para = float(head[1])
latt = np.zeros([3,3])
for i in range(3):
  latt[i] = np.array(head[i+2].split(), dtype=float)
ele = head[5].split()
ele_num = np.array(head[6].split(), dtype=float)
N = ele_num.sum()

coor = np.zeros([int(N), 3])
for i in range(int(N)):
  coor[i] = np.array(poscar.readline().split()[0:3], dtype=float)
np.savetxt('coor', coor)

sum = 0
for i in range(len(ele)):
  ele_coor = np.zeros([int(ele_num[i]), 3])
  ele_coor = coor[sum: sum+int(ele_num[i]), :]
  sum = sum + int(ele_num[i])
  np.savetxt('%s' % ele[i], np.dot(ele_coor, latt.T), fmt="%10.5f")
