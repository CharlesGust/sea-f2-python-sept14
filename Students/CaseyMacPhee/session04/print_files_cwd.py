if __name__ == '__main__':
	import pathlib
	path = pathlib.Path('./')
	path.absolute()
	for f in path.iterdir():
		print path.absolute() / f




