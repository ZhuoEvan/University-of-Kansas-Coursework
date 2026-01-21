/*
* Title: EECS 468 Assignment 6
* Description: Remote Access to a File System
* Inputs: HTTP methods
* Output: The method function result
* Collaborators: EECS 468 Lecture Slides | developer.mozilla.org | Google Gemini
* Name: Evan Zhuo
* Date: 04/04/25
* Assignment6.js
*/

//Starting the Server | Used EECS 468 Lecture Slides
const {createServer} = require("http"); //Have a server that uses http
const methods = Object.create(null); //Have a variable for methods
createServer((request, response) => { //Start a server
    //Bypass CORS
    response.setHeader('Access-Control-Allow-Origin', '*'); //Allow all domains
    response.setHeader('Access-Control-Allow-Methods', '*'); //Allow HTTP methods
    response.setHeader('Access-Control-Allow-Headers', '*'); //Allow headers
    if (request.method === 'OPTIONS') { //Handle preflight OPTIONS request
        return response.end(); //immediately end the response
    }
    //Set the handler to a valid method | Invalid method will go to notAllowed function
    let handler = methods[request.method] || notAllowed; 
    handler(request) //Handle a method on a request
        .catch(error => { //Catch potential errors
            if (error.status != null) return error; //Return an error
            return {body: String(error), status: 500}; //Return status 500: Internal Server Error Message
        })
        .then (({body, status = 200, type = "text/plain"}) => { //Set status to 200 to proceed after error check
            response.writeHead(status, {"Content-Type": type}); //Assign the response header with the content type and ok status
            if (body && body.pipe) body.pipe(response); //Check if the body is a readable stream | Used Google Gemini
            else response.end(body); //End the response
        });
}).listen(8000) //Listen to Port 8000

const {parse} = require("url"); //Parse function from url module
const baseDirectory = process.cwd(); //Set baseDirectory current working directory of the process

//URL Path Function | Used EECS 468 Lecture Slides
function urlPath(url) {
    let {pathname} = parse(url); //Access the path of the url
    let path = resolve(decodeURIComponent(pathname).slice(1)); //Decode any URL-encoded characters in the path name | Used Google Gemini
    if (path != baseDirectory && !path.startsWith(baseDirectory + sep)) { //Check if it is a valid path
        throw {status: 403, body: "Forbidden"}; //Return status 403: Forbidden Message
    }
    return path; //Return path of the url
}

const {resolve, sep} = require("path"); //Resolve and sep function from path module

//PipeStream Function | Used EECS 468 Lecture Slides
function pipeStream(from, to) {
    return new Promise((resolve, reject) => { //Return a Promise
        from.on("error", reject); //Reject if an error is in from
        to.on("error", reject); //Reject if an error is in to
        to.on("finish", resolve); //Piping is complete 
        from.pipe(to); //Move data from the from to the to
    });
}

//notAllowed Function | Used EECS 468 Lecture Slides
async function notAllowed(request) {
    return {
        status: 405, //Status Code 405: Method not allowed
        body: `Method $(request.method) not allowed.` //Method not allowed message
    };
}

const {createReadStream} = require("fs"); //createReadStream function from fs module
const mime = require("mime"); //mime from mime module
const {stat, readdir} = require("fs").promises; //stat and readdir functions from fs module

//HTTP GET Function | Used EECS 468 Lecture Slides
methods.GET = async function (request) {
    let path = urlPath(request.url); //Set path to the request url
    let stats; //Initalize a stats variable
    try {
        stats = await stat(path); //Get the file or directory at the resolved path | Used Google Gemini
    } catch (error) { //Catch potential errors
        if (error.code != "ENOENT") throw error; //Throw a general error if error is not file not found
        else return {status: 404, body: "File not found"}; //Return status 404: File not found Message
    }
    if (stats.isDirectory()) { //Check if the data at the end of the resolved path is a directory
        return {body: (await readdir(path)).join("\n")}; //Read the directory and join the information together
    } else {
        return {body: createReadStream(path), //Return a readable stream of a file
                type: mime.getType(path)}; //Get the mime type
    }
}

const {createWriteStream} = require("fs"); //createWriteStream function from fs module
const {rmdir, unlink} = require("fs").promises; //rmdir and unlink functions from fs module

//HTTP PUT Function | Used EECS 468 Lecture Slides
methods.PUT = async function (request) {
    let path = urlPath(request.url); //Set path to the request url
    await pipeStream(request, createWriteStream(path)); //Write the request into the request url
    return {status: 204}; //return status 204: No Content; Successful Response | Used developer.mozilla.org
}

//HTTP DELETE Function | Used EECS 468 Lecture Slides
methods.DELETE = async function (request) {
    let path = urlPath(request.url); //Set path to the request url
    let stats; //Initalize a stats variable
    try {
        stats = await stat(path); //Get the file or directory at the resolved path | Used Google Gemini
    } catch (error) { //Catch potential errors
        if (error.code != "ENOENT") throw error; //Throw a general error if error is not file not found
        else return {status: 204}; //return status 204: No Content; Successful Response | Used developer.mozilla.org
    }
    if (stats.isDirectory()) await rmdir(path); //Check if the resolved path leads to a directory, remove the directory if true
    else await unlink(path); //Delete file using unlink at the resolved path
    return {status: 204}; //return status 204: No Content; Successful Response | Used developer.mozilla.org
}

//HTTP MKCOL Function | Used Google Gemini
methods.MKCOL = async (request) => {
    let path = urlPath(request.url); //Set path to the request url
    try {
        await mkdir(path, { recursive: true }); //Creating the directory
        return { status: 201 }; //Status 201: Successful 
    } catch (error) { //Catch potential errors
        console.error('Error creating directory:', error); //Print the error to the console
        return { status: 500, body: 'Error creating directory' }; //Return status 500: Internal Server Error Message
    }
}