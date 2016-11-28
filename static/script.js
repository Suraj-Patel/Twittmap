var geocoder;
var map;
function initMap(locs) {
    geocoder = new google.maps.Geocoder();

    var loc = {lat: 23, lng: 0};
    var myOptions = {
      zoom: 2,
      center: loc
    };
    map = new google.maps.Map(document.getElementById('map'), myOptions);
    map.setOptions({ minZoom: 2, maxZoom: 10 });

    codeLocation(locs);
    //var marker = new google.maps.Marker({
    //  position: loc,
    //  map: map
    //});
}

function codeLocation(locs) {
        var markers = []

        for (var i in locs)
        {
            markers.push(i)
        }

        var icons = {
          positive: {
            icon: '/static/icons/green.png'
          },
          negative: {
            icon: '/static/icons/red.png'
          },
          neutral: {
            icon: '/static/icons/black.png'
          }
        };
        if(markers.length > 0)
        {
            for (i=0; i<markers.length; i++)
            {
                address = JSON.parse("[" + markers[i] + "]");
                console.log(address)
                console.log(icons[locs[markers[i]]].icon)
                //var iconfile = icons[locs[address]].icon
                //geocoder.geocode( { 'address': address}, function(results, status) {
                //  if (status == google.maps.GeocoderStatus.OK) {
                    //map.setCenter(results[0].geometry.location);
                var marker = new google.maps.Marker({
                    map: map,
                    icon: icons[locs[markers[i]]].icon,
                    animation: google.maps.Animation.DROP,
                    position: new google.maps.LatLng(address[0][0], address[0][1])
                });
            }
        }
    }