package SISTEMAS_CLASES;

public class Producto {
    int Precio;
    String IdProducto;
    UnidadDeMedida UnidadDeMedida;

    public Producto(int precio,String idProducto){
        this.Precio=precio;
        this.IdProducto=idProducto;


    }

    public int getPrecio() {
        return Precio;
    }

    public void setPrecio(int precio) {
        Precio = precio;
    }

    public String getIdProducto() {
        return IdProducto;
    }

    public void setIdProducto(String idProducto) {
        IdProducto = idProducto;
    }

    public SISTEMAS_CLASES.UnidadDeMedida getUnidadDeMedida() {
        return UnidadDeMedida;
    }

    public void setUnidadDeMedida(SISTEMAS_CLASES.UnidadDeMedida unidadDeMedida) {
        UnidadDeMedida = unidadDeMedida;
    }

    @Override
    public String toString() {
        return "Producto{" +
                "Precio=" + Precio +
                ", IdProducto='" + IdProducto + '\'' +
                ", UnidadDeMedida=" + UnidadDeMedida +
                '}';
    }
}
