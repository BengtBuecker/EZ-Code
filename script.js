

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

    return response;
}

