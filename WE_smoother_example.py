#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example/test of Python Whittaker smoother

The test data files
    'nmr.dat'
    'wood.txt'
can be downloaded from
    http://dx.doi.org/10.1021/ac034173t
    (follow link 'Supporting Info')
and are also included in the repository of this implementation.

This script reproduces Figure 3 and Figure 10 (top) of Ref. [1]

[1] P. H. C. Eilers, "A perfect smoother",
    Anal. Chem. 2003, (75), 3631-3636
"""

import numpy as np
from whittaker_smooth import whittaker_smooth
import matplotlib.pyplot as plt

nmr = np.loadtxt('nmr.dat')
nmr_sm10 = whittaker_smooth(nmr, 10, d=3)
nmr_sm100 = whittaker_smooth(nmr, 100, d=3)
plt.figure(1)
plt.clf()
plt.plot(nmr)
plt.plot(nmr_sm10-20)
plt.plot(nmr_sm100-40)
plt.xlabel('Channel')
plt.ylabel('Signal strength')
plt.title('NMR spectrum smoothed with d = 3 and $\lambda$ = 10, 100')
plt.ylim(-60,60)
plt.xlim(0,1100)

wood = np.loadtxt('wood.txt')
wood_sm = whittaker_smooth(wood, 2E4, d=2)
plt.figure(2)
plt.clf()
plt.plot(wood)
plt.plot(wood_sm)
plt.ylim(60,130)
plt.xlim(0,350)
plt.title('Wood surface data and optimal smooth ($\lambda = 2 \\times 10^4$)')
plt.xlabel('Distance [mm]')
plt.ylabel('Height [µm]')

plt.show()
