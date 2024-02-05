# Command Setup - Python 3

echo "Start setup..."
python3 -m venv .


echo "Activate virtual environment"
source bin/activate

echo "Install packages"
pip install -r ./requirements/base.txt

echo "Finished"