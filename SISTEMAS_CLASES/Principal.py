from Producto import Producto
from Persona import Persona
from CarritoDeCompras import CarritoDeCompras
from Empleado import Empleado
from Factura import Factura
from Caja import Caja1
from ArchivoPagoTargeta import ArchivoPagoTarjeta
from UnidadDeMedida import UnidadDeMedida
from ArchivoProducto import ArchivoProducto

from Sucursal import Sucursal
from Empresa import Empresa
from UnidadDeMedida import UnidadDeMedida
from Cliente import Cliente
from Encabezado import EncabezadoCarritoDeCompras
from FormaDePago import FormaDePago
from PagoEfectico import PagoEfectivo1
from PagoTageta import PagoTarjeta1
from PagoPse import PagoPse
from Historial import Historial
from Franquicias import Franquicias

from ArchivoSucursal import ArchivoSucursal
from ArchivoProducto import ArchivoProducto
from ArchivosFactura import ArchivosFactura
from ArchivoPagoPse import ArchivoPagoPse
from ArchivoPagoEfectivo import ArchivoPagoEfectivo
from ArchivoHistorial import ArchivoHistorial
from ArchivoPersona import ArchivoPersona
from ArchivoCaja import ArchivoCaja



## Creando los objetos 

sucursal=Sucursal("cr 36 a 99","Risos")
empresa=Empresa(sucursal)
producto=Producto(3200,"3312",UnidadDeMedida.kg)
carritoCompras=CarritoDeCompras(producto)
caja=Caja1("3")
cliente=Cliente("123456987","Juan pablo","juanpis43@gmail.com","321786948")
empleado=Empleado("9153578624","Ricardo","8976")

pagoEfectivo=PagoEfectivo1()
pagoTargeta=PagoTarjeta1()
pagoPse=PagoPse()

encabezado=EncabezadoCarritoDeCompras(pagoEfectivo,carritodecompras=carritoCompras)
factura=Factura(empresa,encabezado,cliente,empleado)
historial=Historial(caja)

# Archivos que se guardan

#Producto
archivoProducto=ArchivoProducto()
archivoProducto.GenerarArchivo(producto)
print()

#Factura
archivoFactura=ArchivosFactura()
archivoFactura.GenerarArchivoFactrura(factura)
print()

#Sucursal
sucursal.CajasSet("3")
archivoSucursal=ArchivoSucursal()
archivoSucursal.GenerarArchivoSucursal(sucursal)


# Pago Targeta
pagoTargeta.BancoSet("Nuestro banco")
pagoTargeta.CodigoSet("352648")
pagoTargeta.FranquiciaSet(franquicia=Franquicias.AmericanExpress)
total=int(3)
pagoTargeta.TotalPagarSet(total)
archivoPagoTargeta=ArchivoPagoTarjeta()
archivoPagoTargeta.GenerarArchivoPagoTarjeta(pagoTargeta)


# Pago Pse
pagoPse.BancoSet("otro banco")
pagoPse.DispisticoSet("computador")
pagoPse.CorreoSet("cristian56@gmail.com")

archivopagoPse=ArchivoPagoPse()
archivopagoPse.GenerarArchivo(pagoPse)

# Pago Efectivo

pagoEfectivo.MonedaSet("peso colombiano")
archivoPagoEfectivo=ArchivoPagoEfectivo()
archivoPagoEfectivo.GenerarArchivo(pagoEfectivo)

# Historial
historial.fechaSet("22/01/2022")
historial.HoraSet("9:45")
archivohistorial=ArchivoHistorial()
archivohistorial.GenerarArchivoHistorial(historial)

#Persona
persona=Persona("895623","nicolas")
archivopersona=ArchivoPersona()
archivopersona.GenerarArchivo(persona)

#caja

archivoCaja=ArchivoCaja()
archivoCaja.GenerarArchivo(caja)


















    