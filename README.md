# cookiecutter-gokart

This is a [cookiecutter](https://github.com/audreyr/cookiecutter) template for generating a [gokart](https://github.com/m3dev/gokart) tasks.


# Usage

```
cookiecutter https://github.com/m3dev/cookiecutter-gokart
```

- question

Set up using interactive style. Press enter to use default value.

```
project_name [project_name]: m3sample                        # project name, repo name
package_name [package_name]: sample                          # python package name
python_version [3.6]:                                        # using python version
author [your name]: m3dev                                    # repository author name
package_description [What's this project?]: this is sample   # short description
license [MIT License]:                                       # license
```

- run sample

```
python main.py sample.Sample --local-scheduler
```


# Thanks

- cookiecutter: https://github.com/audreyr/cookiecutter
- gokart: https://github.com/m3dev/gokart
