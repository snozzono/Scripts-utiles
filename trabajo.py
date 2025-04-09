import webbrowser
import time

# Ruta de Firefox en Windows
firefox_path = "C://Program Files//Mozilla Firefox//firefox.exe"

# Registrar Firefox como navegador
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))

# Lista de sitios de empleo en Chile
urls = [
    "https://www.laborum.cl/en-region-metropolitana/empleos-part-time-publicacion-menor-a-7-dias-modalidad-presencial.html",
    "https://www.trabajando.cl/trabajo-empleo?region=1&jornadas=3",
    "https://www.chiletrabajos.cl/encuentra-un-empleo?2=&13=1022&fecha=&categoria=&8=&14=21&inclusion=&f=2",
    "https://cl.indeed.com/jobs?q=&l=Santiago+de+Chile%2C+Regi%C3%B3n+Metropolitana&fromage=7&sc=0kf%3Aattr%2875GKK%29%3B&from=searchOnDesktopSerp&vjk=03681dee85cfd56b",
    "https://cl.computrabajo.com/empleos-en-rmetropolitana-jornada-part-time?pubdate=7&by=publicationtime",
    "https://www.bne.cl/ofertas?mostrar=empleo&textoLibre=&idRegion=378&idTipoJornada=10&fechaIniPublicacion=7%2F4%2F2025&numPaginaRecuperar=1&numResultadosPorPagina=10&clasificarYPaginar=true&totalOfertasActivas=6992",
    "https://duoclaboral.cl/trabajo/trabajos-en-chile?Search%5Bterms%5D=&Search%5BjobOfferType%5D=0&Search%5BgenericCareer%5D=&Search%5Bremote%5D=&Search%5Bregion%5D=1&Search%5Btownship%5D=&Search%5BworkDayType%5D=2&Search%5BjobArea%5D=&Search%5Binclusive%5D=&Search%5BdateFilter%5D=2&Search%5BorderFilter%5D=&Search%5BminExperience%5D=&Search%5BmaxExperience%5D=&Search%5BminSalary%5D=&Search%5BmaxSalary%5D=&Search%5B_token%5D=8fac0884181ccc414554a44f31c843.PScc-28PjHdb0rTmeai3YEftHeJdF2GRq8E8R5pFhzw.SHJwqT5hvkJi5N_LN_rvUBO-ZYASe1Hw7aR_ItQX4BEEX3eQADjqADilhA#"
]

# Abrir cada página en una nueva pestaña
for url in urls:
    webbrowser.get('firefox').open_new_tab(url)
    time.sleep(1)  # Espera 1 segundo entre aperturas (puede quitarse o ajustarse)
