namespace Problem6{
    const promptSync = require("prompt-sync")();

    function reverse(num: number): number {
        let result = 0
        let temp = 0
        while(num > 0){
            temp = num % 10
            result = (result * 10) + temp
            num = Math.floor(num/10);
        }
        return result
    }

    const num: number = parseInt(promptSync("Enter a number: ")!);
    console.log(`Reverse of ${num} is: ${reverse(num)}`);
}