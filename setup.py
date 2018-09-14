from setuptools import setup

def readme():
      with open("README.md", r, encoding="UTF-8") as f:
            return f.read()

setup(name='pyMetrics',
      version='0.1',
      description='Python code ast manipulation',
      url='https://github.com/seantyh/pyMetrics',
      author='Sean Tseng',
      author_email="seantyh@gmail.com",
      license='CC-BY',
      packages=['pyMetrics'],
      install_requires=['numpy', 'scipy'],
      test_suite='tests')
