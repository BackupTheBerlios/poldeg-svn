#!/bin/sh

intltool-extract --type=gettext/glade ../glade/poldeg.glade
xgettext -k_ -kN_ -o ../po/poldeg.pot ../src/*.py ../glade/poldeg.glade.h
rm -f ../glade/poldeg.glade.h
