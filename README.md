#README
___

This script returns weather conditions for the zip code you enter from the command line.

This uses Geopy to convert the Zip code to Latitude and Longitude coordinates then uses those coordinates to look up the weather conditions. Right now this only returns:

* `Current temp`
* `Current conditions`
* `Nearest storm`
* `Eight day (including current day) high and low temperatures`

You can easily add other data points from the documentation found here: https://developer.forecast.io/docs/v2/#data-points

You will need an api key from Forecast. You can get one here: https://developer.forecast.io/

You will need to put your api key in a file called api.txt in the same directory as the script. Do not add anything to the file other then your api key.

After adding the file simply run the script from the command line.