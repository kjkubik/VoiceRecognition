# Teach Them To Fish

Deploy at https://kjkubik.github.io/VoiceRecognition


![alt text](/images/image.png)


## Vision Statement: 

As engineers, we often times internalize the things we learn, rarely sharing the thought processes behind the solutions we create. We receive business requirements, produce a solution and deliver them. No one (except for our trusty team members) ever cares to know how we came up with the solution. The end-users are grateful; we just made their lives a wee-bit easier.

While this may work in the short term, I believe that, as solution-driven individuals, we need to be able to articulate our thinking more effectively. We face a recurring challenge: verbalizing complex technical concepts. Whether in meetings or interviews, we often find ourselves unable to express our ideas clearly when the 'spotlight' is on us, such as during an interview. This is a gap we must address, not only to improve communication but to demonstrate our expertise with clarity and confidence.

My vision is simple: Prioritize verbal communication.

When we collaborate, we must prioritize clear and specific verbal communication. This will enable us to arrive at solutions faster and work more efficiently. During interviews, we should be able to express our ideas with confidence, conciseness, and precision, showcasing our technical mastery and expertise with the tools and languages we use.

To address this, I envision a system where we can practice articulating our thoughts under pressure. This tool will present randomly selected questions and answers from a set of categories, display them on screen, and read them aloud. A timer will start once the question is read, allowing us 15 seconds to formulate a response. After we provide our verbal answer, the system will use speech-to-text technology to transcribe our response and then evaluate the answer using machine learning.

This process will help us build confidence in verbalizing technical concepts, ensuring we can communicate effectively in any setting.

Here is the current web pages I have created: 

# Initial Page 
![alt text](/images/image-1.png)

# Class Choices
![alt text](/images/image-2.png)

# Initial Evaluation
During the initial evaluation SpeechRecognition is used to change questions from text to audio. Once the question is read, a timer is set to 15 seconds. The user is prompted to press the answer button. Once the user presses the Answer button and answers the question verbally, their answer is evaluated as correct or incorrect.

![alt text](/images/image-3.png)

This continues until the user has answered 10 questions correctly. Then, animated confetti covers the page to celebrate their win and they are directed to the next evaluation. If they are unable to answer ten questions, they are sent into a lesson to practice the skill they were evaluated over.
![alt text](/images/image-4.png)