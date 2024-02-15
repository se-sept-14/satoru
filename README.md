# 🚧 **Software Engineering Project (Group 14)**

### **[⛏️ Check Projects board](https://github.com/orgs/se-sept-14-draft-work/projects/1)**

## 🖧 **API details**
| 🌱 Prod Environment | 🔗 URL |
|----------------------|--------|
| 🖥️ Swagger Doc      | /docs   |

## 🛢️ **Run a MariaDB instance**
```sh
docker run --name mariadb-dev \
  -v /path/on/your/system:/var/lib/mysql:Z \
  -e MARIADB_DATABASE=db_name \
  -e MARIADB_ROOT_PASSWORD=strong-root-password \
  -p 3306:3306 \
  -d mariadb:latest
```
If you are on Windows and don't have docker installed on your system, you can download and install [MariaDB from here](https://dev.mysql.com/downloads/installer) (MariaDB and MySQL are more or less the same thing)

## 🏃‍♀️ **To run this locally on your machine**
<blockquote>
You'll need MariaDB/MySQL for this API to work.

Follow the steps mentioned above to quickly spin up a MariaDB/MySQL instance using docker, either on your local machine or some remote machine. If you don't want to use Docker, follow the MariaDB/MySQL documentation then.

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
- To run the client
  - `cd client`
  - `npm install`
  - `npm run dev`

## 💫 **To deploy the API**

👉️ **Then, follow the steps to deploy the ⚡️ FastAPI server**
- `cd server`
- `cp .env.example .env`
- Make sure to edit the `.env` file with proper details
- `sh deploy.sh`

## 🩺 **To test the API endpoints**
- Create and activate the environment as described above, install requirements
- Run the `pytest.sh` script
  - `cd server`
  - `sh pytest.sh`

## 💉 **For writing tests**
- The directory name has to be `tests`
- The filename must start with `test_`
  - Example: Use name like `test_auth.py` to make tests for `auth.py` endpoints
