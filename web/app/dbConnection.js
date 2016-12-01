const MongoClient = require('mongodb').MongoClient;
const EventEmitter = require('events');


class DbConnection extends EventEmitter {

    constructor() {
        super();
        MongoClient.connect('mongodb://db:27017/sqwaks', (err, db) => {
            if(err) console.log(err);
            this._db = db;
            this.emit('dbConnected');        
        });
    }

    get db () {
        return this._db;
    }
}

module.exports = new DbConnection();