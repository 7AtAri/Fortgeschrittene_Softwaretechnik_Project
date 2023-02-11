from pathlib import Path

from pybuilder.core import use_plugin, init

use_plugin('python.core')
use_plugin('python.install_dependencies')
use_plugin('python.distutils')
# use_plugin("python.unittest") # added to the github workflow instead
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin('pypi:pybuilder_pycharm_workspace')

project_path = Path(__file__).resolve().parent

name = project_path.name
default_task = "publish"


@init
def set_properties(project):
    project.set_property('pycharm_workspace_project_path', project_path)
    project.set_property("coverage_break_build", False)
    project.build_depends_on_requirements("requirements.txt")


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == 'pycharm_builder':
        from subprocess import run

        pyb_command = ['pyb_'] + sys.argv[2:]
        run(pyb_command)  # Add more complexity here as desired
    else:
        print("Nothing to do here")
