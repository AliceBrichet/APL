var map = L.map('map').setView([43.6053809, 2.2411289], 9);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
}).addTo(map);

$.getJSON("/static/geojson/communes.geojson", function(data) {
    L.geoJSON(data, {
        style: function (feature) {
            return {
                fillColor: '#FFEDA0', // Couleur de remplissage
                weight: 2, // Largeur de la bordure
                opacity: 1,
                color: 'white', // Couleur de la bordure
                dashArray: '3',
                fillOpacity: 0.7
            };
        },
        onEachFeature: function (feature, layer) {
            layer.bindPopup(feature.properties.name);
        }
    }).addTo(map);
});