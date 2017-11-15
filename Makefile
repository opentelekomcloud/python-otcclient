test:
	./otcclient/tests/do_tests.sh

build:
	./build.sh

clean:
	find -name '*.bak' | xargs rm
	find -name '*~' | xargs rm
