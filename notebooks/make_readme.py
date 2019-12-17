"""MIDOSS Jupyter Notebook collection README generator

Copyright 2018 the MIDOSS project contributors,
the University of British Columbia,
and Dalhousie University.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import datetime
import json
import os
import re


nbviewer = "https://nbviewer.jupyter.org/urls"
repo = "bitbucket.org/midoss/analysis-doug/raw/default"
repo_dir = "notebooks"
url = os.path.join(nbviewer, repo, repo_dir)
title_pattern = re.compile("#{1,6} ?")
readme = """The Jupyter Notebooks in this directory are made by Doug for
sharing of Python code techniques and notes about model results analysis
code.

The links below are to static renderings of the notebooks via
[nbviewer.jupyter.org](https://nbviewer.jupyter.org/).
Descriptions below the links are from the first cell of the notebooks
(if that cell contains Markdown or raw text).

"""
notebooks = (fn for fn in os.listdir("./") if fn.endswith("ipynb"))
for fn in notebooks:
    readme += f"* ## [{fn}]({url}/{fn})  \n    \n"
    with open(fn, "rt") as notebook:
        contents = json.load(notebook)
    try:
        first_cell = contents["worksheets"][0]["cells"][0]
    except KeyError:
        first_cell = contents["cells"][0]
    first_cell_type = first_cell["cell_type"]
    if first_cell_type in "markdown raw".split():
        desc_lines = first_cell["source"]
        for line in desc_lines:
            suffix = ""
            if title_pattern.match(line):
                line = title_pattern.sub("**", line)
                suffix = "**"
            if line.endswith("\n"):
                readme += f"    {line[:-1]}{suffix}  \n"
            else:
                readme += f"    {line}{suffix}  "
        readme += "\n" * 2
this_year = datetime.date.today().year
license = f"""
##License

These notebooks and files are copyright {this_year}
by the the MIDOSS project contributors,
the University of British Columbia,
and Dalhousie University.

They are licensed under the Apache License, Version 2.0.
http://www.apache.org/licenses/LICENSE-2.0
Please see the LICENSE file for details of the license.
"""
with open("README.md", "wt") as f:
    f.writelines(readme)
    f.writelines(license)
