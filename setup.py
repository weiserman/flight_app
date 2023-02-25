from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in flight_management/__init__.py
from flight_management import __version__ as version

setup(
	name="flight_management",
	version=version,
	description="SAP Flight App",
	author="DataGimbal (Pty) Ltd",
	author_email="admin@datagimbal.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
