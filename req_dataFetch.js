const fs = require('fs');
const axios=require("axios")
async function request_data(){
response= await axios("https://saral.navgurukul.org/api/courses")
let d=response.data;
const data = JSON.stringify(d,null,4);
fs.writeFile('data.json', data, (err) => {
    if (err) {
        throw err;
    }
    console.log("JSON data is saved.");
});

}
request_data()
