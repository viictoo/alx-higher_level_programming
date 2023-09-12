#!/usr/bin/node
// fs.appendFile( path, data[, options], callback )
// path: String, Buffer, URL or number that denotes the source filename or file descriptor that will be appended to.
// data: String or Buffer that denotes the data that has to be appended.
// options: It is an string or an object that can be used to specify optional parameters that will affect the output. It has three optional parameters:
//     encoding: It is a string which specifies the encoding of the file. The default value is ‘utf8’.
//     mode: It is an integer which specifies the file mode. The default value is ‘0o666’.
//     flag: It is a string which specifies the flag used while appending to the file. The default value is ‘a’.
// callback: It is a function that would be called when the method is executed.
//     err: It is an error that would be thrown if the method fails.

const fs = require('fs');

const argv = process.argv.slice(2);

fs.readFile(argv[0], (err, content) => {
  if (err) throw err;
  fs.appendFile(argv[2], content, (err) => { if (err) throw err; });
});

fs.readFile(argv[1], (err, content) => {
  if (err) throw err;
  fs.appendFile(argv[2], content, (err) => { if (err) throw err; });
});
