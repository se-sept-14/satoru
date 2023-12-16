# 🚧 **Software Engineering Project (Group 14)**

## 🖧 **API details**

| 🌱 Prod Environment | 🔗 URL                                                              |
|---------------------|---------------------------------------------------------------------|
| 🏭 Base URL         |[api.pickmycourse.online](https://api.pickmycourse.online)           |
| 🖥️ Swagger Doc      |[api.pickmycourse.online/docs](https://api.pickmycourse.online/docs) |

## 💻 **Web app details**

| 🌱 Environment  | 🔗 URL                                           |
|-----------------|---------------------------------------------------|
| 📱 Vue frontend |[pickmycourse.online](https://pickmycourse.online) |

### **[⛏️ Check Projects board](https://github.com/orgs/se-sept-14-draft-work/projects/1)**

## 💫 **To deploy the API using Docker**
> Well it goes without saying, make sure you have [Docker installed on your system](https://docs.docker.com/engine/install)

### 🛢️ **Run a MariaDB instance**
> To quickly get a MariaDB instance running, run the following 👇️
```sh
docker run --name mariadb-dev \
  -v /path/on/your/system:/var/lib/mysql:Z \
  -e MARIADB_DATABASE=some-db-name \
  -e MARIADB_ROOT_PASSWORD=strong-root-password \
  -p 3306:3306 \
  -d mariadb:latest
```
Also need to migrate the peewee DB models to MariaDB, look into the [`peewee-migrate` tool](https://github.com/klen/peewee_migrate)

👉️ **Then, follow the steps to deploy the ⚡️ FastAPI server**
- `cd server`
- `cp .env.example .env`
- Make sure to edit the `.env` file with proper details
- `sh deploy.sh`

## 🏃‍♀️ **To run this locally on your machine**
<blockquote>
You'll need MariaDB for this API to work.

Follow the steps mentioned above to quickly spin up a MariaDB instance using docker, either on your local machine or some remote machine. If you don't want to use Docker, follow the MariaDB documentation then.

You'll also need to make a copy of `.env` file with proper details (`.env.example` is given). Follow the below steps next:
</blockquote>

- Use Git Bash on Windows (avoid using `cmd` or `powershell`) [Better if you use WSL](https://learn.microsoft.com/en-us/windows/wsl/)
  - `cd server`
- Create & activate python virtual environment
  - [Linux]() 👉️ `python3 -m venv .venv`
  - [Windows or `conda`]() 👉️ `python -m venv .venv`
  - [Linux]() 👉️ `source .venv/bin/activate`
  - [Windows]() 👉️ `source .venv/Scripts/activate`
- Install the requirements
  - `pip install -r requirements.txt`
- Run it using the shell script
  - `sh run.sh`

## 🩺 **To test the API endpoints**
- Create and activate the environment as described above, install requirements
- Run the `pytest.sh` script
  - `sh pytest.sh`

## 💉 **For writing tests**
- The directory name has to be `tests`
- The filename must start with `test_`
  - Example: Use name like `test_auth.py` to make tests for `auth.py` endpoints
