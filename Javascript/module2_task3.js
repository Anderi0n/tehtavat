const dogs = [];
 
for (let i = 1; i <= 6; i++) {
  const name = prompt(`Enter name for dog ${i}:`);
  dogs.push(name);
}
 
dogs.sort();
dogs.reverse();
 
let html = '<ul>';
for (let i = 0; i < dogs.length; i++) {
  html += `<li>${dogs[i]}</li>`;
}
html += '</ul>';
 
document.body.innerHTML = html;
