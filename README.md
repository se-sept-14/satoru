## 🚧 **Software Engineering Project (Group 14)**

### **To run the api server**
- `cd server`
- [OPTIONAL]() Create an environment
  - On Windows Powershell
    - `python -m venv .venv`
    - `.venv\Scripts\activate`
  - On Windows Git Bash or Linux or Mac
    - `python3 -m venv .venv`
    - `source .venv/bin/activate`
- Install dependencies `pip install -r requirements.txt`
- Run the api server
  - On Windows Powershell
    - `uvicorn main:app --port 5000 --reload`
  - On Windows Git Bash or Linux or Mac
    - `sh run.sh`
- You can use something like Insomnia, Postman or ThunderClient to test APIs
  - Or, just visit [http://localhost:5000/docs](http://127.0.0.1:5000/docs) to open Swagger and test the endpoints there