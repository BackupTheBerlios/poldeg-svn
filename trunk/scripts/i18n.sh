#!/bin/sh

intltool-extract --type=gettext/glade ../glade/win_main.glade
intltool-extract --type=gettext/glade ../glade/win_progress.glade
xgettext -k_ -kN_ -o ../po/poldeg.pot ../src/*.py ../glade/*.glade.h
rm -f ../glade/*.glade.h
