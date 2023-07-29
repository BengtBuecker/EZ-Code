document.getElementById("searchInput").addEventListener("input", function () {
  let input = this.value.toLowerCase();
  let commands = document.querySelectorAll("#commandList li");

  for (let i = 0; i < commands.length; i++) {
    let commandText = commands[i].innerText.toLowerCase();
    if (commandText.indexOf(input) > -1) {
      commands[i].style.display = "list-item";
    } else {
      commands[i].style.display = "none";
    }
  }
});
