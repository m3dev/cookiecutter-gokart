import luigi
import numpy as np
import gokart

import {{cookiecutter.package_name}}

if __name__ == '__main__':
    gokart.add_config('./conf/param.ini')
    gokart.run()
