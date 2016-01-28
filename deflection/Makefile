PYTHON=$(wildcard *.py)
PYOUT = $(patsubst %.py, %.out, $(PYTHON))

all : $(PYOUT) gnu-units.out readme.html

gnu-units.out : gnu-units.sh
	sh gnu-units.sh > gnu-units.out

%.out : %.py Makefile
	python $<

readme.html : readme.rst
	rst2html readme.rst readme.html

clean:
	rm -f $(PYOUT) gnu-units.out
	rm -f readme.html
