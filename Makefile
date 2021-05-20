build:
	@echo No build step for this module - use install target to install

install:
	sudo install -m 755 -c ledmonitor.py /usr/local/libexec
	sudo install -m 755 -c ledmonitor.service /etc/systemd/system

test:
	test_tristate_led.py

run: install
	systemctl start ledonitor

clean:
	rm -rf .idea build dist ledmonitor.spec
