import webkit, gtk

window = gtk.Window()
browser = webkit.WebView()
window.add(browser)
window.set_default_size(370,170)
window.show()
browser.set_size_request(360,170)
browser.show()
browser.load_uri("file:///home/pi/smartmirror/apps/horoscope/url.html")
window.connect("delete-event",gtk.main_quit)
window.set_title("Horoscop")
gtk.main()

