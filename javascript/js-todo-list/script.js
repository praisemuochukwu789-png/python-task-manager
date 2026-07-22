let task = document.getElementById('todo-ctn')
window.onload = function() {
    let savedTasks = localStorage.getItem("myTodoList");
    if (savedTasks) {
        task.innerHTML = savedTasks; // Put the saved HTML back into the container
    }
}
// Listen for the Enter key press on the input box
// Listen for the keypress on the entire window instead
window.addEventListener('keypress', function(event) {
    // 1. Only run if the user hits Enter
    // 2. AND only run if they are actually typing inside your input box
    if (event.key === 'Enter' && document.activeElement.id === 'input_value') {
        createList(); 
    }
});
function createList(){
    let input_value = document.getElementById('input_value')
    if (input_value.value == "") { return; } 
    task.innerHTML += 
     `<div class="lists">
        <span class="txt-color">${input_value.value}</span>
            <span class="btn-wrapper">
            <button class="edit-btn" onclick="editTask(this)">EDIT</button>
            <button class="complete-btn" onclick="completeTask(this)">COMPLETED</button>
            <button class="del-btn" onclick="deleteTask(this)">DELETE</button>
        </span>
    </div>`;
    document.getElementById('input_value').value = "";
    saveToStorage(); // Save the new list
}
function completeTask(button) {
    const textSpan = button.closest('.lists').querySelector('.txt-color');
    textSpan.style.textDecoration = textSpan.style.textDecoration === "line-through" ? "none" : "line-through";
    textSpan.style.opacity = textSpan.style.textDecoration === "line-through" ? "0.5" : "1";
    saveToStorage();
}

// 2. Function to handle the Edit button
function editTask(button) {
    const textSpan = button.closest('.lists').querySelector('.txt-color');
    let currentText = textSpan.textContent;
    let newText = prompt("Edit your task:", currentText);
    
    if (newText !== null && newText.trim() !== "") {
        textSpan.textContent = newText;
        saveToStorage();
    }
}
function deleteTask(button) {
    button.closest('.lists').remove();
    saveToStorage(); // Save the list after deleting an item
}
function saveToStorage() {
    // Saves the raw HTML inside the container into the browser's brain under the key "myTodoList"
    localStorage.setItem("myTodoList", task.innerHTML);
}