package com.azurdiacristian.eddmail_android;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.ActionBarActivity;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;

import org.json.JSONObject;

import java.util.HashMap;


public class Crear_categoria extends ActionBarActivity {

    private EditText eT_entrada;
    private Button b_ingresar;
    private Usuario sesion;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.layout_crear_categoria);
        iniciar_UI();
    }

    public void iniciar_UI(){
        sesion = (Usuario)getIntent().getExtras().getSerializable("Parametro");
        eT_entrada = (EditText) findViewById(R.id.eT_categoria);
        b_ingresar = (Button) findViewById(R.id.b_insertar);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_crear_categoria, menu);
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
    public void insertar_categoria(View v){
        String url = "http://192.168.3.3:5000/insertar_categoria";
        HashMap<String,String> parametros = new HashMap();
        parametros.put("usuario",sesion.getUsuario());
        parametros.put("password",sesion.getPassword());
        parametros.put("categoria",eT_entrada.getText().toString());

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
            Intent regresar = new Intent(this,Inicio.class);
            startActivity(regresar);
        }catch(Exception e){
            Toast toast = Toast.makeText(this,e.getMessage(), Toast.LENGTH_SHORT);
            toast.show();
        }
    }//fin del metodo para leer los objetos json
}
