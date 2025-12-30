from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'id_parampkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Reoto Koya',
    maintainer_email='s24c1053jd@s.chibakoudai.jp',
    description='IDを読み取り、許可されたIDのみをパスするパッケージです.',
    license='BSD-3-Clause',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'id_talker = id_parampkg.id_param_talker:main',
            'id_listener = id_parampkg.id_param_listener:main',
        ],
    },
)
