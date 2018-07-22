# Mod Organizer omod Installer
### Description
A Python plugin for
[Mod Organizer 2](https://github.com/Modorganizer2/modorganizer) which installs
omod files generated by Oblivion Mod Manager.

### Requirements
#### Binaries
* [Python 2.7](https://www.python.org/downloads/)
    * [Anaconda](https://www.anaconda.com/download/) is strongly recommended
    instead.

#### Packages
* [backports.lzma](https://pypi.org/project/backports.lzma/)
* [kaitaistruct](https://kaitai.io/)
* [pathlib2](https://pypi.org/project/pathlib2/)
* `DEV` [pytest](https://docs.pytest.org/en/latest/)
* `OPTIONAL` [pipenv](https://docs.pipenv.org/)

### Installation
First, clone the repository or download the ZIP. Then, install Python. If you
choose to use pipenv to install dependencies, install pipenv through
[pip](https://pip.pypa.io/en/stable/quickstart/). Otherwise, install all
required packages through pip.

#### backports.lzma
Due to its dependency on the XZ Utils C library, pip/pipenv will most likely
fail to install backports.lzma. The simplest solution is to install this package
through Conda:

```bash
conda install -c conda-forge backports.lzma
```

For more details and options on installation of this package, see its
[description](https://pypi.org/project/backports.lzma/#installation).

#### pipenv
Start off by changing your shell's current working directory to the extracted
repository. If backports.lzma was installed through Conda, create the virtual
environment with access to the system's site-packages directory:

```bash
pipenv --site-packages
```

Follow it up with (or start with, if the above did not apply to you) the
following command to install dependencies from the pipfile:

```bash
pipenv install
```