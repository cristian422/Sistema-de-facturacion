from Cliente import Cliente
from Factrura import Factura
from ArchivosFactura import ArchivosFactura
from Empleado import empleado
from Empresa import Empresa
from Sucursal import Sucursal
from ArchivoSucursal import ArchivoSucursal
from UnidadDeMedida import UnidadDeMedida


sucur=Sucursal("cr35","pepe")
elcliente=Cliente()
lafactura=Factura("5")
elempleado=empleado()
laEmpresa=Empresa(sucur)
#asignacion atributos
sucur.Cajas=[32,23,3]
#archivo=ArchivoSucursal()
#archivo.GenerarArchivoSucursal(sucur)
print("ya")
#pruebas carrito de compras

from Producto import Producto
from CarritoDeCompras import CarritoDeCompras

product=Producto(3500,"3312",UnidadDeMedida.kg)

carrito=CarritoDeCompras(product)
print(carrito.Cantidad)

carrito.AumentarCantidad()
print(carrito.Cantidad)

