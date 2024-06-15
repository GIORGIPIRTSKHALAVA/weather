document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('getWeather').addEventListener('click', function() {
        const city = document.getElementById('city').value;
        if (city === '') {
            alert('Please enter a city name');
            return;
        }

        const apiKey = 'a1f091c4f0238f190936f30d574ef4a6';  
        const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

        fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                console.log(data);  // Log the data for debugging
                const weatherDetails = `
                    <h2>${data.name}</h2>
                    <p>Temperature: ${data.main.temp}°C</p>
                    <p>Weather: ${data.weather[0].description}</p>
                    <p>Humidity: ${data.main.humidity}%</p>
                    <p>Wind Speed: ${data.wind.speed} m/s</p>
                `;

                const weatherIcon = document.getElementById('weatherIcon');
                const weatherDescription = data.weather[0].description.toLowerCase();

                // Update the weather icon based on the weather condition
                if (weatherDescription.includes('rain')) {
                    weatherIcon.src = 'imiges/rainy-icon.png';  // Path to your rainy icon image
                } else if (weatherDescription.includes('clear sky')) {
                    weatherIcon.src = 'imiges/sunny-icon.png';  
                } else if (weatherDescription.includes('cloud')) {
                    weatherIcon.src = 'imiges/cloudy-icon.png';  
                } else {
                    weatherIcon.src = 'imiges/default-icon.png';  
                }

                weatherIcon.style.display = 'block';
                document.getElementById('weatherDetails').innerHTML = weatherDetails;
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                alert('An error occurred while fetching the weather data.');
            });
    });
});
