all: todo.html readme.html

todo.html: todo.md Makefile
	markdown todo.md > todo.html

readme.html: readme.rst Makefile
	rst2html readme.rst readme.html

pip_install_user: Makefile
	pip install --user astropy
	#pip install --user buckingham # https://github.com/mdipierro/buckingham/issues/3
	pip install --user cf-units
	pip install --user magnitude
	#pip install --user misu # https://github.com/cjrh/misu/issues/7
	pip install --user natu
	pip install --user numericalunits
	pip install --user Pint
	#pip install --user PhysicalQuantities # https://github.com/juhasch/PhysicalQuantities/issues/69
	pip install --user quantities
	pip install --user scimath
	pip install --user simtk.unit
	pip install --user sympy
	pip install --user udunitspy
	pip install --user units
	pip install --user Unum
