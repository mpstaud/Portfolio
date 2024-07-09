
let cgpa;

function qualityPoints(lgrade, credithrs){
  let qpoints;
  if (lgrade == "A"){
    qpoints = credithrs * 4;  
  }
  else if (lgrade == "B"){
    qpoints = credithrs * 3;
  }
  else if (lgrade == "C"){
    qpoints = credithrs * 2;
  }
  else if (lgrade == "D"){
    qpoints = credithrs;
  }
  else {
    qpoints = 0;
  }
  return qpoints;
}

function getInputValue(){
  let grade1 = document.getElementById("input1").value;
  let grade2 = document.getElementById("input2").value;
  let grade3 = document.getElementById("input3").value;
  let grade4 = document.getElementById("input4").value;
  let grade5 = document.getElementById("input5").value;
  
  const letterGrades = new Array(grade1,grade2,grade3,grade4,grade5);
  let length = letterGrades.length;
  for (let i=0; i < length; i++){
    
  }

  return;
}
