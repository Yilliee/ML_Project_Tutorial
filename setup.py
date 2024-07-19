from setuptools import setup, find_packages
try:
    with open('requirements.txt', 'r') as req_file:
        required_pkgs = [pkg.strip() for pkg in req_file.readlines()]
        
        if required_pkgs[-1] == "-e .":
            required_pkgs.pop()
except FileNotFoundError:
    required_pkgs = []

setup(
    name = "ML Project",
    version = "0.0.1",
    packages = find_packages(),
    install_requires = required_pkgs,
)
