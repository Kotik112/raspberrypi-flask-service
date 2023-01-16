function turnOn(room) {
  fetch(`/on/${room}`, { method: 'POST' });
}
function turnOff(room) {
  fetch(`/off/${room}`, { method: 'POST' });
}
function setBrightness(room, level) {
  fetch(`/brightness/${room}/${level}`, { method: 'POST' });
}
function setColor(room, hex) {
  if (hex[0] === '#') {
    hex = hex.slice(1);
  }
  let color = tinycolor(hex);
  let r = color.toRgb().r;
  let g = color.toRgb().g;
  let b = color.toRgb().b;

  // send a post request to the server with the room, r, g, b values
  fetch(`/color/${room}/${r}/${g}/${b}`, { method: 'POST' });
}
