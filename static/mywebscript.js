
function RunSentimentAnalysis() {
    const textToAnalyze = document
        .getElementById("textToAnalyze").value.trim();

    const output = document.getElementById("system_response");

    if (!textToAnalyze) {
        output.textContent = "Please enter some text to analyze.";
        return;
    }

    fetch("/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze))
        .then(async response => {
            const message = await response.text();

            if (!response.ok) {
                throw new Error(message);
            }

            return message;
        })
        .then(message => {
            output.textContent = message;
        })
        .catch(error => {
            output.textContent = error.message;
        });
}
