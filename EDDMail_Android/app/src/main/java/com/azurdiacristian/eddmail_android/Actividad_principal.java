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

public class Actividad_principal extends ActionBarActivity {

    private Button b_login;
    private Button b_nuevousuario;
    private EditText eT_usuario;
    private EditText eT_password;
    private Spinner sp_dominios;
    private String[] dominios;
    private ArrayAdapter<String> adaptador;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.layout_principal);
        Iniciar_UI();
        imprimir_dominios();
    }
    private void Iniciar_UI(){
        b_login = (Button) findViewById(R.id.b_login);
        b_nuevousuario = (Button) findViewById(R.id.b_nuevousuario);
        eT_usuario = (EditText) findViewById(R.id.eT_usuario);
        eT_password = (EditText) findViewById(R.id.eT_password);
        sp_dominios = (Spinner) findViewById(R.id.sp_dominios);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_actividad_principal, menu);
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
     public void OnIniciar(View v){
         String aux = eT_usuario.getText().toString();
         String dominio = sp_dominios.getSelectedItem().toString();
         String usuario = aux +dominio;
         String password = eT_password.getText().toString();
         String url = "http://192.168.3.3:5000/buscar_usuario";
         HashMap<String,String> parametros = new HashMap();
         parametros.put("usuario",usuario);
         parametros.put("password",password);

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
            String usuario = response.getString("usuario");
            String password = response.getString("password");
            String dominio = sp_dominios.getSelectedItem().toString();
            String usuario2 = eT_usuario.getText().toString()+dominio;
            String password2 = eT_password.getText().toString();
            if(usuario.equals(usuario2) && password.equals(password2)){
                Usuario parametro= new Usuario(usuario,password);
                Intent acceso = new Intent(Actividad_principal.this,Inicio.class);
                acceso.putExtra("Parametro",parametro);
                startActivity(acceso);
            }else{
                Toast toast = Toast.makeText(this,"El usuario o la contraseña no son correctos", Toast.LENGTH_SHORT);
                toast.show();
            }
        }catch(Exception e){
            Toast toast = Toast.makeText(this,e.getMessage(), Toast.LENGTH_SHORT);
            toast.show();
        }

    }//fin del metodo para leer los objetos json
    public void OnCrear(View v){
        Intent nuevo_layout = new Intent(Actividad_principal.this,Crear_usuario.class);
        startActivity(nuevo_layout);
    }

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
                Log.i("Error:",error.toString());
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
}//FIN DEL ACTIVITY
