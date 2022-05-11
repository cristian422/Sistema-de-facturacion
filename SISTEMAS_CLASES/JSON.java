package SISTEMAS_CLASES;


import org.json.JSONObject;

import java.io.BufferedWriter;

import java.io.File;
import java.io.IOException;

import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.OpenOption;
import java.nio.file.Path;
import java.nio.file.Paths;

public class JSON {
    private final String Archivo = "C:\\Users\\57322\\Desktop\\facturacion\\SISTEMAS_CLASES\\ArchivoJson1.json";

    //el siguiente es la url de la direccion donde esta la carpeta .json de producto
    private final String ArchivoJsonProducto = "C:\\Users\\57322\\Desktop\\facturacion\\SISTEMAS_CLASES\\ArchivoJsonProducto.json";

    //url del archivo json carrito de compras
    private final String ArchivoJsonCarritoDeCompras = "C:\\Users\\57322\\Desktop\\facturacion\\SISTEMAS_CLASES\\ArchivoJsonCarritoDeCompras.json";


    /**
     * creando los objetos json
     */
    public JSONObject CrearObjetoSucursal() {
        /**
         * 1 creo el objeto que voy a guardar
         */
        Sucursal nuevaSucursal = new Sucursal("cr 35a #99-129", "Fruver");
        /**
         * 2 creso el objeto json
         */
        JSONObject ObjetoJson = new JSONObject();
        /**
         * 3. le coloco al objeto clave valor
         */
        ObjetoJson.put("direccion", nuevaSucursal.getDireccion());
        ObjetoJson.put("nombre", nuevaSucursal.getNombre());


        System.out.println(ObjetoJson.toString());
        return ObjetoJson;
    }

    /**
     * en este guardamos la informacion que creamos
     */
    public void EscribirJsonSucursal() {
        try {

            BufferedWriter Escritor = Files.newBufferedWriter(Path.of(Archivo), Charset.defaultCharset());
            JSONObject objetoJson = this.CrearObjetoSucursal();
            Escritor.write(objetoJson.toString());
            Escritor.close();

        } catch (IOException e) {
            System.out.println("Error al escribir");

        }
    }

    public void leerJsonSucursal() {
        try {
            String cadena = Files.readString(Path.of(Archivo));
            System.out.println("cadena leida: " + cadena);
            JSONObject objetoJson = new JSONObject(cadena);
            String direccion = objetoJson.getString("direccion");
            String nombre = objetoJson.getString("nombre");
            Sucursal nuevaSucursal = new Sucursal(direccion, nombre);
            System.out.println("la sucursal leida es: " + nuevaSucursal);

        } catch (IOException e) {
            System.out.println("Error al escribir");

        }
    }

    /**
     * hacemos lo mismo de crear el objeto y escribirlo pero para la clase producto
     */
    public JSONObject CrearObjetoProducto() {
        Producto NuevoProducto = new Producto(3500, "1407");
        JSONObject objetojsonProducto = new JSONObject();
        objetojsonProducto.put("precio", NuevoProducto.getPrecio());
        objetojsonProducto.put("idProducto", NuevoProducto.getIdProducto());


        System.out.println(objetojsonProducto.toString());
        return objetojsonProducto;
    }

    public void EscribirJsonProducto() {
        try {
            BufferedWriter EscritorProducto = Files.newBufferedWriter(Path.of(ArchivoJsonProducto), Charset.defaultCharset());
            JSONObject objetoJsonProducto = this.CrearObjetoProducto();
            EscritorProducto.write(objetoJsonProducto.toString());
            EscritorProducto.close();

        } catch (IOException ex) {
            System.out.println("Error al escribir");
        }

    }

    //devuelve de un archivo json a un objeto producto
    public Producto LeerJsonProducto() {


        String cadena = null;
        try {
            cadena = Files.readString(Path.of(ArchivoJsonProducto));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        System.out.println("cadena leida: " + cadena);
        JSONObject objetoJson = new JSONObject(cadena);
        int precio = objetoJson.getInt("precio");
        String idProducto = objetoJson.getString("idProducto");
        Producto nuevoProducto = new Producto(precio, idProducto);
        System.out.println("el producto leido es: " + nuevoProducto);


        return nuevoProducto;
    }

    /**
     * como tercera clase es carrito de compras
     */
    public JSONObject CrearObjetoCarritoDecompras() {

        CarritoDeCompras nuevoCarrito = new CarritoDeCompras(3, 2384);
        JSONObject objetoJsonNuevoCarrito = new JSONObject();
        objetoJsonNuevoCarrito.put("cantidad", nuevoCarrito.getCantidad());
        objetoJsonNuevoCarrito.put("total", nuevoCarrito.getTotal());


        System.out.println(objetoJsonNuevoCarrito.toString());
        return objetoJsonNuevoCarrito;
    }

    /**
     * p
     */
    public void EscribirJsonCarritoDeCompras() {
        try {
            BufferedWriter Escritor = Files.newBufferedWriter(Path.of(ArchivoJsonCarritoDeCompras), Charset.defaultCharset());
            JSONObject objetoJson = this.CrearObjetoCarritoDecompras();
            Escritor.write(objetoJson.toString());
            Escritor.close();
        } catch (IOException e) {
            System.out.println("Error al escribir");
        }
    }


    public void LeerJsonCarritoDeCompras() {
        try {
            String cadena = Files.readString(Path.of(ArchivoJsonCarritoDeCompras));
            System.out.println("cadena leida: " + cadena);
            JSONObject objetoJson = new JSONObject(cadena);
            int cantidad = objetoJson.getInt("cantidad");
            int total = objetoJson.getInt("total");
            CarritoDeCompras nuevocarrito = new CarritoDeCompras(cantidad, total);
            System.out.println("el carrito leido es: " + nuevocarrito);

        } catch (IOException e) {
            System.out.println("Error al escribir");
        }


    }
}
