var new_task_planning = document.querySelector('#new-task-planning')
var new_task_progress = document.querySelector('#new-task-progress')
var new_task_review = document.querySelector('#new-task-review')
var new_task_finished = document.querySelector('#new-task-finished')

var new_task_modal = document.querySelector("#new-task-modal");
var submit = document.querySelector('#modal-submit');

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

new_task_planning.addEventListener("click", openModal);
new_task_progress.addEventListener("click", openModal);
new_task_review.addEventListener("click", openModal);
new_task_finished.addEventListener("click", openModal);

span.addEventListener("click", closeModal);
submit.addEventListener("click", onSubmit)

function addClassToSubmit(id){
  if(id == 'new-task-planning'){
    document.getElementById("modal-submit").classList.add('planning')
  } else if(id == 'new-task-progress'){
    document.getElementById("modal-submit").classList.add('progress')
  } else if(id == 'new-task-review'){
    document.getElementById("modal-submit").classList.add('review')
  } else if(id == 'new-task-finished'){
    document.getElementById("modal-submit").classList.add('finished')
  }
}
function removeClassSubmit(){
  var status = document.getElementById("modal-submit")
  status.className = 'submit-new-task'
}

function openModal() {
  addClassToSubmit(this.id)
  new_task_modal.style.display = "block";
}

function closeModal(){
  new_task_modal.style.display = "none";
}

function onSubmit(event){
  event.preventDefault()
  // console.log(this)

  var title = document.querySelector('#title')
  var description = document.querySelector('#description')
  var author = document.querySelector('#author')
  var priority = document.querySelector('#priority')
  var duration = document.querySelector('#duration')
  var status = document.getElementById("modal-submit").className.slice(16)
  removeClassSubmit()


  var request = {
    title: title.value,
    description: description.value,
    creator: author.value,
    priority: priority.value,
    completion_time: duration.value,
    status: status
  }
  var url = 'http://bb97c023c004.ngrok.io/task'

  postRequest(request, url)

}

function postRequest(request, url){
  var http = new XMLHttpRequest();
  var params = 'title=test&creator=1';
  http.open('POST', url, true);

  //Send the proper header information along with the request
  // http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
  http.setRequestHeader('Content-type', 'text/plain');
  http.send(JSON.stringify(request));
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == new_task_modal) {
    new_task_modal.style.display = "none";
  }
}