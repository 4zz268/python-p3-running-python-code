import io
import sys
import runpy
from os import path

class TestAppPy:
    def test_app_py_exists(self):
        '''
        exists in lib directory
        '''
        assert(path.exists("lib/app.py"))

    def test_app_py_is_executable(self):
        '''
        is executable
        '''
        assert(path.isfile("lib/app.py"))

    def test_prints_hello_world(self):
        '''
        prints "Hello World! Pass this test, please."
        '''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        runpy.run_path("lib/app.py")
        sys.stdout = sys.__stdout__  # Make sure this line is indented with 8 spaces total
        output = captured_out.getvalue().strip()
        assert output == "Hello World! Pass this test, please."
