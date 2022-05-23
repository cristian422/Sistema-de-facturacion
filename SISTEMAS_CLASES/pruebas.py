from Cliente import cliente
from Factrura import Factura
from ArchivosFactura import ArchivosFactura
from Empleado import empleado
from Empresa import Empresa
from Sucursal import Sucursal
from ArchivoSucursal import ArchivoSucursal

sucur=Sucursal("cr35","pepe")
elcliente=cliente()
lafactura=Factura("5")
elempleado=empleado()
laEmpresa=Empresa()
##asignacion atributos

sucur.Cajas=[32,23,3]


archivo=ArchivoSucursal()
archivo.GenerarArchivoSucursal(sucur)
print("ya")



