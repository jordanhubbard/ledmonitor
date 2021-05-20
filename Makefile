build:
	@echo No build step for this module - use install target to install

install:
	pyinstaller --onefile ledmonitor.py
	sudo install -m 755 -c dist/ledmonitor /usr/local/libexec
	sudo install -m 755 -c ledmonitor.service /etc/systemd/system

test:
	test_tristate_led.py

run: install
	systemctl start ledonitor

clean:
	rm -rf build dist ledmonitor.spec
