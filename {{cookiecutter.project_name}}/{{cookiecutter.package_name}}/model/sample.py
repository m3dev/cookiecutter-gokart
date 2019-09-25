from logging import getLogger

import gokart

logger = getLogger(__name__)


class Sample(gokart.TaskOnKart):
    task_namespace = '{{cookiecutter.package_name}}'

    def output(self):
        return self.make_target('data/sample.pkl')

    def run(self):
        self.dump('sample output')
