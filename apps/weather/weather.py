import webkit, gtk
import os

window = gtk.Window()
browser = webkit.WebView()
window.add(browser)
window.set_default_size(200,240)
window.resize(200,240)
window.show()
browser.set_size_request(200,240)
browser.show()
browser.load_uri("file:///home/pi/smartmirror/apps/weather/bucharest.html")
window.connect("delete-event",gtk.main_quit)
window.set_title("Weather")
retvalue = os.system("/home/pi/smartmirror/speech/speech.sh Smarty Weather - Is it sunny or cloudy\?")
gtk.main()

