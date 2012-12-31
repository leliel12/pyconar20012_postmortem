=============
Acerca de ...
=============

Licencia
--------

.. figure:: about/cc.png
    :align: center
    :scale: 20 %

    Pycon Argentina 2012 - Post-Mortem por PyAr se
    encuentra bajo una licencia
    `Creative Commons Atribución-SinDerivadas 3.0 Unported <http://creativecommons.org/licenses/by-nd/3.0/deed.es>`_.


Referencias
-----------

- Fuentes de este documento: https://bitbucket.org/leliel12/pyconar20012_postmortem
- Pagina web del evento: http://ar.pycon.org/2012
- PyAr: http://pyar.org.ar
- Hitchhiker's guide to make a PyConAr2010: http://python.org.ar/pyar/HGTTP
- DebConf Final Reports: http://media.debconf.org/reports/
- PgCon Brasil 2009: http://pgbr.postgresql.org.br/2009/asl/pgcconbr-2009prestcontas.pdf
- Evaluación de las 7JRSL: http://robertoallende.com/es/evaluacion-de-las-7jrsl
- Free software and education - Fighting the digital divide: http://www.downes.ca/presentation/247


Objetivo y estructura de este documento
---------------------------------------

Este documento se deja como referencia a la posteridad para futuros
organizadores de PyCons

Fue inspirado en los reportes finales de *DebConf*,
*Evaluación de las 7JRSL* y *PgCon Brasil 2009*,
siguiendo las necesidades establecidas en el artículo
*Hitchhiker's guide to make a PyConAr2010*.

La estructura que se estableció para los capítulos se desprende de los
siguientes criterios:

- Objetivos de la conferencia (como el caso del track científico)
- Independencia con otras áreas (como el caso de lo administrativo)
- Factores críticos (proveedores)
- Feedback (Todos los artículos relacionados con opiniones)

La estructúra de "Lo Bueno, Lo Malo y Lo Feo" esta inspirada en el artículo
*Free software and education - Fighting the digital divide*.

Todas las referencias aquí citadas se encuentran debidamente enlazadas en el
apartado *Referencias* de este mismo capítulo.


Entendiendo "Lo Bueno, Lo Malo y lo Feo"
----------------------------------------

A lo largo de todo el documento vera que casi todo capitulo contiene un resumen
dividido en "Lo Bueno, Lo Malo y lo Feo". Estos tres grupos de registros deben
ser interpretados de la siguiente manera.

- **Lo Bueno:** Son aciertos organizativos, comunitarios o de suerte que
  favorecieron a la conferencia que, de ser posible, deben ser imitados a
  futuro.
- **Lo Malo:** Son desaciertos menores organizativos, comunitarios o de suerte
  que, de ser posible, deben ser evitados a futuro.
- **Lo Feo:** Son desaciertos mayores organizativos, comunitarios o de suerte
  que ponen en riesgo aspectos críticos de la conferencia. En el futuro deben
  ser tenidos en cuenta ya que no pueden bajo ninguna circunstancia suceder en
  una PyCon.


Versiones
---------

El número de versión de este documento se compone de:

::

    <YEAR>.<MONTH>.<DAY>.<HOUR><MINUTES><STATUS>

Siendo ``STATUS`` alfa, beta o no hay status en el
caso de que el documento ya sea una version final. La hora y los
minutos se establecen con un mercurial hook justo antes de iniciar el push.


Staff
-----

PyCon Argentina es organizada por un grupo de voluntarios dedicados y con
experiencia en la comunidad internacional de Python. El núcleo del comité de
organización consiste en:

- **Coordinador General:** Mariano Reingart <reingart@gmail.com>
- **Co-Coordinador General:** Juan B. Cabral <jbc.develop@gmail.com>
- **Tesorera:** Nadia Ayelen Luczywo <nluczywo@gmail.com>
- **Secretaria:** Romina Castrogiovani <r.castrogiovani@gmail.com>
- **Coordinador de Charlas:** Alejandro J. Cura <alecu@protocultura.net>
- **Coordinador de Becas y Donaciones:** Facundo Batista
  <facundobatista@gmail.com>
