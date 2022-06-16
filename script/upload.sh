rm -rf ./dist/* ./build/*
python setup.py sdist
python setup.py bdist_wheel
twine upload dist/*


