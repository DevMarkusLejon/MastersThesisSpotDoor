
from glob import glob
import os
from setuptools import find_packages, setup

PACKAGE_NAME = "spot_bt_test"

setup(
    name=PACKAGE_NAME,
    version="0.0.0",
    packages=[PACKAGE_NAME],
    data_files=[
        ("share/ament_index/resource_index/packages", [f"resource/{PACKAGE_NAME}"]),
        (f"share/{PACKAGE_NAME}", ["package.xml"]),
    ],
    install_requires=["setuptools", "py_trees", "py_trees_os"],
    zip_safe=True,
    maintainer="sundt-lejon",
    maintainer_email="sundtfredrik@gmail.com",
    description="Testing the capabilities of spot bt",
    license="TODO",
    test_require=["pytest"],
    entry_points={
        'console_scripts': [
		'stand_walk_sit_bt = spot_bt_test.stand_walk_sit_bt:main',
		'spot_arm_demo = spot_bt_test.demo_arm:main',
        ],
    },
)
