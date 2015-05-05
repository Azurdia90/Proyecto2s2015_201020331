package com.azurdiacristian.eddmail_android;


import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.Response;

import java.io.IOException;
import java.net.URL;

/**
 * Created by Cristian on 30/04/2015.
 */
public class EDD_Get {

    OkHttpClient cliente = new OkHttpClient();

    /*Este metodo utiliza la libreria okhttp y oki para realizar un response
    a nuestro web service enviandole la url que deseamos, asi como tambien
    podemos obtener el response realizado y enviarlo como una cadena String
    que luego decidiremos si volverlo un objeto Json*/
    public Response get(URL url)throws IOException {
        Request request = new Request.Builder()
                .url(url)
                .build();
        Response response = cliente.newCall(request).execute();
        return response;
    }//fin del metod consumir get

    public String imprimir_dominios(){
        //String resultados;
        try{
            URL url = new URL("http://192.168.1.11:5000/consultar_dominios");
            Response respuestas  = get(url);
            if (respuestas != null){
                return "CONEXION EXITOSA";
            }else{
                return "NO HAY CONEXION";
            }
            //JSONArray dominios = new JSONArray(respuestas.body().string());
            //int tamaño =  dominios.length();
            //resultados = new String[tamaño];
            //for(int x= 0; x<tamaño; x++){
               // JSONObject dominio = dominios.getJSONObject(x);
                //resultados[x] = dominio.get("dominio").toString();
            //}

        }catch(Exception e){
            return e.toString();
            //no se que hacer aca
        }
    }//fin del metodo imprimir_dominios

}//fin de la clase
