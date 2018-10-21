from setuptools import find_packages, setup

setup(
    name='movieblog',
    version='1.0.0',
    description='Blog about movies',
    author='Eugene Zabolotny',
    author_email='eugene.zabolotny@gmail.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
