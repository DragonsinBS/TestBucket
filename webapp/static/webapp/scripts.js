document.addEventListener('DOMContentLoaded',()=>{
  var count=0;
  document.getElementById('add_question').onclick=()=>{
    if(count == 0){
      document.getElementById('create_test').disabled=false;
    }
    if(count>10){
      alert("Only 10 questions allowed");
      return false;
    }
    count++;
    document.getElementById('questions').innerHTML+=`<br><li>
   <textarea name="question-${count}" rows=5 cols=50 required></textarea>
   <ol id="options" type="A">
      <li  class="white""><input required name="question-${count}-A"></li>
      <li  class="white"><input required name="question-${count}-B"></li>
      <li  class="white"><input required name="question-${count}-C"></li>
      <li  class="white"><input required name="question-${count}-D"></li>
   </ol>
   <label>Correct Option:</label><select name="correct">
    <option value='A'>Option A</option>
    <option value='B'>Option B</option>
    <option value='C'>Option C</option>
    <option value='D'>Option D</option>
   </select>
   </li>`;
    document.getElementById('count').value=count;
    return false;
  };
});
