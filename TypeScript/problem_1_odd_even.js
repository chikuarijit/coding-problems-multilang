"use strict";
const promptSync = require("prompt-sync")();
const number = parseInt(promptSync("Enter a number: "));
if (number % 2 === 0) {
    console.log(number + " is even");
}
else {
    console.log(number + " is odd");
}
