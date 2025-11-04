// Toggle show/hide for forms
function toggleForm(sectionId) {
    const formDiv = document.getElementById(sectionId + '-form');
    formDiv.style.display = formDiv.style.display === 'none' ? 'block' : 'none';
}

// Flash messages timeout
setTimeout(() => {
    const flashDiv = document.getElementById('flash-messages');
    if (flashDiv) flashDiv.remove();
}, 2000);

// Check if an item (book/author) is removable
function checkIfRemovable(url, selectId, formContainerId) {
    const itemId = document.getElementById(selectId).value;
    fetch(`${url}${itemId}`)
        .then(res => res.json())
        .then(data => {
            const isFree = data.free;
            const parent = document.getElementById(formContainerId);
            const message = parent.querySelector('.warning-message');
            const button = parent.querySelector('.delete-btn');
            if (isFree) {
                button.style.display = 'block';
                message.style.display = 'none';
            } else {
                message.style.display = 'block';
                button.style.display = 'none';
            }
        });
}

// Load existing book details for update
function loadBookData() {
    const bookId = document.getElementById('update-book-select').value;
    fetch(`/admin/get-book/${bookId}`)
        .then(res => res.json())
        .then(data => {
            document.getElementById('update-book-details').style.display = 'block';
            document.getElementById('update-book-id').value = data.book_id;
            document.getElementById('update-title').value = data.title;
            document.getElementById('update-subtitle').value = data.subtitle;
            document.getElementById('update-description').value = data.description;
            document.getElementById('update-author').value = data.author_id;
        });
}

// To handle the issue and return buttons in books
function handleBookCard(bookDiv){
    const available = parseInt(bookDiv.dataset.available);
    const total_copies = parseInt(bookDiv.dataset.total_copies);
    const issueBtn = bookDiv.querySelector(".issue-btn");
    const returnBtn = bookDiv.querySelector(".return-btn");
    if(available === total_copies){
        issueBtn.disabled = false;
    }else if(available === 0){
        returnBtn.disabled = false;
    }else{
        issueBtn.disabled = false;
        returnBtn.disabled = false;
    }
}


document.addEventListener("DOMContentLoaded", () => {
    const allBooks = document.querySelectorAll(".book-card");
    allBooks.forEach(bookDiv => handleBookCard(bookDiv));
});

function toggleTransForm(bookDiv, btn){
    const parent = document.getElementById(bookDiv);
    const issueForm = parent.querySelector('.issue-form');
    const returnForm = parent.querySelector('.return-form');
    if(btn){
        issueForm.style.display = 'block';
        returnForm.style.display = 'none';
    }else{
        issueForm.style.display = 'none';
        returnForm.style.display = 'block';
    }
}

function checkStudent(url, parentDiv) {
    const parent = document.getElementById(parentDiv);
    const studentId = parent.querySelector('.issue-form').querySelector('.student-id').value;
    fetch(`${url}${studentId}`)
        .then(res => res.json())
        .then(data => {
            const isFree = data.free;
            //const parent = document.getElementById(formContainerId);
            const form = parent.querySelector('.student-info-form');
            const button = form.querySelector('.issue-btn-2');
            form.style.display = 'block';
            form.querySelector('.student-id').value = studentId;
            form.querySelector('.student-name').innerText = data.student_name;
            form.querySelector('.student-branch').innerText = data.student_branch;
            if (isFree) {
                button.disabled = false;
                button.innerText = 'Issue to Student';
            } else {
                button.disabled = true;
                button.innerText = 'Limit Exceeded';
            }
        });
}