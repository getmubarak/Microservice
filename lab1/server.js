'use strict';

const express = require('express');

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// App
const app = express();
app.get('/date', (req, res) => {
        console.log('entered get date');
        var datetime = new Date();
        
        var waitTill = new Date(new Date().getTime() + 5000);
        while(waitTill > new Date()){}
        
        res.send(datetime.toISOString());
        console.log('completed get date');
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
