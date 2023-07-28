var i = 0;
var txt = 'Programmieren war nie einfacher.';
var speed = 50;

function einleitung() {
  if (i < txt.length) {
    document.getElementById("einleitung").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}
