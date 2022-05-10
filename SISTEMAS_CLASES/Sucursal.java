package Facturacion;

public class Sucursal {
    String Direccion;
    String Nombre;
    //Caja[] Cajas;

    public Sucursal(String direccion,String nombre){
        this.Direccion=direccion;
        this.Nombre=nombre;
    }

    @Override
    public String toString() {
        return "Sucursal{" +
                "Direccion='" + Direccion + '\'' +
                ", Nombre='" + Nombre + '\'' +
                '}';
    }
}
