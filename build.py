from pathlib import Path

from pybuilder.core import use_plugin, init, Author


use_plugin('python.core')
use_plugin('python.install_dependencies')
use_plugin('python.distutils')

use_plugin('pypi:pybuilder_pycharm_workspace')

project_path = Path(__file__).resolve().parent

name = project_path.name
authors = [Author("foo", 'bar')]
license = "Apache License, Version 2.0"
version = '1.0.0'


@init
def initialise(project):
    project.set_property('pycharm_workspace_project_path', project_path)


# Most important part of the script below (previous one is just filling code)
if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == 'pycharm_builder':
        from subprocess import run

        pyb_command = ['pyb_'] + sys.argv[2:]
        run(pyb_command)  # Add more complexity here as desired
    else:
        print("Nothing to do here")
