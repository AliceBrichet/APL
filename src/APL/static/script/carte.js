console.log("carte.js chargé");

var map = L.map('map').setView([46.8534, 2.3488], 6);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
}).addTo(map);
