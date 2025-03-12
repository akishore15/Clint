CC = python
CFLAGS = 
LDFLAGS = 

GUI_CODE = gui.py
TEST_CODE = test.py
VENV = venv
REQUIREMENTS = requirements.txt

all: $(GUI_CODE)

$(GUI_CODE):
    $(CC) $(CFLAGS) $(GUI_CODE)

run: $(GUI_CODE)
    $(CC) $(GUI_CODE)

test: $(TEST_CODE)
    $(CC) $(TEST_CODE)

venv:
    python -m venv $(VENV)

install: venv
    source $(VENV)/bin/activate; pip install -r $(REQUIREMENTS)

clean:
    rm -f *.pyc
    rm -rf $(VENV)

uninstall:
    rm -rf $(VENV)