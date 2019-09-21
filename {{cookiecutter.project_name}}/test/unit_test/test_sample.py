from logging import getLogger
import unittest
from unittest.mock import MagicMock
from {{cookiecutter.package_name}}.model.sample import Sample

logger = getLogger(__name__)


class TestSample(unittest.TestCase):
    def setup(self):
        self.output_data = None

    def test_run(self):
        task = Sample()
        task.dump = MagicMock(side_effect=self._dump)
        task.run()
        self.assertEqual(self.output_data, "sample output")

    def _dump(self, data):
        self.output_data = data
