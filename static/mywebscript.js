function RunSentimentAnalysis() {
    var textToAnalyze = document.getElementById("textToAnalyze").value;

    fetch(`/emotionDetector?textToAnalyze=${encodeURIComponent(textToAnalyze)}`)
        .then(response => {
            // Se la risposta non è ok, leggila come testo per visualizzare il messaggio di errore
            if (!response.ok) {
                return response.text().then(errorMessage => {
                    document.getElementById("system_response").innerText = errorMessage;
                    throw new Error("Error: " + response.status);
                });
            }
            return response.text();
        })
        .then(data => {
            // Se la risposta è OK, mostra il risultato
            document.getElementById("system_response").innerText = data;
        })
        .catch(error => {
            console.error("Error:", error);
        });
}
