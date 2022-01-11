from setuptools import setup

package_name = 'simple_pubsub_python'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lch',
    maintainer_email='yuipo190@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'basic_publisher = simple_pubsub_python.basic_publisher:main',
            'natural_number_generator = simple_pubsub_python.natural_number_generator:main',
            'sum_calculator = simple_pubsub_python.sum_calculator:main',
            'factorial_calculator = simple_pubsub_python.factorial_calculator:main',
        ],
    },
)
