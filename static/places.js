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
        var data = {
            "latitude": position.coords.latitude,
            "longitude": position.coords.longitude
        };

        $.ajax({
            url: "/",
            type: "POST",
            data: JSON.stringify(data),
            contentType: "application/json",
            dataType: "json",

            success: function (response) {
                x.innerHTML = "Success!";
            },
            error: function () {
                x.innerHTML = "An error occured while fetching places!";
            }
        });
    }
});