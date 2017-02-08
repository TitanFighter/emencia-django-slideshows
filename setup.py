import pip

from setuptools import setup, find_packages

flat_installed_packages = [package.project_name for package in pip.get_installed_distributions()]

if 'django-filebrowser' in flat_installed_packages:
    install_requires = ['Django>=1.7']
else:
    install_requires = [
        'Django>=1.7',
        'django-filebrowser-no-grappelli>=3.5.6',
    ]

setup(
    name='emencia-django-slideshows',
    version=__import__('slideshows').__version__,
    description=__import__('slideshows').__doc__,
    long_description=open('README.rst').read(),
    author='David Thenon',
    author_email='dthenon@emencia.com',
    url='http://pypi.python.org/pypi/emencia-django-slideshows',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=install_requires,
    include_package_data=True,
    zip_safe=False
)