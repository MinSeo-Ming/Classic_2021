$.getJSON('https://api.openweathermap.org/data/2.5/weather?id=1835848&appid=23b58efaade154fc157883de54595599&units=metric', 
function(data){
    //data로 할 일
    var $minTemp = data.main.temp_min;
    var $maxTemp = data.main.temp_max;
    var $current_temp = data.main.temp;
    var $time = new Date($.now());
    var $current_date = $time.getFullYear() + '년' + ($time.getMonth() + 1) + '월' + $time.getDate() + '일'
        // +$time.getHours() + ':' + $time.getMinutes()
    var $current_humidity = data.main.humidity;
    var $weather_icon = data.weather[0].icon;
   
    // alert($time.getFullYear() +'/'+ $time.getMonth() +'/'+$time.getDate() +'/'+$time.getHours() +':' + $time.getMinutes() );

    $('.lowtemp').append($minTemp);         //lowtemp뒤에 minTemp추가(openweathermap api)
    $('.hightemp').append($maxTemp);
    $('.current_temp').append($current_temp);
    $(' h1').prepend($current_date);
                                            //h2앞에 current_date 추가
    $('.icon').append('<img src="http://openweathermap.org/img/wn/' + $weather_icon + '.png">');
    $('.current_humidity').append($current_humidity) 
});