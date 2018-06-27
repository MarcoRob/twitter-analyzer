

const express = require('express');
const app = express();
const bodyparser = require('body-parser')
const fs = require("fs"),
    readline = require('readline');



app.use(bodyparser.json())


app.get("/api/counts", function(req, res){
  var filename = "twitter-mapreduce/serial_sorted.txt"
  /*fs.readFile(filename, 'utf8', function(err, data) {
    if (err) throw err;
    console.log('OK: ' + filename);
    var content = data.split("\t");
    res.send(content)
  });*/
  var rd = readline.createInterface({
      input: fs.createReadStream(filename),
      output: process.stdout,
      console: false
  });
  var obj = {}
  res.write("<table border='1' padding='50em'><tr><td><b>Name</b></td><td><b>Count</b></td></tr>")
  rd.on('line', function(line) {
      var regex = /(mex)|(mx)|(Mex)|(MEX)|(suec)|(Suec)|(SUEC)\w/g
      if(regex.test(line) === true) {
        console.log(true)
        console.log(line)
        var data = line.split("\t");
        res.write("<tr><td>"+data[0]+"</td><td>"+data[1]+"</td></tr>")
      }
      
      //console.log(JSON.stringify(obj))
  });
  rd.on('end', function() {
    res.write("</table>")
    res.end()
  });
  
  //console.log(JSON.stringify(obj))
})

app.get('/', function (req, res) {
  res.send('Hello World!');
});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});