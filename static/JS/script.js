// FORM OPEN AND CLOSE
function toggleForm(formId){
    const formDiv = document.getElementById(formId + '-Form');
    if(formDiv.style.display === "none"){
        formDiv.style.display = 'block';
    }else{
        formDiv.style.display = 'none';
    }
}

// FLASH MESSAGES TIMEOUT
setTimeout(() => {
    const flashDiv = document.getElementById('flash-messages');
    if (flashDiv) {
      flashDiv.remove();
    }
  }, 2000);


// IS THE BOOK OR AUTHOR POSSIBLE TO REMOVE? (INVOLVED IN NO LINKS)
function isRemovalPossible(url, selectId, parentDivId){
    const id = document.getElementById(selectId).value;
    fetch(`${url}${id}`)
        .then(response => response.json())
        .then(data =>{
            const isFree =  data.free;
            console.log(isFree);
            const parent = document.getElementById(parentDivId);
            const msg = parent.querySelector('.message');
            const button = parent.querySelector('.deleteButton');
            if(isFree){
                button.style.display = 'block';
                msg.style.display = 'none';
            }else{
                msg.style.display = 'block';
                button.style.display = 'none';
            }
        });
}
