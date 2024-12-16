# wfp-survey-toolbox

<div align="center">

[![Build status](https://github.com/WFP-VAM/wfp-survey-toolbox/workflows/build/badge.svg?branch=master&event=push)](https://github.com/WFP-VAM/wfp-survey-toolbox/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/wfp-survey-toolbox.svg)](https://pypi.org/project/wfp-survey-toolbox/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/WFP-VAM/wfp-survey-toolbox/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/WFP-VAM/wfp-survey-toolbox/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/WFP-VAM/wfp-survey-toolbox/releases)
[![License](https://img.shields.io/github/license/WFP-VAM/wfp-survey-toolbox)](https://github.com/WFP-VAM/wfp-survey-toolbox/blob/master/LICENSE)
![Coverage Report](assets/images/coverage.svg)

Package containing functionality to analyse WFP surveys.

</div>

## Very first steps

### Initialize your code

1. Initialize `git` inside your repo:

```bash
cd wfp-survey-toolbox && git init
```

2. If you don't have `uv` installed run:

```bash
pip install uv
```

3. Initialize uv and install `pre-commit` hooks:

```bash
uv venv
make pre-commit-install
```

4. Run the codestyle:

```bash
make check-codestyle
```

5. Upload initial code to GitHub:

```bash
git add .
git commit -m ":tada: Initial commit"
git branch -M main
git remote add origin https://github.com/WFP-VAM/wfp-survey-toolbox.git
git push -u origin main
```