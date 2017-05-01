# [Vue.js](vuejs) SPA & [Japronto](japronto) REST server example*
SPA -- single page web application <br/>
REST -- representative state transfer

## Getting started
Make sure the following software is installed and is in the PATH.
* [Node.js](nodejs) and [npm](npm)
* Python 3.5 or higher and pip
* [MongoDB](mongo)

Checkout repository and run following commands inside the repo
root. It will install all necessary front-end and back-end dependencies.
```sh
pip install -r requirements.txt
npm install
```
Then build front-end by running
```sh
npm run build
```
Before running Japronto server, first start MongoDB server as
follows or change DB connection string in `server/config.py`
if you have existing MongoDB instance.
```sh
npm run mongo
```
To start Japronto server execute, by default it will start
HTTP server at `localhost:5432`.
```sh
npm run dev  # debug environment
npm run prod # production environment
```

[vuejs]:    https://github.com/vuejs/vue
[japronto]: https://github.com/squeaky-pl/japronto
[mongo]:    https://github.com/mongodb/mongo
[nodejs]:   https://github.com/nodejs/node
[npm]:      https://github.com/npm/npm
