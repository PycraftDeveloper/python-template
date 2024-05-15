from json import loads
from setuptools import setup, find_packages

author = "Author"
project_name = "ProjectName"
email = "Email"
description = "Description"
readme_file_type = "text/markdown"
project_url = "GitHub URL"
python_version_requirement = ">=3.6"

try:
    from requests import get
    requests_module_found = True
except ModuleNotFoundError:
    requests_module_found = False

if requests_module_found:
    tag_data = get(f"https://api.github.com/repos/{author}/{project_name}/tags")
    latest_tag = loads(tag_data.text)[0]["name"]
else:
    latest_tag = "0.0.0"

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

"""
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",]

python_requires = ">=3.6"
"""

setup(
    name = project_name,
    version = latest_tag,
    author = author,
    author_email = email,
    description = description,
    long_description = long_description,
    long_description_content_type = readme_file_type,
    url = project_url,
    project_urls = {
        "Bug Tracker": f"{project_url}/issues",
    },
    classifiers = [],
    package_dir = {"": "src"},
    packages = find_packages(where="src"),
    python_requires = python_version_requirement
)