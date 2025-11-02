//admin-modals
function openModal(modalId){
    const modal = document.getElementById(modalId);
    modal.style.display = 'flex';
    window.onclick = function(event){
        if(event.target === modal){
            modal.style.display = 'none';
        }
    };
}

function closeModal(modal){
    document.getElementById(modal).style.display = 'none';
}
setTimeout(() => {
    const flashDiv = document.getElementById('flash-messages');
    if (flashDiv) {
      flashDiv.remove();
    }
  }, 2000);