// obtain coordinates of current location. use the Geolocation API.

$( document ).ready(function() {
	var x = document.getElementById( "places-list" );

	$( 'button' ).click(function() {
		getLocation();
	});

	// When Click the button, the app makes a call to the Geolocation API and retrieves
    // the current position of the device via the API's Navigator.geolocation object.
	function getLocation() {
		x.innerHTML = "Searching your location..";

		if (navigator.geolocation) {
			navigator.geolocation.getCurrentPosition(fetchPlaces);
		} else {
			x.innerHTML = "Geolocation is not supported by this browser.";
		}
	}

	function fetchPlaces(position) {
		x.innerHTML = position.coords.latitude + "|" + position.coords.longitude;
	}
});