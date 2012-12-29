==================
Sobre el sitio web
==================

:Autor: Mariano Reingart
:Email: reingart@gmail.com

Sitio web de la conferencia: http://ar.pycon.org/2012

Mas allá del esfuerzo empeñado en este tema (más de 300 cambios desde
2010 (https://code.google.com/p/web2conf/source/list),
con  una dedicación aproximada de
2 meses de trabajo fulltime (http://www.ohloh.net/p/web2conf)
e incluso haber tratado de explicado publicamente (http://pyconar.blogspot.com.ar/2012/07/sitio-web-de-pycon-argentina-un-poco-de.html)),
no fue suficiente.

Tomamos muchas características de PyCon US (http://us.pycon.org/) y
EuroPython (https://ep2012.europython.eu/), tratando de adaptarlas para nuestra
operatoria, costumbres y posibilidades.

Incluso simplificamos muchos aspectos como la registración y propuesta de
charlas (que comparativamente tiene menos pasos que los sitios mencionados).

Por los comentarios y discusiones, esto no fue percibido, y algunos de los
participantes solicitaron algo "más simple como en otros eventos" (quizás como
EventBrite (http://www.eventbrite.com/) o similar).

El problema es que para un evento como PyCon Argentina (gratuito, con decenas
de disertantes y miles de potenciales usuarios), se complicaría manejarlo de
esa manera porque necesitamos algunas características (como la agenda
personalizada (http://pyconar.blogspot.com.ar/2012/10/cronograma-personalizado-reserva-tu.html))
para estimar mejor la asistencia, funcionalidades para las
búsquedas laborales (campos y CV, que ya son tradicionales y las hemos
ofrecido a los sponsors desde la primera conferencia), o temas adicionales
como la previsualización de certificados y credenciales (que no solo es un
tema visual, sino que también podría ayudar a mejorar y evitar algunos
inconvenientes que venimos teniendo). 
Incluso el sitio tiene funcionalidad para adjuntar los slides que no ha sido
muy utilizada.
Incluír también la compaginación de las presentaciones, video y subtitulos sería 
ideal (y estamos trabajando en ello, ver: http://code.google.com/p/video2py),
sobre todo si es de manera colaborativa para reducir los tiempos y costos.

.. figure:: web/sshot.png
    :align: center
    :scale: 75 %

    Sitio web de la conferencia

Por otro lado, tenemos recursos limitados y poca colaboración para esta
aplicación. En general, la cantidad de administradores/desarrolladores no
supera las dos personas  (desde 2009, ya sea en web2py o django), recibimos
pocos reportes de incidentes (menos de 10 en el sitio del proyecto) y menos
parches aún (1 solo este año). Incluso, el interés decrece sensiblemente
luego de que termina la conferencia, y se hace sentir cuando hay que actualizar
los sitios web anteriores para mantener un archivo histórico.
Obviamente es necesario modernizar la apariencia y navegación. Este año dimos
un primer paso respecto al diseño gráfico, y tuvimos una propuesta de una
empresa para mejorar el HTML que lamentablemente no se concretó.

Si bien muchos de estos temas pueden parecer accesorios y se podría
tranquilamente usar algún paquete "extranjero" o directamente un sitio
estático y recibir las charlas por mail, me parecería un retroceso, no
solo perderíamos la experiencia y trabajo de estos últimos 4 años
(comenzando desde 0 otra vez), sino que resultaría menos práctico, poco
transparente y hasta desprolijo (dependiendo de la opción elegida).

Una última recomendación sobre este tema es no desarrollar el sitio web a la
par de la conferencia. Lamentablemente venimos con ese "modus operandi" desde
2009 (por falta de tiempo e intentos fallidos), haciendo ajustes sobre la
marcha, que si bien son necesarios para implementar las mejoras, también
causan cierta confusión de los usuarios menos experimentados y generan algunos
inconvenientes de estabilidad y performance.

Lo ideal sería tener todo definido y probado antes de comenzar con el llamado
a propuestas de charlas.
