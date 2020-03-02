from setuptools import setup

setup(name='funniest',
      version='0.1',
      description='The funniest joke in the world',
      url='http://github.com/storborg/funniest',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      include_package_data=True,
      packages=['funniest'],
      package_dir={'funniest': 'funniest'},
      package_data={'funniest': ['data/*.txt']},
      zip_safe=False)
