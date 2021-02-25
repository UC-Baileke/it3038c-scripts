var fs = require("fs");
var http = require("http");
var os = require("os");
var ip = require("ip");

var server = http.createServer(function(req, res) {
    if (req.url === "/" ) {
        fs.readFile("./public/index.html", "UTF-8", function(err,body){
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);    
        })
    }

    else if(req.url.match("/sysinfo")) {
        //code from ourcodeworld for the conversion into MB for memory
        /**
         * Converts a long string of bytes into a readable format e.g KB, MB, GB, TB, YB
         * 
         * @param {Int} num The number of bytes.
         */
        function readableBytes(bytes) {
            var i = Math.floor(Math.log(bytes) / Math.log(1024)),
            sizes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'];

            return (bytes / Math.pow(1024, i)).toFixed(2) * 1 + ' ' + sizes[i];
        }
        
        myHostName=os.hostname();
        myTotalMem=os.totalmem();
        myUpTime=os.uptime();
          //code obtained from stack overflow to assist with converting seconds of server uptime into days/hours/mins/seconds
          var seconds = myUpTime;

          var days = Math.floor(seconds / (3600*24));
          seconds  -= days*3600*24;
          var hrs   = Math.floor(seconds / 3600);
          seconds  -= hrs*3600;
          var mnts = Math.floor(seconds / 60);
          seconds  -= mnts*60;
        myFreeMem=os.freemem();
        myNumCPU=os.cpus();
        const numOfCpus = os.cpus().length
        ServerUptime=days+" days, "+hrs+" Hrs, "+mnts+" Minutes, "+seconds+" Seconds"
        html=`
        <!DOCTYPE html>
        <head>
            <title>Node JS Response</title>
        </head>
        <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: ${ServerUptime} </p>
            <p>Total Memory: ${readableBytes(myTotalMem)} </p>
            <p>Free Memory: ${readableBytes(myFreeMem)}  </p>
            <p>Number of CPUs: ${numOfCpus} </p>
        </body>
        </html>
        ` 
        res.writeHead(200, {"Content-Type" : "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File not Found at ${req.url}`);
    }

});

server.listen(3000);
console.log("Server listening on port 3000");
