// script.js
let avatar = document.getElementById('avatar');
let currentLesson = 0; // Track the current lesson completed

// Function to move the avatar along the path
function moveAvatar(lessonNumber) {
    const lessonPositions = {
        1: '10%', // Lesson 1
        2: '40%', // Lesson 2
        3: '70%', // Lesson 3
        4: '90%'  // Lesson 4
    };

    avatar.style.left = lessonPositions[lessonNumber];
}

// Function to mark lesson as completed
function completeLesson(lessonNumber) {
    if (lessonNumber === currentLesson + 1) {
        currentLesson = lessonNumber;
        moveAvatar(lessonNumber);
        alert('Well done! You completed Lesson ' + lessonNumber);
    } else {
        alert('Please complete the previous lessons first.');
    }
}
