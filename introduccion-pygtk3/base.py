"""
Primero importamos gi y decimos que version de Gtk
queremos que usar y luego importamos Gtk 
"""
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hola mundo")

        # create the magic here

# Instanciamos la clase MyWindow
win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()