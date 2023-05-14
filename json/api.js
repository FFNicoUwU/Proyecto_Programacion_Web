function showPosition(position) {
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;
  
    fetch(`http://api.weatherapi.com/v1/current.json?key=f341cb72910244aa827131715230905&q=${lat},${lon}`)
      .then(response => response.json())
      .then(data => {
        const weatherInfo = document.getElementById("weather-info");
        weatherInfo.innerHTML = `La temperatura en ${data.location.name} es de: ${data.current.temp_c} Grados Celcius.`;
      })
      .catch(error => console.error(error))
  }
  
  function getLocation() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(showPosition);
    } else {
      console.error("Geolocation is not supported by this browser.");
    }
  }
  
  getLocation();
  