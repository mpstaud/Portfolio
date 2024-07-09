
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
  let credit1 = document.getElementById("input6").value;
  let credit2 = document.getElementById("input7").value;
  let credit3 = document.getElementById("input8").value;
  let credit4 = document.getElementById("input9").value;
  let credit5 = document.getElementById("input10").value;
  let totalCredits = credit1 + credit2 + credit3 + credit4 + credit5;
  const pointValues = new Array(qualityPoints(grade1,credit1),qualityPoints(grade2,credit2),qualityPoints(grade3,credit3),qualityPoints(grade4,credit4),qualityPoints(grade5,credit5));
  let length = pointValues.length;
  let totalQpoints = 0;
  for (let i=0; i < length; i++){
    totalQpoints += pointValues[i];
  }
  cgpa = totalQpoints / totalCredits;
  alert("Your GPA is: " + cgpa)

  return;
}
