//calculate the quality points earned for each course
function qualityPoints(lgrade, credithrs){
  let qpoints
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
  
  return qpoints;
}

function getInputValue(){
  //retrieve values from HTML page
  let grade1 = document.getElementById("input1").value;
  let grade2 = document.getElementById("input2").value;
  let grade3 = document.getElementById("input3").value;
  let grade4 = document.getElementById("input4").value;
  let grade5 = document.getElementById("input5").value;
  let credit1 = Number(document.getElementById("input6").value);
  let credit2 = Number(document.getElementById("input7").value);
  let credit3 = Number(document.getElementById("input8").value);
  let credit4 = Number(document.getElementById("input9").value);
  let credit5 = Number(document.getElementById("input10").value);
  
  
  let totalQpoints = 0;
  let totalCredits = 0;
  const letterGrades = [grade1,grade2,grade3,grade4,grade5];
  let length = letterGrades.length;
  const courseCredits = [credit1,credit2,credit3,credit4,credit5];
  
  //iterate through and get our totals
  for (i=0; i < length; i++){
    totalQpoints += qualityPoints(letterGrades[i],courseCredits[i]);
    totalCredits += courseCredits[i];
    
  }
  //divide total quality points by the number of credit hours
  let cgpa = totalQpoints / totalCredits;

  alert("Your GPA is: " + cgpa)


  return;
}
