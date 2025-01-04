let instructions = document.querySelectorAll('#instructions-list li'); // Select all instructions
let voices = [];
let currentInstruction = 0;

// Function to load voices and ensure they are available
function loadVoices() {
    voices = speechSynthesis.getVoices();
    console.log("Available voices:", voices); // Log available voices in console

    const voiceSelected = voices.find(voice => voice.name === "Microsoft Zira - English(United States)") || voices[4];

    if (voiceSelected) {
        console.log("Selected voice:", voiceSelected.name); // Log the selected voice
    } else {
        console.log("No suitable voice found.");
    }

    // Proceed to read instructions only after voices are loaded
    if (voices.length > 0) {
        // Ensure reading starts automatically once the page loads
        startReadingInstructions(voiceSelected);
    } else {
        // Retry loading voices if the voices array is empty
        setTimeout(loadVoices, 1000);
    }
}

// Function to read the instructions aloud with the selected voice
function startReadingInstructions(voiceSelected) {
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

            // Move to the next instruction after a small delay
            currentInstruction++; 

            if (currentInstruction < instructions.length) {
                // Delay the reading of the next instruction to ensure the previous one finishes
                setTimeout(function() {
                    startReadingInstructions(voiceSelected);
                }, 500); // Small delay before moving to the next instruction
            }
        };

        // Start speaking the current instruction
        window.speechSynthesis.speak(speech);
    }
}

// Trigger speech synthesis to start reading instructions automatically after the page loads
document.addEventListener('DOMContentLoaded', function() {
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
    loadVoices();
};


function StartEvaluation() {
    // Check if the necessary HTML elements exist
    const categoryTitleElement = document.getElementById('categoryTitle');
    const questionTextElement = document.getElementById('questionText');
    const questionContainer = document.getElementById('questionContainer');

    if (!categoryTitleElement || !questionTextElement || !questionContainer) {
        console.error('Missing HTML elements. Please ensure "categoryTitle", "questionText", and "questionContainer" are present in the HTML.');
        return;
    }

    fetch('javascript/datatypedata.json')
        .then(response => response.json())  // Parse the JSON data
        .then(data => {
            // Randomly pick a question from the data
            const randomIndex = Math.floor(Math.random() * data.length);
            const questionData = data[randomIndex];

            // Display the question and category
            categoryTitleElement.textContent = `Category: ${questionData.category}`;
            questionTextElement.textContent = questionData.question;

            // Show the question container
            questionContainer.style.display = 'block';

            // Optionally, you could show additional elements or initiate other actions here
        })
        .catch(error => console.error('Error fetching the data:', error));
}