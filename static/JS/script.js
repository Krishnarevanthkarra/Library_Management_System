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
