let center = [57.82018062115083,28.330161542328177];
let placemarks = [
	{
		latitude: 57.81157872602884,
		longitude: 28.33719590220985,
		draggable: true,
		balloonContent: [
			'<h2>This is balloon</h2>',
			'<img class="bd-placeholder-img" width="170" height="100" src="/static/images/15.jpg" alt="lhs"/>'
		]
	},
	{
		latitude: 57.82323733557179,
		longitude: 28.34872025313253,
		draggable: true,
		balloonContent: [
			'<h2>This is balloon</h2>',
			'<img class="bd-placeholder-img" width="170" height="100" src="/static/images/15.jpg" alt="lhs"/>'
		]
	},
	{
		latitude: 57.80480508696977,
		longitude: 28.333814508344734,
		draggable: true,
		balloonContent: [
			'<h2>This is balloon</h2>',
			'<img class="bd-placeholder-img" width="170" height="100" src="/static/images/15.jpg" alt="lhs"/>'
		]
	}
];

function init() {
	let myPlacemark,
		map = new ymaps.Map('map-test', {
			center: center,
			zoom: 13,
			controls: ['zoomControl', 'searchControl', 'typeSelector',  'fullscreenControl', 'routeButtonControl']
		},{
			searchControlProvider: 'yandex#search'
		});

    // Слушаем клик на карте.
    map.events.add('click', function (e) {
        let coords = e.get('coords');

        // Если метка уже создана – просто передвигаем ее.
        if (myPlacemark) {
            myPlacemark.geometry.setCoordinates(coords);
        }
        // Если нет – создаем.
        else {
            myPlacemark = createPlacemark(coords);
            map.geoObjects.add(myPlacemark);
            // Слушаем событие окончания перетаскивания на метке.
            myPlacemark.events.add('dragend', function () {
                getAddress(myPlacemark.geometry.getCoordinates());
            });
        }
        getAddress(coords);
    });

    // Создание метки.
    function createPlacemark(coords) {
        return new ymaps.Placemark(coords, {
            iconCaption: 'поиск...'
        }, {
            preset: 'islands#pinkDotIconWithCaption',
            draggable: true
        });
    }

    // Определяем адрес по координатам (обратное геокодирование).
    function getAddress(coords) {
        myPlacemark.properties.set('iconCaption', 'поиск...');
        ymaps.geocode(coords).then(function (res) {
            let firstGeoObject = res.geoObjects.get(0);

            myPlacemark.properties
                .set({
                    // Формируем строку с данными об объекте.
                    iconCaption: [
                        // Название населенного пункта или вышестоящее административно-территориальное образование.
                        firstGeoObject.getLocalities().length ? firstGeoObject.getLocalities() : firstGeoObject.getAdministrativeAreas(),
                        // Получаем путь до топонима, если метод вернул null, запрашиваем наименование здания.
                        firstGeoObject.getThoroughfare() || firstGeoObject.getPremise()
                    ].filter(Boolean).join(', '),
                    // В качестве контента балуна задаем строку с адресом объекта.
                    balloonContent: firstGeoObject.getAddressLine()
                });
        });
    }
	
	placemarks.forEach(function(obj) {
		let placemark = new ymaps.Placemark([obj.latitude, obj.longitude], {
			balloonContent: obj.balloonContent.join('')
		},
		{
			iconLayout: 'default#image',
			iconImageHref: '/static/images/11330376.png',
			iconImageSize: [55, 60],
			iconImageOffset: [-27, -49]
		});

		placemark.events.add('click', function (){
			alert('Wow!');
		});

		map.geoObjects.add(placemark);
	});
	
	//функционал добавления полигонов

$('#addEditPolyline').on('click', function(){
	polygon = new ymaps.GeoObject({
		geometry:{
			type: "Polygon",
			coordinates:[]
		},
	
			properties:{
				balloonContentHeader: 'Title',
				balloonContentBody:'Description',
				hintContent:'всплывающая подсказка для полигона',
			}
		},{
	editorDrawingCursor:"crosshair"});
	
		map.geoObjects.add(polygon);
	
		polygon.editor.startDrawing();
});
	
	//нажатие кнопки расчета координат
$('#stopEditPolyline').on('click', function(){
	$('#datacootd').empty();
map.geoObjects.each(function(obj, objIndex){
printGeometry(obj.geometry.getCoordinates()[0], objIndex);
});

});
	
	// map.controls.remove('geolocationControl'); // удаляем геолокацию
  	map.controls.remove('trafficControl'); // удаляем контроль трафика
  	map.controls.remove('typeSelector'); // удаляем тип
 	map.controls.remove('fullscreenControl'); // удаляем кнопку перехода в полноэкранный режим
  	map.controls.remove('rulerControl'); // удаляем контрол правил
	
}

//функция прорисовки координат
function printGeometry(coords, index){
	let addcoord='Полигон: <b>'+index+'</b>'+stringify(coords)+ '<br>';
	$('#datacoord').append(addcoord);

	function stringify(coords){
		let res = '';
		if ($.isArray(coords)){
			res = '[ '
			for (let i=0, l=coords.length; i<l; i++) {
			if (i>0){
				res += ', '; 
			}
			res += stringify(coords[i]);
		}
		res += ' ]';
		} else if (typeof coords=='number'){
			res = coords.toPrecision(6);
		}else if (coords.toString){
			res=coords.toString();

		}
return res;

	}
}


ymaps.ready(init);

