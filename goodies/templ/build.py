#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import string

PATH = os.path.abspath(os.path.dirname(__file__))

OUT = os.path.join(PATH, "out")

DATA = [
    ("Juan Bautista Cabral", "Co-Organizador General"),
    ("Nadia Luczywo", u"Tesorera"),
    ("Nadia Luczywo", u"Asistente"),
    ("Gustavo Taira", u"Diseñador Gráfico"),
    ("Analy Laudado", u"Diseñador Gráfico"),
    ("Salvador Bravo", u"Artista")

]

import shutil, codecs

src = string.Template(codecs.open("certpycon.svg", encoding="utf-8").read())

shutil.rmtree(OUT)

if not os.path.exists(OUT):
    os.mkdir(OUT)

for idx, data in enumerate(DATA):
    nombre, participacion = data
    rend = src.substitute(nombre=nombre, participacion=participacion)
    fname = os.path.join(OUT, "{idx}.svg".format(idx=idx))
    with codecs.open(fname, "w", encoding="utf-8") as fp:
        fp.write(rend)
    out = os.path.join(OUT, "{idx}.png".format(idx=idx))
    cmd = "inkscape -d 300 {fname} -z -e {out}".format(fname=fname, out=out)
    os.system(cmd)

#os.system("rm {}/*.svg".format(OUT))

