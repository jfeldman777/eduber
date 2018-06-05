<div id="map">

</div>
<script>
var iconGreen = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'
var iconRed = 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'
function shift(pos, dlat, dlng){
    var pos2 = {
      lat: pos.lat + dlat,
      lng: pos.lng + dlng
    }
    return pos2;
}

function makeMarker(txt,pos,dlat,dlng,map,icon){
  var m = new google.maps.Marker(
      {
        position: shift(pos,dlat,dlng),
        map: map,
        title: txt,
        icon: icon
      });
      return m;
}

var txt1 = "Маша, 12 лет, играет на скрипке";
var txt2 = "Вася, 13 лет, играет на скрипке";
var txt3 = "Костя, 11 лет, альт";
var txt4 = "Михаил, 14 лет, контрабас";
var txt5 = "Иван Андреевич Крылов, музыкальный педагог со стажем";

var position =  {
            lat:59.93863, lng:30.31413-0.05
          };

function initMap(){
    var element = document.getElementById('map');
    var options = {
        zoom:12,
        center: position
    };

    var map = new google.maps.Map(element,options);

    var marker1 = makeMarker(txt1,position,0,-0.01,map,iconRed);
    var marker2 = makeMarker(txt2,position,0.01,-0.01,map,iconRed);
    var marker3 = makeMarker(txt3,position,0.001,0.01,map,iconRed);
    var marker4 = makeMarker(txt4,position,0,-0.02,map,iconRed);
    var marker11 = makeMarker('площадка 1',position,0.015,-0.008,map,iconGreen);
    var marker22 = makeMarker('площадка 2',position,-0.01,-0.012,map,iconGreen);
    var marker33 = makeMarker('площадка 3',position,-0.001,0.005,map,iconGreen);
}
</script>
<script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAjST-98VH5P3tlhqSDwRgCwNnaCxH0f8o&callback=initMap">
  </script>


</script>
