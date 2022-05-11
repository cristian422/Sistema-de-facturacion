package SISTEMAS_CLASES;

import org.json.JSONObject;

public class Principal {
    public static void main(String[] args) {
        /**
         *
         *
         *
         *
         */
        JSON JsonSucursal= new JSON();
        JsonSucursal.CrearObjetoSucursal();
        System.out.println("escribir");
        JsonSucursal.EscribirJsonSucursal();
        JsonSucursal.leerJsonSucursal();


        System.out.println("el siguiente es la clase producto");
        JSON JsonProducto= new JSON();
        JsonProducto.CrearObjetoProducto();
        System.out.println("escribimos el producto");
        JsonProducto.EscribirJsonProducto();
        System.out.println("leemos ");
        JsonProducto.LeerJsonProducto();

        System.out.println("el siguiente es las clase carrito de compras");
        JSON JsonCarrito=new JSON();
        JsonCarrito.CrearObjetoCarritoDecompras();
        System.out.println("escribimos el carrito");
        JsonCarrito.EscribirJsonCarritoDeCompras();
        System.out.println("leemos el carrito");
        JsonCarrito.LeerJsonCarritoDeCompras();






    }
}



