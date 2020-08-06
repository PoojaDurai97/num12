from setuptools import setup

setup(
    name='num12',
    version='0.0.1',
    description='My private package from private github repo',
    url='https://github.com/PoojaDurai97/num12',
    author='Pooja Durai',
    author_email='poojadurai1997@gmail.com',
    license='unlicense',
    packages=['num12'],
    install_requires=[
       
        'pandas>=0.23.3',
        'numpy>=1.14.5',
        
    ]
    
)