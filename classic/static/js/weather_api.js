console.log(navigator)
console.log(navigator.appVersion)

function requestCoords() {
    navigator.geolocation.getCurrentPosition(success,fail);
    navigator.geolocation.getCurrentPosition
    navigator.geolocation.getweather
}

function success(position){                        //성공시 위도와 경도(위치) 정보 받음
    console.log("위도" + position.coords.latitude)
    console.log("경도" + position.coords.longitude)
    console.log(position);
    const latitude = position.coords.latitude;       // 경도
    const longitude = position.coords.longitude;     // 위도
}

function fail(err){     //실패함수
    console.log("fail! " + err);
}

(function(){
    navigator.geolocation.getCurrentPosition(success,fail)
})()

function getweather(lat, lon){
    fetch(`https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=23b58efaade154fc157883de54595599&units=metric`)
    .then(res => res.json())
    .then(data => {
        const temp = data.main.temp;
        const weathers = data.weather[data.weather.length-1];
        weatherSpan.innerHTML =  `${temp}&#176;C ${weathers.main}`;
    })
}
