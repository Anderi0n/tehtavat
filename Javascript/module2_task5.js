
const numbers = [];
 
while (true) {
  const num = parseInt(prompt("Enter a number:"));
  
  if (numbers.includes(num)) {
    console.log("Number already given!");
    break;
  }
  
  numbers.push(num);
}
 
numbers.sort((a, b) => a - b);
 
console.log("All numbers in ascending order:");
for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i]);
}
