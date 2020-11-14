Sous l'océan
============

**Category** : Forensic
**Score** : 50 points
**Solved** : 286 times

---

>Nous pensons avoir retrouvé la trace d'Eve Descartes. Nous avons reçu un fichier anonyme provenant d'un smartphone Android (probablement celui de son ravisseur). Retrouvez des informations dans son historique de position.

>Le flag est de la forme DGSESIEE{x} avec x une chaine de caractères

#### Files

* [memdump.txt](memdump.txt) (29c702ff8dc570319e5e8d05fc4cb96c1536b595b9a4e93d6205774f9afd2bff)

This file is a debug dump of an android smartphone. We are told to retrieve information from the geolocation history. 
The dump being 61584 lines, it's bit hard to comb by hand, but it's helpfully organized in sections with one section for every running service, and a list of services at the start.

```
Currently running services:
 DockObserver
 SurfaceFlinger
 accessibility
 account
 activity
 alarm
[...]
 launcherapps
 location           <<<< this is the one we want to check out
 lock_settings
[...]
```

All sections start like this:

```
-------------------------------------------------------------------------------
DUMP OF SERVICE servicename:
[...]
```

So we can just text search for "DUMP OF SERVICE location" to get to the interesting part: 

```
-------------------------------------------------------------------------------
DUMP OF SERVICE location:
[...]
  Custom Location 1
 gps: Location[gps -47,1462046 30,9018186 hAcc=20 et=??? alt=0.0 vel=0.0 bear=0.0 vAcc=??? sAcc=??? bAcc=??? {Bundle[{satellites=0, maxCn0=0, meanCn0=0}]}]
 gps: Location[gps -47,1963297 30,9012294 hAcc=20 et=??? alt=0.0 vel=0.0 bear=0.0 vAcc=??? sAcc=??? bAcc=??? {Bundle[{satellites=0, maxCn0=0, meanCn0=0}]}]
 gps: Location[gps -47,1970164 30,8641039 hAcc=20 et=??? alt=0.0 vel=0.0 bear=0.0 vAcc=??? sAcc=??? bAcc=??? {Bundle[{satellites=0, maxCn0=0, meanCn0=0}]}]
 gps: Location[gps -47,1438013 30,8652827 hAcc=20 et=??? alt=0.0 vel=0.0 bear=0.0 vAcc=??? sAcc=??? bAcc=??? {Bundle[{satellites=0, maxCn0=0, meanCn0=0}]}]
 gps: Location[gps -47,1448313 30,9642508 hAcc=20 et=??? alt=0.0 vel=0.0 bear=0.0 vAcc=??? sAcc=??? bAcc=??? {Bundle[{satellites=0, maxCn0=0, meanCn0=0}]}]
Custom Location 2
 gps: Location[gps -47,0820032 30,8641039 hAcc=20 et=??? alt=0.0 vel=0.0 bear=0.0 vAcc=??? sAcc=??? bAcc=??? {Bundle[{satellites=0, maxCn0=0, meanCn0=0}]}]
 gps: Location[gps -47,1300684 30,8643986 hAcc=20 et=??? alt=0.0 vel=0.0 bear=0.0 vAcc=??? sAcc=??? bAcc=??? {Bundle[{satellites=0, maxCn0=0, meanCn0=0}]}]
[...]
```

We now have a long list of GPS coordinates. Looking one up in google maps, it seems to be in the middle of the ocean - in fact, all of them seem to be clustered in that region out in the ocean.

Next step is to draw lines between those coordinates, hoping they spell out something.

To do that quickly, I hijacked Google Maps's [polyline lib jsfiddle example](https://developers.google.com/maps/documentation/javascript/examples/polyline-simple):

