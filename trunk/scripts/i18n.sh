#!/bin/sh

intltool-extract --type=gettext/glade ../glade/*.glade
xgettext -k_ -kN_ -o ../po/poldeg.pot ../src/*.py *.glade.h
rm -f *.glade.h
