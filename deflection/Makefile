PYTHON=$(wildcard *.py)
PYOUT = $(patsubst %.py, %.out, $(PYTHON))

all: $(PYOUT) 

%.out: %.py Makefile
	python $<

clean:
	rm -f $(PYOUT)
