## if (you've done this before):

- Clone this repository
- Ensure you have MongoDB
- Create and activate a virtual environment with `./requirements.txt`
- Start MongoDB server
- Create environment variables:
    - `SENDER_USERNAME`
    - `SENDER_PASSWORD`
    - `SECRET_KEY`
    - `ADMIN_AID`
- Run `./vms.py` with `python`
- Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to dive in

## else:

- Install Miniconda. Download it from [here](https://docs.conda.io/en/latest/miniconda.html#) **OR** Use `virtualenv` for creating environment; and use `pip install -r requirements.txt` _instead_ of `conda create .....`
- Install MongoDB. Download the Community Server version [here](https://www.mongodb.com/download-center/community). Refer [this](https://docs.mongodb.com/manual/administration/install-community/) for further installation instructions.

- `git clone https://github.com/chttrjeankr/visitor-management-system.git`
- `cd visitor-management-system`
- `conda create --name vms --file requirements.txt`
- `conda activate vms`
- `sudo service mongod start`
- `sudo service mongod status`
- `touch .env` and create the environment variables
    - `SENDER_USERNAME`
    - `SENDER_PASSWORD`
    - `RECEIVER_EMAIL` (not mandatory)
    - `SECRET_KEY`
    - `ADMIN_AID`
- `python vms.py`
- `sudo service mongod stop`

- Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
