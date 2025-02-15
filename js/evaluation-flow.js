let testQuestions = [];                 // where all input question/answers are put
let isTestLoaded = false;               // flag for input file load errors
let firstTimeFlag = true;               // first entering getQuestionReady
let questionAnswerPicked = [];          // random question picked 
let currentQuestion;                    // used to store the current question
let expectedAnswer;                     // used to store the current answer 
let numberOfChances = 15;               // the most questions used in an evaluation
let questionsAlreadyAsked = [];         // store questions already asked (so we don't ask again)
let questionsAsked = 0;                 // number of questions asked
let timeLeft = 0;                       // don't want to destroy expectedSeconds, used for de-incrementation
let expectedSeconds = 15;               // amount of time user has to press the answer button, a stressor to help create stress (so user learns to answer questions under pressure)
let countdown = 0;                      // used to set timer, after question is read, user only has 15 seconds to start answer question
let userAnswer = '';                    // answer recorded using Speech Recognition
let allAnswers = [];                    // collecting all users answers temporarily
let answersCorrect = 0;                 // number of answers user got correct
let userScore = 0;                      // calculate score, displayed on screen
let maxQuestions = 15;                  // max questions that can be asked during a single evaluation
let expectedCorrect = 10;               // number of questions required for user to continue
let thresholdScore = 80;                // lowest possible score user can have to move on
let perfectScore = 100;                 // used to check if user has perfect score
let manager;                            // Declare a global variable for the NLP manager   
let voices = [];                        // Declare voices globally so you can reuse them

// Event listener to update the voices list once they are loaded
window.speechSynthesis.onvoiceschanged = function() {
    voices = speechSynthesis.getVoices();
    console.log("Available voices:", voices); // Log available voices for debugging
}

// Elements
const questionContainer = document.getElementById('question-container');
const answerContainer = document.getElementById('answer-container');
//const scoreContainer = document.getElementById('score-container');
const timerDisplay = document.getElementById('timer');
const statusContainer = document.getElementById('status');
const startButton = document.getElementById('start-button');
const nextButton = document.getElementById('next-button');
const answerButton = document.getElementById('answer-button');
const answersList = document.getElementById ('answers-list');
const progressBar = document.getElementById ('progress')
const titleGiven = document.getElementById ('title-given')

// Get the URL parameters
const urlParams = new URLSearchParams(window.location.search);
const fileName = urlParams.get('file'); // Get the file name from the URL
const titleToGive = urlParams.get('title'); 

console.log("urlParams: ", urlParams);
console.log("fileName: ", fileName);
console.log("titleToGive: ", titleToGive);

// If title is provided, set it to the <h1> element
if (titleToGive) {
    document.getElementById('title-given').textContent = titleToGive;
}


// Start Button Event Listener
document.getElementById('start-button').addEventListener('click', function() {
    takeExam();  
    this.disabled = true;  
});

// This is added to initialize the event listener when the page is loaded or when the test starts.
nextButton.addEventListener('click', function() {
    nextButton.disabled = true;  // Disable the next button so it can't be pressed again until the next question
    answerButton.disabled = true;  // Enable the answer button
    getQuestionReady(testQuestions);  // Load the next question
});

async function takeExam() {
    console.log("takeExam()");

    // Get the URL parameters
    //const urlParams = new URLSearchParams(window.location.search);
    //const fileName = urlParams.get('file'); // Get the file name from the URL
    
    //console.log("urlParams: ", urlParams);
    //console.log("fileName: ", fileName);

    if (fileName){
        // Now you have the file name, you can load the JSON file
        try {
            const response = await fetch(`resources/json/${fileName}`);
            const data = await response.json();
            
            testQuestions = data;
            console.log('Questions loaded:', testQuestions);

            getQuestionReady(testQuestions);
        } catch (error) {
            console.error("Error loading questions:", error);
        }
    } else {
        console.error("File name given is either invalid or is incorrectly named.");
    }
}

