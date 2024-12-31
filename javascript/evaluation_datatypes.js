let voices = [];

// Function to load voices and ensure they are available
function loadVoices() {
    voices = speechSynthesis.getVoices();
    console.log("Available voices:", voices); // console will log voice choices
    const voiceSelected = voices.find(voice => voice.name === "Microsoft EmmaMultilingual Online (Natural) - English (United States)")// || voices[10]);

        // Read instructions once voices are loaded and a voice is selected
    readInstructions(voiceSelected);
}
        // // Fallback for browsers that may not trigger onvoiceschanged event immediately
        // if (voices.length === 0) {
        //     setTimeout(loadVoices, 1000); // Try again after 1 second
        // }

// Function to read the instructions aloud with the selected voice
function readInstructions(voiceSelected) {
    // Get the instructions text
    const instructionsText = document.getElementById('instructions-list').innerText;

    // Create a SpeechSynthesisUtterance object to convert text to speech
    const speech = new SpeechSynthesisUtterance(instructionsText);
    speech.lang = 'en-US'; // Set language to English (US)

    // Set the selected voice
    speech.voice = voiceSelected;

    // Speak the instructions
    window.speechSynthesis.speak(speech);
    }

// Function to trigger the start of the quiz
function Start() {
    // To start, a random question is 

}

// Trigger voice loading and reading on page load
window.onload = function() {
    if (speechSynthesis.getVoices().length > 0) {
        loadVoices();
    } else {
        setTimeout(loadVoices, 1000); // Wait for 1 second to try loading again
    }
};