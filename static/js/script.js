const startListeningButton = document.getElementById('start-listening');
const responseElement = document.getElementById('response');

// Initialize speech recognition
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();

recognition.onstart = () => {
    console.log('Voice recognition started. Speak now.');
};

recognition.onspeechend = () => {
    console.log('Speech recognition ended.');
    recognition.stop();
};

recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript.toLowerCase();
    console.log('You said: ' + transcript);

    axios.post('/command', { command: transcript })
        .then(response => {
            const data = response.data;
            if (data.response.startsWith('https://')) {
                window.open(data.response, '_blank');
            } else {
                responseElement.textContent = data.response;
            }
        })
        .catch(error => {
            console.error('There was an error!', error);
        });
};

startListeningButton.addEventListener('click', () => {
    recognition.start();
});
