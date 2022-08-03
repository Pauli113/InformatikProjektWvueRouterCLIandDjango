const fs = require('fs')

const lang = fs.readFileSync('./data/lang.yaml', {encoding: 'utf-8'});
console.log(lang);
