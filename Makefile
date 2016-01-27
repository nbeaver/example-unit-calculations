PYTHON=$(wildcard *.py)
LOG = $(patsubst %.py, %.log, $(PYTHON))

all: $(LOG)

%.log: %.py Makefile
	python $< > $@ 

clean:
	rm -f $(LOG)
