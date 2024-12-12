from setuptools import setup, find_packages

setup(
    name='sophy',
    version='0.1.0',
    packages=find_packages("./sophy"),
    install_requires=[
        'requests',
    ],
    author='Sidhart Krishnan',
    author_email='sidhartkrishnan@gmail.com',
    description='A Slack notification utility',
    long_description=open('README.md').read() if open('README.md').read() else '',
    long_description_content_type='text/markdown',
    url='https://github.com/SidhartK/python-sophy',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
