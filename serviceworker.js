var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/acerca',
    '/arsenal',
    '/formulario',
    '/equipos',
    '/registro',
    '/static/ProyectowebApp/css/estilos.css',
    '/static/ProyectowebApp/img',
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request).then(function(response) {

          return fetch(event.request)
          .catch(function(rsp) {
             return response; 
          });
          
          
        })
    );
});


//solo para cachear todo reemplazar por esta versión del Fetch


self.addEventListener('fetch', function(event) {
    event.respondWith(

      fetch(event.request)
      .then((result)=>{
        return caches.open(CACHE_NAME)
        .then(function(c) {
          c.put(event.request.url, result.clone())
          return result;
        })
        
      })
      .catch(function(e){
          return caches.match(event.request)
      })
  

     
    );
});
