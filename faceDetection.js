const fs = require('fs');
const request = require('request');

const outFile = "coordinates.json";

// api config details
const api_key = "n3vg0dfc4j42o0ap4b54mm0msg";
const api_secret = "l20v0d9j4a7bnb7lqcqps7rddm";

// image constants
const img_url = "http://i4.mirror.co.uk/incoming/article10263400.ece/ALTERNATES/s615b/PROD-Kim-Jong-Un.jpg";
const img_width = 1000;
const img_height = 700;
const img_center_x = img_width / 2.0;
const img_center_y = img_height / 2.0;
const x_variance = 15.0; // satisfactory horizontal target range
const y_variance = 15.0; // satisfactory vertical target range

var url = "http://api.skybiometry.com/fc/faces/detect?api_key=" + api_key + "&api_secret=" + api_secret;
url += "&urls=" + img_url;

request.get(url, function (error, response, body){
  if (!error && response.statusCode == 200) {
    // success
    var data = JSON.parse(body);
    console.log(data.photos[0].tags[0]);


    var dataForWrite = data.photos[0].tags[0];
    
    fs.writeFile(outFile, JSON.stringify(dataForWrite), function (err) {
      if (err) return console.log(err);
         console.log("JSON saved to: " + outFile);
    });

  } else { // error
    console.log(response.body);
  }
});




