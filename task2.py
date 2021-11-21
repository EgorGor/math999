import matplotlib.pyplot as plt
import random

def z1(n):
	global x
	global formula
	m = 2
	x = n**m
	formula = f'${n}^{m} = x$'
	
def z2(n):
	global x
	global formula
	m = 3
	x = n**m
	formula = f'${n}^{m} = x$'
	
def z3(n):
	global x
	global formula
	b = random.randint(2, 4)
	# a = random.randint(1, 5)
	c = random.randint(2, 4)
	x = b**c-n
	formula = f'$\log_{b}(x+{n}) = {c}$'

zz = [z1, z2, z3]

def plot(n):
	global fig
	random.choice(zz)(n)
	xsize = 5
	ysize = 1.5
	plt.figure(figsize=(xsize, ysize))
	# plt.text(xsize / 20, ysize/20, formula, fontsize=25)
	plt.text(0.0, 0, formula, fontsize=35)
	# Прячем оси
	plt.axis('off')
	# fig = plt.gca()
	# fig.axes.get_xaxis().set_visible(False)
	# fig.axes.get_yaxis().set_visible(False)

	plt.savefig('filename.png')
	plt.close()