import setuptools

setuptools.setup(
    name='pycrystalfield',
    version='0.1.0',    
    description='Code to calculate the crystal field Hamiltonian of magnetic ions.',
    url='https://github.com/oberth-effect/PyCrystalField',
    author='Allen Scheie',
    author_email='',
    license='GNU GPL',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=['matplotlib',
                      'scipy',
                      'numba',                     
                      ],
    package_data={'pcf_lib':['*',]}
)