- **Coordinadores Sede:**
    - Sebastián Bassi <sbassi@gmail.com>
    - Alberto Paparelli <albertopaparelli@gmail.com>
- **Responsable de Speakers Internacionales:** Gabriela Arevalo
  <gabriela.b.arevalo@gmail.com>
- **Webmaster:** Alan Etkin <spametki@gmail.com>
- **Coordinador en UNQui:** Leonardo Marina <leonardo@unq.edu.ar>
- **Revisores de Charlas:**
    - Hector Sanchez <hectorsanchez.mov@gmail.com>
    - Sebastián Bassi <sbassi@gmail.com>
    - Maximiliano Robaina <maxirobaina@gmail.com>
    - Emiliano Dalla Verde Marcozzi <6564766d@gmail.com>
    - Mariano Guerra <luismarianoguerra@gmail.com>
    - Damián Ávila <damianavila@gmail.com>
    - Marcelo Fidel Fernandez <marcelo.fidel.fernandez@gmail.com>
    - Ángel Velázquez <angelvelasquez@gmail.com>
- **Registración:**
    - Maria Orfilia Schleppi <orfi.sch@gmail.com>
    - Nadia Ayelen Luczywo <nluczywo@gmail.com>
    - Romina Castrogiovani <r.castrogiovani@gmail.com>
    - Juan Martín Báscolo <martin.bascolo@gmail.com>
    - Juan Pedro Fisanotti <fisadev@gmail.com>
- **Editor del Post-Mortem:** Juan B. Cabral <jbc.develop@gmail.com>
- **Redactores del Post-Mortem:**
    - Celia Cintas <cintas.celia@gmail.com>
    - Facundo Batista <facundobatista@gmail.com>
    - Nadia Ayelen Luczywo <nluczywo@gmail.com>
    - Juan B. Cabral <jbc.develop@gmail.com>
    - Mariano Reingart <reingart@gmail.com>
    - Romina Castrogiovani <r.castrogiovani@gmail.com>
    - Damián ávila <damianavila@gmail.com>
    - Juan Pedro Fisanotti <fisadev@gmail.com>
    - Gabriela Arevalo <gabriela.b.arevalo@gmail.com>
    - Maria Orfilia Schleppi <orfi.sch@gmail.com>
    - Marcelo Fidel Fernandez <marcelo.fidel.fernandez@gmail.com>

Nuestro reconocimiento para los voluntarios y empresas que participan del
evento colaborando con la organización:

- **Logo y Sitio Web:** Gustavo Taira <gustaira@gmail.com>
- **Mousepad y Banners:** Analy Laudado <anitalaudado@gmail.com>
- **Arte:** Salvador Bravo <ta3kaiserhotmail.com@gmail.com>
- **Diagramación de Programa:** Cristian Bruscella <agustin.mendieta@gmail.com>
- **Imprenta:** Imprenta Lozano
- **Filmación:**
    - Universidad Nacional de Quilmes
    - Posta Productora Audiovisual
    - Pablo M. Mana <pablo.m.mana@gmail.com>
- **Infraestructura y Redes:** Universidad Nacional de Quilmes


Compilar este documento
-----------------------

- Instalar todas las dependencias de Sphinx y latexpdf (http://sphinx-doc.org/)
- Configurar un hook en ``.hg/hgrc`` como el siguiente:


.. code-block:: cfg

    [paths]
    default = https://@bitbucket.org/leliel12/pyconar20012_postmortem

    [hooks]
    pre-push = python postmortem/prepush.py


- Para compilar en la carpeta ``postmortem``

.. code-block:: console

    $ make latexpdf html


.. only:: latex

    Made with `Sphinx <http://sphinx-doc.org/>`_!
