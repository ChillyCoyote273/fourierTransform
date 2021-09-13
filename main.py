from graphics import *

from drawRotations import *


def main():
	window = GraphWin("Main Window", 800, 600, autoflush=False)
	coefficients = generate_random_coefficients(10)
	rotations(window, coefficients)


if __name__ == '__main__':
	main()
