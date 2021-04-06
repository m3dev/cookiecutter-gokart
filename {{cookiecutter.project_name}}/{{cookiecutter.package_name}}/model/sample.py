from logging import getLogger

from utils.templete import GokartTask

logger = getLogger(__name__)


class Sample(GokartTask):
    def run(self):
        self.dump('sample output')
