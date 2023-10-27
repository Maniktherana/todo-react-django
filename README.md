# React + Django + Mongo + Docker Todo App

## Setup

1. Clone this repository

```bash
git clone https://github.com/Maniktherana/todo-react-django.git
```

2. Add a `.env` in the root directory of the project as well as in the src/rest directory according to the `.env.example` files.

3. Build container (you only need to build containers for the first time or if you change image definition, i.e., `Dockerfile`). This step will take a good amount of time.

```bash
docker-compose build
```

4. Once the build is completed, start the containers:

```bash
docker-compose up -d
```

5. Once complete, `docker ps` should output something like this:

```bash
CONTAINER ID   IMAGE               COMMAND                  CREATED         STATUS         PORTS                      NAMES
e445be7efa61   adbrew_test_api     "bash -c 'cd /src/re…"   3 minutes ago   Up 2 seconds   0.0.0.0:8000->8000/tcp     api
0fd203f12d8a   adbrew_test_app     "bash -c 'cd /src/ap…"   4 minutes ago   Up 3 minutes   0.0.0.0:3000->3000/tcp     app
884cb9296791   adbrew_test_mongo   "/usr/bin/mongod --b…"   4 minutes ago   Up 3 minutes   0.0.0.0:27017->27017/tcp   mongo
```

6. Check that you are able to access <http://localhost:3000> and <http://localhost:8000/todos>
