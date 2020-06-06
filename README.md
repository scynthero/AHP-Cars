# AHP-Cars
Django website for picking cars using AHP method

# How to install
git clone https://github.com/scynthero/AHP-Cars.git
<br />
cd AHP-Cars
<br />

linux -> python3 -m venv .env
<br />
windows -> python -m venv .env
<br />

linux -> source .env/bin/activate
<br />
windows -> .env\Scripts\activate
<br />

python3 -m pip install --upgrade pip
<br />
pip install -r requirements.txt
<br />
python3 manage.py makemigrations
<br />
python3 manage.py migrate --run-syncdb
<br />
python3 manage.py createsuperuser
<br />
python3 manage.py runserver