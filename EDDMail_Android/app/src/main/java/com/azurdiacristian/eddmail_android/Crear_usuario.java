package com.azurdiacristian.eddmail_android;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.ActionBarActivity;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.JsonObjectRequest;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.HashMap;

public class Crear_usuario extends ActionBarActivity {
    //atributos del Activity del tipo UI
    private Spinner sp_dominios;
    private Button b_aceptar;
    private EditText eT_usuario1;
    private EditText eT_usuario2;
    private EditText eT_dominio;
    private EditText eT_extension;
    private EditText eT_contraseña;
    //atributos de la clase del tipo objetos
    private String[] dominios;
    private ArrayAdapter<String> adaptador;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.layout_crear_usuario);
        iniciar_UI();
        imprimir_dominios();
    }

    private void iniciar_UI(){
        sp_dominios = (Spinner) findViewById(R.id.sp_dominios);
        b_aceptar =(Button) findViewById(R.id.b_aceptar);
        eT_usuario1 = (EditText) findViewById(R.id.eT_usuario);
        eT_usuario2 = (EditText) findViewById(R.id.eT_usuario2);
        eT_dominio = (EditText) findViewById(R.id.eT_dominio);
        eT_extension = (EditText) findViewById(R.id.eT_extension);
        eT_contraseña =(EditText) findViewById(R.id.eT_contraseña);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_crear_usuario, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
    /********************METODOS CREADOS PARA LAS FUNCIONALIDADES DEL ACTIVITY*********************/

    public void imprimir_dominios(){
        String url = "http://192.168.3.3:5000/consultar_dominios";
        JsonArrayRequest stringRequest = new JsonArrayRequest(url,
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        cargar_dominios(response);
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Log.i("Error:", error.toString());
            }
        });
        SingleTon.getInstance(getApplicationContext()).addToRequestQueue(stringRequest);
    }

    public void cargar_dominios(JSONArray response){
        int tamaño = response.length();
        dominios = new String[tamaño];
        for(int x=0; x<tamaño;x++ ){
            try{
                JSONObject dominio = response.getJSONObject(x);
                dominios[x] = dominio.getString("dominio");
            }catch (Exception e){
                Log.i("Error:",e.toString());
            }
        }
        adaptador = new ArrayAdapter<String>(this,android.R.layout.simple_spinner_item,dominios);
        sp_dominios.setAdapter(adaptador);
    }//fin del metodo cargar dominios

    public void Crear_usuario(View v){
        String user1 = eT_usuario1.getText().toString();
        String user2 = eT_usuario2.getText().toString();
        String pass = eT_contraseña.getText().toString();
        if(!user1.equals("") && user2.equals("")){
            String aux2 = sp_dominios.getSelectedItem().toString();
            post_usuario(user1+aux2,pass);
        }else if( user1.equals("") && !user2.equals("")){
            String aux2 = eT_dominio.getText().toString();
            String aux3 = eT_extension.getText().toString();
            post_usuario(user2+"@"+aux2+"."+aux3,pass);
        }else{
            Toast toast = Toast.makeText(this, "Elija solamente una opcion", Toast.LENGTH_SHORT);
            toast.show();
        }

    }//fin del metodo

    public void post_usuario(String usuario, String contraseña){
        String url = "http://192.168.3.3:5000/nuevo_usuario";
        HashMap<String,String> parametros = new HashMap();
        parametros.put("usuario",usuario);
        parametros.put("password",contraseña);

        JsonObjectRequest stringRequest = new JsonObjectRequest(
                Request.Method.POST,
                url,
                new JSONObject(parametros),
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        // Manejo de la respuesta
                        leer_objeto_json(response);
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // Manejo de errores
                    }
                });
        SingleTon.getInstance(getApplicationContext()).addToRequestQueue(stringRequest);
    }

    public void leer_objeto_json(JSONObject response){
        try{
            String respuesta = response.getString("mensaje");
            Toast toast = Toast.makeText(this, respuesta, Toast.LENGTH_SHORT);
            toast.show();
            Intent regresar = new Intent(Crear_usuario.this,Actividad_principal.class);
            startActivity(regresar);
        }catch(Exception e){
            Toast toast = Toast.makeText(this,e.getMessage(), Toast.LENGTH_SHORT);
            toast.show();
        }

    }//fin del metodo para leer los objetos json
}//fin de la clase activity
