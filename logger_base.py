import logging as log

log.basicConfig(level=log.DEBUG,
                format="%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s",
                datefmt="%d/%m/%Y  %I:%M:%S %p",
                handlers=[
                    log.FileHandler("capa_datos.log"),
                    log.StreamHandler()    
                ])

if __name__ == "__main__":
    log.debug("Mensaje a nivel debug")
    log.info("mensaje a nivel info")
    log.warning("mensaje a nivel de warning")
    log.error("mensaje a nivel de error")
    log.critical("mensaje a nivel de critical")