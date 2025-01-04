let instructions = document.querySelectorAll('#instructions-list li'); // Select all instructions
let voices = [];
let currentInstruction = 0;

// Function to load voices and ensure they are available
function loadVoices() {
    voices = speechSynthesis.getVoices();
    console.log("Available voices:", voices); // Log available voices in console

    // Select a specific voice (you can change this if you want another voice)
    const voiceSelected = voices.find(voice => voice.name === "Microsoft Zira - English(United States)") || voices[4];

    if (voiceSelected) {
        console.log("Selected voice:", voiceSelected.name); // Log the selected voice
    } else {
        console.log("No suitable voice found.");
    }

    // Proceed to read instructions only after voices are loaded
    if (voices.length > 0) {
        // Ensure reading starts after button press
        startReadingInstructions(voiceSelected);
    } else {
        // Retry loading voices if the voices array is empty
        setTimeout(loadVoices, 1000);
    }
}

// Function to read the instructions aloud with the selected voice
function readInstructions(voiceSelected) {
    if (currentInstruction < instructions.length) {
        // Get the current instruction text
        const instructionText = instructions[currentInstruction].innerText;

        // Highlight the current instruction
        instructions[currentInstruction].classList.add('highlight');  // Add highlight class

        // Create a SpeechSynthesisUtterance to convert text to speech
        const speech = new SpeechSynthesisUtterance(instructionText);
        speech.lang = 'en-US'; // Set language to English (US)

        // Set the selected voice
        speech.voice = voiceSelected;

        // When the speech ends, move to the next instruction
        speech.onend = function() {
            // Remove the highlight from the current instruction
            instructions[currentInstruction].classList.remove('highlight');

            // Move to the next instruction
            currentInstruction++; 

            // Recursively read the next instruction
            readInstructions(voiceSelected); 
        };

        // Start speaking the current instruction
        window.speechSynthesis.speak(speech);
    }
}

// Trigger speech synthesis only after a user interaction (e.g., when the "Read Instructions" button is clicked)
function startReadingInstructions(voiceSelected) {
    // Reset the currentInstruction so the reading starts from the first instruction
    currentInstruction = 0;

    // Proceed to read instructions only if voices are available
    if (voiceSelected) {
        readInstructions(voiceSelected);
    }
}

// Add an event listener to the "Read Instructions" button to begin the instructions
document.querySelector('#read-instructions-button').addEventListener('click', function() {
    console.log("Button clicked!"); // Debugging: Confirm button click
    // Ensure voices are loaded before starting to read instructions
    if (speechSynthesis.getVoices().length > 0) {
        loadVoices(); // Proceed to read instructions after voices are available
    } else {
        // Retry after 1 second if voices aren't available
        setTimeout(loadVoices, 1000);
    }
});

// We don't want speech synthesis to run as soon as the page loads
// So, we ensure no reading is triggered on page load
window.speechSynthesis.onvoiceschanged = function() {
    // Ensure that voices are loaded but don't start reading immediately
    loadVoices();
};

function StartEvaluation() {
    // Fetch the JSON data from the file
    fetch('/javascript/datatypedata.json')  // Ensure the file path is correct
        .then(response => response.json())
        .then(data => {
            // Randomly pick a question from the data
            const randomIndex = Math.floor(Math.random() * data.length);
            const questionData = data[randomIndex];

            // Display the question in the question container
            document.getElementById('categoryTitle').textContent = `Category: ${questionData.category}`;
            document.getElementById('questionText').textContent = questionData.question;
            //document.getElementById('answerText').textContent = `Answer: ${questionData.answer}`;

            // Show the question container
            document.getElementById('questionContainer').style.display = 'block';

            // Enable the speak button
            document.getElementById('speakButton').addEventListener('click', startSpeechRecognition);
        })
        .catch(error => console.error('Error fetching the data:', error));
}