
const numbers = [];
 
while (true) {
  const num = parseInt(prompt("Enter a number (0 to stop):"));
  if (num === 0) {
    break;
  }
  numbers.push(num);
}
 
numbers.sort((a, b) => b - a);
 
console.log("Numbers from largest to smallest:");
for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i]);
}