```js
function initMap() {
	const coords = [
		[{lat: -47.1462046, lng: 30.9018186},
		 {lat: -47.1963297, lng: 30.9012294},
		 {lat: -47.1970164, lng: 30.8641039},
		 {lat: -47.1438013, lng: 30.8652827},
		 {lat: -47.1448313, lng: 30.9642508}],

		[{lat: -47.0820032, lng: 30.8641039},
		 {lat: -47.1300684, lng: 30.8643986},
		 {lat: -47.1304118, lng: 30.9006402},
		 {lat: -47.0789133, lng: 30.9003456},
		 {lat: -47.0847498, lng: 30.8131067},
		 {lat: -47.1307551, lng: 30.8148758},
		 {lat: -47.1304118, lng: 30.8340395},
		 {lat: -47.1084391, lng: 30.8319759}],

		[{lat: -47.0631205, lng: 30.8649880},
		 {lat: -47.0322214, lng: 30.9015240},
		 {lat: -47.0047556, lng: 30.8608621},
		 {lat: -47.0411478, lng: 30.8632198}],

		[{lat: -46.9934318, lng: 30.8750074},
		 {lat: -46.9481132, lng: 30.8744180},
		 {lat: -46.9532630, lng: 30.9085939},
		 {lat: -46.9961784, lng: 30.9047644},
		 {lat: -46.9927451, lng: 30.8511361},
		 {lat: -46.9457099, lng: 30.8508414}],

		[{lat: -46.9295737, lng: 30.8517256},
		 {lat: -46.9072578, lng: 30.8926859},
		 {lat: -46.8797919, lng: 30.8534940},
		 {lat: -46.9137809, lng: 30.8505466}],

		[{lat: -46.8571326, lng: 30.8912128},
		 {lat: -46.8564460, lng: 30.8484834}],

		[{lat: -46.8173416, lng: 30.8745954},
		 {lat: -46.7703064, lng: 30.8743007},
		 {lat: -46.7778595, lng: 30.9096549},
		 {lat: -46.8242081, lng: 30.9040580},
		 {lat: -46.8125351, lng: 30.8404074},
		 {lat: -46.7733963, lng: 30.8474818}],

		[{lat: -46.7438706, lng: 30.8772474},
		 {lat: -46.7009552, lng: 30.8784261},
		 {lat: -46.7054184, lng: 30.9034689},
		 {lat: -46.7479904, lng: 30.8978716},
		 {lat: -46.7376908, lng: 30.8474818},
		 {lat: -46.7115982, lng: 30.8498398}],

		[{lat: -46.6456803, lng: 30.9261490},
		 {lat: -46.6625031, lng: 30.9264435},
		 {lat: -46.6611298, lng: 30.8748901},
		 {lat: -46.6473969, lng: 30.8657549},
		 {lat: -46.6580399, lng: 30.8563241},
		 {lat: -46.6587265, lng: 30.8014891},
		 {lat: -46.6377838, lng: 30.7985401}],

		[{lat: -46.5794168, lng: 30.8664391},
		 {lat: -46.5780435, lng: 30.9070986},
		 {lat: -46.6178690, lng: 30.9082768},
		 {lat: -46.6213022, lng: 30.8463976},
		 {lat: -46.5752970, lng: 30.8428605},
		 {lat: -46.5746103, lng: 30.8693860}],

		[{lat: -46.5114389, lng: 30.9053311},
		 {lat: -46.5443979, lng: 30.9047420},
		 {lat: -46.5395914, lng: 30.8351962},
		 {lat: -46.4997659, lng: 30.8351962}],

		[{lat: -46.4729868, lng: 30.9006178},
		 {lat: -46.4338480, lng: 30.9017961},
		 {lat: -46.4338480, lng: 30.8623132},
		 {lat: -46.4695535, lng: 30.8623132},
		 {lat: -46.4338480, lng: 30.8629027},
		 {lat: -46.4297281, lng: 30.8222244},
		 {lat: -46.4674936, lng: 30.8269416}],

		[{lat: -46.3644968, lng: 30.8204554},
		 {lat: -46.3727365, lng: 30.9076877},
		 {lat: -46.4214884, lng: 30.8682072},
		 {lat: -46.3425241, lng: 30.8629027}],

		[{lat: -46.3184915, lng: 30.8198657},
		 {lat: -46.3219248, lng: 30.9041528},
		 {lat: -46.2752329, lng: 30.8169173},
		 {lat: -46.2793527, lng: 30.9035636}],

		[{lat: -46.2477670, lng: 30.9218260},
		 {lat: -46.2196146, lng: 30.9212369},
		 {lat: -46.2154947, lng: 30.8646709},
		 {lat: -46.2409006, lng: 30.8469871},
		 {lat: -46.2100015, lng: 30.8346066},
		 {lat: -46.2120615, lng: 30.7827088},
		 {lat: -46.2450205, lng: 30.7762196}]
	];
	const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 8,
    center: coords[Math.floor(coords.length/2)][0],
    mapTypeId: "terrain",
  });
  for (var letter in coords) {
		new google.maps.Polyline({
    	path: coords[letter],
    	geodesic: true,
    	strokeColor: "#FF0000",
    	strokeOpacity: 1.0,
    	strokeWeight: 2,
		}).setMap(map);
	}
}
```

![the flag.](flag.png)
