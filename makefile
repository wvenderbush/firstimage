#Winston Venderbush

PYTHON = python

all: dtest.py
	$(PYTHON) dtest.py

run: all
	./prog
