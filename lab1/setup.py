from setuptools import find_packages, setup
from glob import glob

package_name = 'lab1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ("share/" + package_name, glob("launch_folder/lab1_launch.py")),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='simone',
    maintainer_email='simone@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "publisher = lab1.image_publisher:main",
            "subscriber = lab1.image_subscriber:main",
        ],
    },
)