function getQuestionReady(testQuestions) {
    console.log("getQuestionReady()");
    
    // Are we here for the first time?
    if (firstTimeFlag) {
        firstTimeFlag = false;
        console.log("This is the first time.")
        getRandomQuestion(testQuestions);                
        readTextAloud(currentQuestion); // Read question aloud
        questionsAsked++;
        console.log("questionsAsked++:", questionsAsked)
    } else { // not first time
        let questionFound = false;
        
        // Keep trying to get a new random question that hasn't been asked
        while (!questionFound) {
            getRandomQuestion(testQuestions);  // Pick a random question
        
            if (!questionsAlreadyAsked.includes(currentQuestion)) {
                console.log("This is a new question.");
                // Read question aloud
                readTextAloud(currentQuestion); // Read question aloud

                // Add current question to questionsAlreadyAsked
                questionsAlreadyAsked.push(currentQuestion);
                questionFound = true;
                questionsAsked++;
                console.log("questionsAsked++:", questionsAsked)
            } else {
                // currentQuestion is already in questionsAlreadyAsked
                console.log("This question has already been asked.");
            }
        }
    }
        // Check if there are more questions left
        if (questionsAsked >= testQuestions.length) {
            console.log("All questions have been asked.");
            return; // Stop if all questions have been asked
        }
} // end getQuestionReady

function getRandomQuestion(testQuestions) {
    console.log("getRandomQuestion()");
    // Pick random question and store in questionAnswerPicked
    const randomIndex = Math.floor(Math.random() * testQuestions.length);
    const randomQuestion = testQuestions[randomIndex];
    questionAnswerPicked = [randomQuestion.question, randomQuestion.answer];
    currentQuestion = randomQuestion.question;
    expectedAnswer = randomQuestion.answer;

    // Display the question and answer
    questionContainer.innerText = randomQuestion.question;
    answerContainer.innerText = randomQuestion.answer; // TODO: Comment out when done testing
} // end getRandomQuestion

function readTextAloud(text) {
    console.log("readTextAloud()");
    //voices = speechSynthesis.getVoices();
    const voiceSelected = voices.find(voice => voice.name === "Microsoft Zira - English (United States)"); //|| voices[2];

    if (voiceSelected) {
        console.log("Selected voice:", voiceSelected.name); // Log the selected voice
    } else {
        console.log("No suitable voice found.");
    }

    const utterance = new SpeechSynthesisUtterance(text);

    // Explicitly set the selected voice for the utterance
    utterance.voice = voiceSelected; // This should come after creating the utterance
    
    // Event listener for when speech has finished
    utterance.onend = function() {
        getTimerReady();
    };
    window.speechSynthesis.speak(utterance);
} // end readQuestionAloud

function getTimerReady() {
    console.log("getTimerReady()");
    timeLeft = expectedSeconds;
        document.getElementById('timer').innerText = timeLeft;  // Display initial time
        startTimer(timeLeft);

        // NOTE: getQuestionReady(testQuestions); you call nextQuestion() which calls getQuestionReady => getRandomQuestion => readTextAloud => getTimerReady 
        // so all you have to do is startTimer()
        
} // end getTimerReady

function startTimer(timeLeft){
    console.log("startTimer()");
    // start timer countdown
    countdown = setInterval(function() {
        if (timeLeft >= 1) {
            timeLeft--;
            document.getElementById('timer').innerText = timeLeft;
            answerButton.disabled = false; // Enable the answer button
            // listen for user to press Answer button, then change speech to string
            startListening();
        } else {
            console.log("Time has ran down and we need user to press 'Next Question'.");
            statusContainer.innerText = "Time's up! Press 'Next Question' to continue.";
            clearInterval(countdown); // Stop the interval once time runs out
            nextQuestion(); // handle nextButton pressed
        } 
    }, 1000);   
}      

