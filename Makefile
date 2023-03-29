hello:
	echo "This is Ahmed"
install:
	pip install --upgrade pip &&\
    	pip install -r requirements.txt

test:
	python -m pytest -vv test_adder.py
