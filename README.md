# 🚧 **Software Engineering Project (Group 14)**

## 🖧 **API details**

| 🌱 Environment         | 🔗 URL                                                               |
|------------------------|----------------------------------------------------------------------|
| 🏭 Production Base URL |[api.pickmycourse.online](https://api.pickmycourse.online)            |
| 🖥️ Swagger Doc         |[api.pickmycourse.online/docs](https://api.pickmycourse.online/docs)  |

## 💻 **Web app details**

| 🌱 Environment  | 🔗 URL                                                    |
|-----------------|-----------------------------------------------------------|
| 📱 Vue frontend |[pickmycourse.vercel.app](https://pickmycourse.vercel.app) |

## 💫 **To deploy the API using Docker**
- Well it goes without saying, make sure you have [Docker installed on your system](https://docs.docker.com/engine/install)
- `cd server`
- `cp .env.example .env`
- Make sure to edit the `.env` file with proper details
- To quickly get a MariaDB instance running, run `docker run --name mariadb-dev -v /path/on/your/system:/var/lib/mysql:Z -e MARIADB_DATABASE=some-db-name -e MARIADB_ROOT_PASSWORD=strong-root-password -p 3306:3306 -d mariadb:latest`
- `sh deploy.sh`

## **[⛏️ Check Projects](https://github.com/orgs/se-sept-14-draft-work/projects/1)**