function startListening(){
    console.log("startListening()");
    //When user presses Answer button, we disable the answer button, stop timer, start listening for answer
    answerButton.addEventListener('click', () => {
        answerButton.disabled = true;
        clearInterval(countdown); //restart the countdown

        // Speech Recognition Setup
        const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        recognition.lang = 'en-US';
        recognition.interimResults = false;
        recognition.maxAlternatives = 1;


        // if recognition is running, stop it (before starting a new one)
        if (recognition.recognizing) {
            console.log("turning off Speech Recognition")
            recognition.stop(); // Stop recognition if it's currently running
        } 
        
        recognition.start(); //Speech Recognition
        

        recognition.onresult = function(event) {
            userAnswer = event.results[0][0].transcript;
            
            // has question been answered verbally?
            if (userAnswer.length > 0) {
                stageAnswer(userAnswer, expectedAnswer);  // Evaluate the answer when it's received
                recognition.stop();  // Stop listening after receiving the answer
            } 
        };

        recognition.onerror = function(event) {
            console.error('Speech Recognition Error:', event.error);
        };
    });
}

// handle nextButton
function nextQuestion() {
    console.log("nextQuestion()");
    
    // Enable the next button after a timer runs out or after answering a question
    nextButton.disabled = false;  // Allow the user to click 'Next Question'
    statusContainer.innerText = "Press 'Next Question' to continue.";  // Show status message
    
    // ATTENTION: Are you enabling answerButton anywhere when you get the question?
    // Disable the answer button until the next question is triggered
    answerButton.disabled = true;  // Can't answer until next question is ready
}

function stageAnswer(userResponse, expectedAnswer){
    console.log("stageAnswer()");
    console.log("Questions Asked: ", questionsAsked);
    console.log("userScore: ", userScore);
    console.log("Perfect Score: ", perfectScore);
    console.log("expectedCorrect:", expectedCorrect);
    

    // Convert both to lowercase for case-insensitive comparison
    userResponse = normalizeText(userResponse);
    expectedAnswer = normalizeText(expectedAnswer);
    
    // save the answer off into allAnswers (tuple)
    allAnswers.push(userResponse);
    console.log("All Answers so far: ", allAnswers);
    
    // display users answer on the screen
    //answersList.innerText = "This was your answer: " + allAnswers + ".";

    // check answer
    evaluateAnswer(userResponse, expectedAnswer);
}

function normalizeText(text) {
    return text
        .trim()                       // Remove leading/trailing whitespace
        .toLowerCase()                // Convert to lowercase
        .replace(/[^\w\s]/g, '');      // Remove punctuation
}

function evaluateAnswer(userResponse, expectedAnswer) {
    console.log("evaluateAnswer()");
    
    // Is user's answer correct? (returns Boolean value)
    if (checkAnswer(userResponse, expectedAnswer)) {
        answersCorrect++;  // Increment the number of correct answers
        updateProgress();

        console.log("questionsAsked:", questionsAsked);
        console.log("answersCorrect: ", answersCorrect);
        console.log("expectedCorrect: ", expectedCorrect);
        console.log("userScore: ", userScore);
        console.log("thresholdScore: ", thresholdScore);

        // DOES THE USER HAVE 10 QUESTIONS RIGHT?
        if (answersCorrect === expectedCorrect) {
            // YES - PASS, MOVE ON
            console.log("TEST: the student has answered enough questions to move to next exam.");
            triggerConfetti();
            statusContainer.innerText = "You Passed! Going to next exam. See you there!";
            // TODO: THE NEXT EXAM WILL EVENTUALLY COME UP
        } else { // not enough answered correctly
            // NO - HAS THE PERSON BEEN ASKED 15 QUESTIONS?
            if (questionsAsked === maxQuestions ) {
                // YES - FAIL, MUST TAKE LESSON
                console.log("TEST: the student has been asked the max number of questions.")
                statusContainer.innerText = "You must complete "+ titleToGive + "lesson. See you there!";
                // TODO: THE LESSON WILL EVENTUALLY COME UP

            }else{ // 15 questions haven't been asked
                // NO - GO TO THE NEXT QUESTION AFTER DISPLAYING SCORE AND BAR AND MESSAGE CORRECTLY    
                // Note: answersCorrect is NOT incremented so there is no reason to ask whether the 
                //       student has met the expected 10 correct answers
                console.log("TEST: the student must continue answering questions; they haven't attempted 15 questions.");
                updateProgress(); // do display the users new score and progress bar
                nextQuestion();  // Proceed to the next question
            }
        }
    } else { // THE QUESTION WASN'T ANSWERED CORRECTLY
        // NO - HAS THE PERSON BEEN ASKED 15 QUESTIONS?
        if (questionsAsked === maxQuestions ) {
            // YES - FAIL, MUST TAKE LESSON
            console.log("TEST: the student has been asked the max number of questions.")
            statusContainer.innerText = "You must complete "+ titleToGive + "lesson. See you there!";
            // TODO: THE LESSON WILL EVENTUALLY COME UP

        }else{ // 15 questions haven't been asked
            // NO - GO TO THE NEXT QUESTION AFTER DISPLAYING SCORE AND BAR AND MESSAGE CORRECTLY    
            // Note: answersCorrect is NOT incremented so there is no reason to ask whether the 
            //       student has met the expected 10 correct answers
            console.log("TEST: the student must continue answering questions; they haven't attempted 15 questions.");
            updateProgress(); // do display the users new score and progress bar
            nextQuestion();  // Proceed to the next question
        }
    }
}

