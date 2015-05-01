package com.azurdiacristian.eddmail_android;

import android.util.Log;

import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.Response;

import org.json.JSONArray;
import org.json.JSONObject;

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

    public String[] imprimir_dominios(){
        String[] resultados;
        try{
            URL url = new URL("192.168.1.11:5000/consultar_dominios");
            Response respuestas  = get(url);
            JSONArray dominios = new JSONArray(respuestas.body().string());
            int tamaño =  dominios.length();
            resultados = new String[tamaño];
            for(int x= 0; x<tamaño; x++){
                JSONObject dominio = dominios.getJSONObject(x);
                resultados[x] = dominio.get("dominio").toString();
            }
            Log.i("Prueba", resultados[0]);
            return resultados;
        }catch(Exception e){
            return null;
            //no se que hacer aca
        }
        //return null;
    }

}
