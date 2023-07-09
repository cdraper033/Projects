var formdata = new FormData();

const API_KEY = '';

function inputData(event) {
  const zipCode = event.target.value;
  const url = `http://dataservice.accuweather.com/locations/v1/postalcodes/search?apikey=${API_KEY}&q=${zipCode}`;
  fetch(url)
    .then(response => response.json())
    .then(result => {
      var x = result[0].ParentCity.Key
      const otherurl = `http://dataservice.accuweather.com/currentconditions/v1/${x}?apikey=${API_KEY}`

      fetch(otherurl)
        .then(res => res.json())
        .then(reslt => {

          if (reslt[0].WeatherText.includes('cloudy')) {
            var myHTML = `
<div id="container">
<p class="location"> Here is today's forecast for </p>
<p class="location"> ${result[0].ParentCity.EnglishName}, ${result[0].AdministrativeArea.LocalizedName}</p>
<hr>
<p class="weatherType"> ${reslt[0].WeatherText} </p>
<p class="temperature"> ${reslt[0].Temperature.Imperial.Value}°F </p>
</div>
`
            document.body.innerHTML = myHTML
          }
          else {
            console.log("error")
          }
        })
    })

    .catch(error => console.log('error', error));
}

const input = document.getElementById("input");

input.addEventListener("change", inputData);







