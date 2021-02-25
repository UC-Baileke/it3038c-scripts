var path = require("path");

var hello = "Hello from Node JS Variable"
console.log(`Printing variable hello: ${hello}`)

console.log("directory name: " + __dirname)
console.log("durectiry and file name: " + __filename)


console.log("Using PATH Module:")
console.log(`Hello from file ${path.basename(__filename)}`)

console.log(`process args: ${process.argv}`)