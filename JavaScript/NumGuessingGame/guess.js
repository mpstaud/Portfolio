let firstVal;
let secVal;
let randVal = Math.floor(Math.random() * 10 + 1);
secVal = randVal;
let attempts = 5;


function numtries() {
    if (attempts == 0) {
      alert("You are out of attempts!");
      window.location.replace("./gameover.html");
    } else {
      alert(attempts + " attempts remaining");
      
    }
}

function compValues() {
  if (secVal == firstVal) {
    alert("You Guessed it!");
  } else {
    attempts = attempts - 1;
    alert("Not quite!");
    numtries();
  }
}



function getInputValue() {
  let inputVal = document.getElementById("myInput").value;
  firstVal = inputVal;

  compValues();

  return;
}



