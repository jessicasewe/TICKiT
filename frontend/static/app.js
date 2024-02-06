function likeButton(){
    let heart = document.querySelector('.heart');
    let likes = document.querySelector('.likes');
    if(heart.src.match("heart.png")){
        heart.src = "heart_red.png";
        likes.innerHTML = "5,490 likes";
    } else {
        heart.src = "heart.png";
        likes.innerHTML = "5,489 likes"
    }
}

// like button 
// script.js
// script.js
function likeButton(heartImage) {
    // Get the card ID from the data attribute
    var cardId = heartImage.getAttribute('data-card-id');

    // Check if the heart is already liked (red)
    var isLiked = heartImage.classList.contains('liked');

    // Toggle the liked class and update the like count
    if (isLiked) {
        heartImage.src = 'images/heart-line.png'; // Set the heart image to the unliked state
        heartImage.classList.remove('liked');
        updateLikeCount(cardId, -1); // Subtract 1 from the like count
    } else {
        heartImage.src = 'images/heart-fill.png'; // Set the heart image to the liked state (red)
        heartImage.classList.add('liked');
        updateLikeCount(cardId, 1); // Add 1 to the like count
    }
}

function updateLikeCount(cardId, change) {
    // Get the current like count element within the specified card
    var likeCountElement = document.querySelector('.card[data-card-id="' + cardId + '"] .likes');

    // Extract the current like count value
    var currentLikes = parseInt(likeCountElement.textContent.replace(',', ''));

    // Update the like count
    var newLikes = currentLikes + change;
    likeCountElement.textContent = formatNumberWithCommas(newLikes);
}

function formatNumberWithCommas(number) {
    return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}

function logout() {
    // logic
    window.location.href = 'login.html';
}


// register js 
function switchForm(formId) {
    document.getElementById('loginForm').style.display = formId === 'loginForm' ? 'block' : 'none';
    document.getElementById('signForm').style.display = formId === 'signForm' ? 'block' : 'none';
}

function loginUser() {
  //logic
  alert('Login button clicked');
  return false;
}

function signupUser() {
    // logic
    alert('Registration logic will go here.');
    return false;
}