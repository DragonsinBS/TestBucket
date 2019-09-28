document.addEventListener('DOMContentLoaded',()=>{
  var count=0;
  document.getElementById('add_question').onclick=()=>{
    count+=1;
    document.getElementById('questions').innerHTML+=`<li>Question no ${count}</li>`;
  };

});
