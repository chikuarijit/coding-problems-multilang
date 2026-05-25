namespace Problem2{
    const promptSync = require("prompt-sync")();


    function isPrime(num: number): boolean {
        if (num <= 1) {
            return false;
        }
        for (let i = 2; i <=Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    const number: number = parseInt(promptSync("Enter a number: ")!);
    console.log(number + " is prime: " + isPrime(number))
}
