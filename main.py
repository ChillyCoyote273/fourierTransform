import cmath
import random as r

from graphics import *


def make_point(x, y):
	return Point(int(x) + 400, 300 - int(y))


def clear(win):
	for item in win.items[:]:
		item.undraw()
		

def draw_line(window, start, coefficient, step):
	end = start + coefficient * cmath.exp(complex(0, cmath.pi * 2 * step))
	start_point = make_point(start.real, start.imag)
	end_point = make_point(end.real, end.imag)
	line = Line(start_point, end_point)
	line.setArrow("last")
	line.draw(window)
	return end, line


def get_rotation_speed(index):
	index += 1
	speed = index // 2
	speed *= 1 - (index % 2) * 2
	return speed


def draw_lines(window, coefficients, step):
	next_start = complex(0, 0)
	lines = []
	for i, coefficient in enumerate(coefficients):
		next_start, line = draw_line(window, next_start, coefficient, step * get_rotation_speed(i))
		lines.append(line)
	return next_start, lines


def draw_shape(window, points):
	for i in range(len(points) - 1):
		line = Line(points[i], points[i + 1])
		line.draw(window)
	line = Line(points[0], points[-1])
	line.draw(window)


def rotations(window, coefficients):
	step = 0
	points = []
	while step < 1:
		point, _ = draw_lines(window, coefficients, step)
		point = make_point(point.real, point.imag)
		points.append(point)
		step += 0.002
	step = 0
	clear(window)
	draw_shape(window, points)
	lines = []
	while window.isOpen():
		if step >= 1:
			step = 0
		else:
			step += 0.002
		for line in lines:
			line.undraw()
		_, lines = draw_lines(window, coefficients, step)
		update(50)
		
		
def generate_random_coefficients(amount):
	size = 100
	coefficients = [
		complex(0, 0)
	]
	for i in range(amount):
		real = (r.random() + 0.5) * size
		imag = (r.random() + 0.5) * size
		coefficients.append(complex(real, imag))
		real = (r.random() + 0.5) * size
		imag = (r.random() + 0.5) * size
		coefficients.append(complex(real, imag))
		size /= 2
	return coefficients


def main():
	window = GraphWin("Main Window", 800, 600, autoflush=False)
	coefficients = generate_random_coefficients(2)
	rotations(window, coefficients)


if __name__ == '__main__':
	main()
