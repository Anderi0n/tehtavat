const numParticipants = parseInt(prompt("Enter number of participants:"));
const participants = [];
 
for (let i = 1; i <= numParticipants; i++) {
  const name = prompt(`Enter name for participant ${i}:`);
  participants.push(name);
}
 
participants.sort();
 
let html = '<ol>';
for (let i = 0; i < participants.length; i++) {
  html += `<li>${participants[i]}</li>`;
}
html += '</ol>';
 
document.body.innerHTML = html;
