#!/usr/bin/env python3
from setuptools import find_packages, setup

package_name = 'simple_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='master',
    maintainer_email='master@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "sample_node = simple_py_pkg.sample_node:main",
            "counter_node = simple_py_pkg.counter_node:main",
            "channel_node = simple_py_pkg.television:main",
            "remote_controller_node = simple_py_pkg.remote_controller:main",
            "add_two_ints_server = simple_py_pkg.add_two_ints_server:main",
            "add_two_ints_client = simple_py_pkg.add_two_ints_client:main",
            "component_status_publisher = simple_py_pkg.components_status_publisher:main",
            "components_status_listener = simple_py_pkg.components_status_listener:main",
        ],
    },
)
