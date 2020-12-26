python3 -m pip install --user --upgrade setuptools wheel

python3 setup.py sdist bdist_wheel
python3 -m venv env
source ./env/bin/activate 
bash build.sh && pip install ./dist/ai42-1.0.0.tar.gz --user