// Compare user answer with correct answer using NLP
function checkAnswer(userResponse, expectedAnswer) {
    if (userResponse === expectedAnswer){
        return 1;
    }else{
        console.log("checkAnswer()");
        console.table({ userResponse, expectedAnswer });

        // Is the answer correct?
        const userDoc = nlp(userResponse);  // Process user answer using compromise
        const correctDoc = nlp(expectedAnswer);  // Process correct answer using compromise
        
        const userTokens = userDoc.nouns().out('array').concat(userDoc.verbs().out('array'));
        console.log("NLP resulting userTokens: ", userTokens);
        const correctTokens = correctDoc.nouns().out('array').concat(correctDoc.verbs().out('array'));
        console.log("NLP resulting correctTokens: ", correctTokens);
        const commonTokens = userTokens.filter(token => correctTokens.includes(token));
        console.log("NLP resulting commonTokens: ", commonTokens);
        const matchRatio = commonTokens.length / correctTokens.length;
        console.log("NLP resulting Ratio: ", matchRatio);

    // returns Boolean value 1 if matchRatio is greater or equal to 30%
    return matchRatio >= 0.30;  
    }
    
}

function updateProgress() {
    //compute and display user's score
    userScore = (answersCorrect * 100) / questionsAsked;
    document.getElementById('score-container').innerText = `Correct: ${answersCorrect}/${questionsAsked}`;
    
    // update progress bar
    console.log("updateProgress()");
    const progress = (answersCorrect / numberOfChances) * 100;
    document.getElementById('progress').style.width = `${progress}%`;
}

function triggerConfetti() {
    console.log("triggerConfetti()");

    clearInterval(countdown);  // Stop the timer when the answer button is clicked

    // set duration of animation
    var duration = .2 * 1000;
    var end = Date.now() + duration;

    // set confetti frame
    (function frame() {
    confetti({
        particleCount: 7,
        angle: 60,
        spread: 300,
        origin: { x: .1 }
    });
    confetti({
        particleCount: 7,
        angle: 60,
        spread: 300,
        origin: { x: .2 }
    });
    confetti({
        particleCount: 7,
        angle: 60,
        spread: 300,
        origin: { x: .3 }
    });
    confetti({
        particleCount: 7,
        angle: 60,
        spread: 300,
        origin: { x: .4 }
    });
    confetti({
        particleCount: 7,
        angle: 60,
        spread: 300,
        origin: { x: .5 }
    });
    confetti({
        particleCount: 7,
        angle: 60,
        spread: 300,
        origin: { x: .6}
    });
    confetti({
        particleCount: 7,
        angle: 60,
        spread: 300,
        origin: { x: .7 }
    });
    confetti({
        particleCount: 7,
        angle: 60,
        spread: 300,
        origin: { x: .8 }
    });
    confetti({
        particleCount: 7,
        angle: 60,
        spread: 300,
        origin: { x: .9 }
    });

    // keep going until we are out of time
    if (Date.now() < end) {
        requestAnimationFrame(frame);
    }
    }());
}