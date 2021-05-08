from logging import getLogger

from {{cookiecutter.package_name}}.utils.template import GokartTask

logger = getLogger(__name__)


class Sample(GokartTask):
    def run(self):
        self.dump('sample output')
