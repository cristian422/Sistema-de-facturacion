package SISTEMAS_CLASES;

public class CarritoDeCompras {
    Producto ProductoSeleccionado;
    int Cantidad;
    int Total;

    public CarritoDeCompras(int cantidad,int total){

        this.Cantidad=cantidad;
        this.Total=total;
    }
    @Override
    public String toString() {
        return "CarritoDeCompras{" +
                "ProductoSeleccionado=" + ProductoSeleccionado +
                ", Cantidad=" + Cantidad +
                ", Total=" + Total +
                '}';
    }

    public Producto getProductoSeleccionado() {
        return ProductoSeleccionado;
    }

    public int getCantidad() {
        return Cantidad;
    }

    public int getTotal() {
        return Total;
    }
}
