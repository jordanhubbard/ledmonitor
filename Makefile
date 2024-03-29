INSTALL_PATH=/usr/local/libexec/ledmonitor

build:
	@echo No build step for this module - use install target to install

install:
	@echo "Target $@ running as root"
	sudo install -d ${INSTALL_PATH}
	sudo install -m 755 ledmonitor.py ${INSTALL_PATH}
	sudo install -m 755 ledcontrol.py ${INSTALL_PATH}
	sudo install -m 755 -c ledmonitor.service /etc/systemd/system

test-led:
	python3 test_tristate_led.py

test-server:
	@echo "Target $@ running as root"
	sudo python3 ledmonitor.py

test:
	@echo "use either the test-led or test-server targets to test each function"

run-server: install reload
	@echo "Target $@ running as root"
	sudo systemctl enable ledmonitor
	sudo systemctl start ledmonitor

stop-server: reload
	@echo "Target $@ running as root"
	sudo systemctl stop ledmonitor

flake:
	@flake8

reload:
	sudo systemctl daemon-reload

clean:
	rm -rf .idea build dist ledmonitor.spec __pycache__
