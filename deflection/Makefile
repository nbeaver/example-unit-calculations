PYTHON=$(wildcard *.py)
OUT = $(patsubst %.py, %.out, $(PYTHON))

all: $(OUT)

%.out: %.py Makefile
	python $<

clean:
	rm -f $(OUT)
