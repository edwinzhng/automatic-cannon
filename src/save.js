var request = require("request");
var express = require('express');
var fsPath = require('fs-path');
var app = express();
var bodyParser = require('body-parser')

app.use( bodyParser.json() );       // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
  extended: true
}));
app.use(express.static('images'))

app.all('/', function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "X-Requested-With");
  next();
 });


// This responds a POST request for the homepage
app.post('/', function(req, res, next) {
  console.log(req.body);

	var base64 = req.body["content"];
        fsPath.writeFile("img.jpeg", base64, "base64", function(err){
            console.log("File saved");
        });

});

var server = app.listen(8081, function() {
    var host = server.address().address;
    var port = server.address().port;

    console.log("Example app listening at http://%s:%s", host, port)
});
