# TP Web Requests

Ce TP consiste a récupérer des données d'une api (météo, twitter ...) et de l'afficher sur votre site, exemple pour une API météo vous afficher la météo d'une ville que l'utilisateur choisi

![](https://i.imgur.com/DuFqpoT.png)


Ducoup on réutilise Flask pour ce tp, pour gérer le site
Pour accéder à une API on a besoin de faire une requête vers un site web pour ce faire on utilise la librairie requests de python (elle est présente par défaut dans python sinon on installe comme d'habitude avec `pip install requests`)
`import requests`


Pour effectuer une requête on utilise la fonction  requests.get() qui renvoit un fichier un objet de type Response qu'on peut manipuler pour obtenir le code source de la page
```
import requests

response = requests.get('https://www.google.com/')

print(response.text)
```


```
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="fr"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="tLqiKGRfxiKmK5iWFdHkow==">(function(){window.google={kEI:'DALxYafOO7yMjLsPyomAgAM',kEXPI:'0,1302536,56873,1709,4350,206,4804,2316,383,246,5,1354,4013,1238,1122515,1197719,675,36,380061,16114,28684,17572,4858,1362,9291,3024,17584,4020,978,13228,3847,4192,6430,22741,5081,1593,1279,2742,149,1103,840,1983,4314,109,3405,606,2023,1733,43,521,14670,3173,54,419,2426,7,4808,1,790,11851,16320,908,2,940,2615,3783,9359,3,576,4386,2073,149,13965,1,1,2,1538,2304,7039,4684,15625,1714,3050,2658,7357,30,15933,2132,16786,5830,2527,4094,17,4035,3,3541,1,16807,38,6866,18443,2,14022,1931,4318,1271,744,5852,8703,618,1142,1160,5679,1021,2377,2721,9767,5120,3347,27,2,1,11,7748,4568,525,2053,3681,18628,2172,2618,437,815,16135,961,86,515,3105,4333,4386,1703,135,1708,1,1,1508,1482,524,7275,2297,2081,781,6,644,1023,2,1,1609,2165,921,1065,2,1242,619,962,10,1,173,239,7803,204,42,44,62,113,857,303,514,510,334,1359,1134,5,37,5,394,68,768,181,798,1,187,2,227,262,2,799,1459,628,13,322,599,2724,800,336,874,41,190,72,956,53,160,30,1106,450,716,371,287,264,1723,1404,241,84,2840,187,5496439,99,599,5995445,1172,211,2800485,882,444,1,2,80,1,1796,1,9,2553,1,748,141,795,563,1,4265,1,1,2,1331,4142,2609,155,17,13,72,139,4,2,20,2,169,13,19,46,5,39,96,548,29,2,2,1,2,1,2,2,7,4,1,2,2,2,2,2,2,353,513,186,1,1,158,3,2,2,2,2,2,4,2,3,3,269,1601,141,204,51,61,8,3,5,3,4,1,2,4,13,5,2,9,25,4,4,1,23952571,4041690,3,2414,1491,9,1435,159,1358,4726,3,927,318,20,1035,2096,1079,46,1205',kBL:'kt7M'};google.sn='webhp';google.kHL='fr';})();(function(){
var f=this||self;var h,k=[];function l(a){for(var b;a&&(!a.getAttribute||!(b=a.getAttribute("eid")));)a=a.parentNode;return b||h}function m(a){for(var b=null;a&&(!a.getAttribute||!(b=a.getAttribute("leid")));)a=a.parentNode;return b}
```

Pour effectuer une requête API on utilise le même code sauf qu'on transforme le texte que renvoit la requête een un dictionnaire, car la page renvoit de la data sous forme de json `data = json.loads(response)`
