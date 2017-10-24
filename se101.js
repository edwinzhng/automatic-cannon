const request = require('request');

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
    console.log(body);

    // get the coordinates of the top of the mouth
    var mouthX = body.tags.mouth_center.x; 
    var mouthY = body.tags.mouth_center.y;

    // get deviation from center of image
    var deltaX = mouthX - img_center_x;
    var deltaY = mouthY - img_center_y;

    // check left/right mouth position
    if (Math.abs(deltaX) > x_variance){
      if (deltaX > 0) { // the mouth is to the right in the image
        console.log("Move the servo left");
      } else { // the mouth is to the left in the image
        console.log("Move the servo right");
      }
    } else {
      console.log("X position is good");
    }

    // check up/down mouth position
    if (Math.abs(deltaY) > y_variance) {
     if (deltaY > 0) { // the mouth is too high in the image
        console.log("Move the servo down");
     } else { // the mouth is too low in the image
        console.log("Move the servo up");
     } 
    } else {
      console.log("Y position is good");
    }

  } else { // error
    console.log(response.body);
  }
});




