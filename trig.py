import matplotlib.pyplot as plt
import random
import numpy as np


	
def z1(n):
	global x
	global formula
	m = random.randint(1, 3)
	k = np.sin(n*np.pi/m)**2
	x = float('{:.3f}'.format(k))
	formula = r'$sin^2(\frac{*n\pi}{m})$'.replace("m", f"{m}").replace("*n", f"{n}")
	# formula = r'${{f"{m}"}}$'
	
def z2(n):
	global x
	global formula
	m = random.randint(1, 3)
	k = np.cos(n*np.pi/m)**2
	x = float('{:.3f}'.format(k))
	formula = r'$cos^2(\frac{*n\pi}{m})$'.replace("m", f"{m}").replace("*n", f"{n}")
	# formula = r'${{f"{m}"}}$'

zz = [z1, z2]

def plot(n):
	global fig
	random.choice(zz)(n)
	xsize = 5
	ysize = 1.5
	plt.figure(figsize=(xsize, ysize))
	# plt.text(xsize / 20, ysize/20, formula, fontsize=25)
	plt.text(0.0, 0.3, formula, fontsize=35)
	# Прячем оси
	plt.axis('off')
	# fig = plt.gca()
	# fig.axes.get_xaxis().set_visible(False)
	# fig.axes.get_yaxis().set_visible(False)

	plt.savefig('filename.png')
	plt.close()