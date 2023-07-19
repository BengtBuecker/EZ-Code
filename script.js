function explainCode() {
    var code = document.getElementById("codeInput").value;
    var lines = code.split("\n");
    var output = document.getElementById("output");
    output.innerHTML = "";

    for (var i = 0; i < lines.length; i++) {
        var line = lines[i].trim();

        if (line !== "") {
            var explanation = getExplanation(line);
            output.innerHTML += "<p><b>Zeile " + (i + 1) + ":</b> " + explanation + "</p>";
        }
    }
}

function getExplanation(code) {
    // Verwende die Chat-GPT API oder eine andere API deiner Wahl, um den Code zu erklären
    // Führe den API-Aufruf durch und gib die erklärende Antwort zurück

    // Beispiel:
    var response = "Dies ist eine Erklärung für den gegebenen Code.";

    return response;
}
