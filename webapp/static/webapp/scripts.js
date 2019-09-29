document.addEventListener('DOMContentLoaded',()=>{
  var count=0;

  document.getElementById('add_question').onclick=()=>{
    if(count>10){
      alert("Only 10 questions allowed");
      return false;
    }
    question=document.getElementById('question').value;
    a=document.getElementById('option-a').value;
    b=document.getElementById('option-b').value;
    c=document.getElementById('option-c').value;
    d=document.getElementById('option-d').value;
    document.getElementById('questions').innerHTML+=`<li><h5> ${question}</h5><ol type="A"><li>${a}</li><li>${b}</li><li>${c}</li><li>${d}</li></ol></li>`;
    count++;

  };

});
