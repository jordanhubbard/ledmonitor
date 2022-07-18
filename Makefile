INSTALL_PATH=/usr/local/libexec/ledmonitor

build:
	@echo No build step for this module - use install target to install

install:
	sudo install -d ${INSTALL_PATH}
	sudo install -m 755 ledmonitor.py ${INSTALL_PATH}
	sudo install -m 755 ledcontrol.py ${INSTALL_PATH}
	sudo install -m 755 -c ledmonitor.service /etc/systemd/system

test_led:
	python3 test_tristate_led.py

test_server:
	@echo "Target $@ running as root"
	sudo python3 ledmonitor.py

test:
	@echo "use either the test_led or test_server targets to test each function"

service-run: install
	@echo "Target $@ running as root"
	sudo systemctl daemon-reload
	sudo systemctl enable ledmonitor
	sudo systemctl start ledmonitor

service-stop:
	@echo "Target $@ running as root"
	sudo systemctl stop ledmonitor

clean:
	rm -rf .idea build dist ledmonitor.spec
