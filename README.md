
### Nearby places viewer
* Step 1: Set up Python and Flask development environment
* Step 2: Create a simple Flask application
* Step 3: Obtain coordinates of your current location
* Step 4: Send location data to the server with AJAX
* Step 5: Fetch nearby places via MediaWiki Action API
* Step 6: Create a user interface for list of places from JSON response
* Step 7: Style changes with Bootstrap

reference: https://www.mediawiki.org/wiki/API:Nearby_places_viewer


#### debugging
Problem: change in `places.js` file not reflect in `html`.\
Solution: force the browser to do a "hard refresh", which is going to be a browser/OS dependent keystroke, but generally this works:

Windows: Ctrl+F5\
Mac: Cmd+Shift+R\
Linux: Ctrl+Shift+R