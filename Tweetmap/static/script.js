var geocoder;
var map;
function initMap(locs) {
    geocoder = new google.maps.Geocoder();
    var markers = locs;

    if(markers.length > 0)
    {
        codeLocation(markers);
    }
    var loc = {lat: 23, lng: 0};
    var myOptions = {
      zoom: 2,
      center: loc
    };
    map = new google.maps.Map(document.getElementById('map'), myOptions);
    map.setOptions({ minZoom: 2, maxZoom: 10 });
    //var marker = new google.maps.Marker({
    //  position: loc,
    //  map: map
    //});
}

function codeLocation(markers) {
        for (i=0; i<markers.length; i++)
        {
            address = markers[i];
            geocoder.geocode( { 'address': address}, function(results, status) {
              if (status == google.maps.GeocoderStatus.OK) {
                //map.setCenter(results[0].geometry.location);
                var marker = new google.maps.Marker({
                    map: map,
                    position: results[0].geometry.location
                });
              } else {
                //alert('Geocode was not successful for the following reason: ' + status);
              }
            });
        }
    }