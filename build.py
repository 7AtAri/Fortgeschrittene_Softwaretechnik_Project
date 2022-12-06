from pybuilder.core import use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.distutils")
## use_plugin("python.install_dependencies")

name = "Appointment Bot"
default_task = "publish"

@init
def set_properties(project):
  project.set_property("coverage_break_build", FALSE)
  # project.depends_on("unittest") etc. 

