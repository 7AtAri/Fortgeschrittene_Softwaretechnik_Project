from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin('pypi:pybuilder_pycharm_workspace')
# use_plugin('python.pycharm')
# use_plugin("python.install_dependencies")

name = "Appointment Bot"
default_task = "publish"


@init
def initialise(project):
    project.set_property('pycharm_workspace_main_version', '2019')
    project.set_property('pycharm_workspace_project_path', project_path)


@init
def set_properties(project):
    project.set_property("coverage_break_build", False)
    # project.depends_on("unittest") etc.
