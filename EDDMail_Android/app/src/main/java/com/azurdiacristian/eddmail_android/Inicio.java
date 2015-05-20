package com.azurdiacristian.eddmail_android;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.ActionBarActivity;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Spinner;
import android.widget.TextView;

import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;

import org.json.JSONObject;

import java.util.HashMap;


public class Inicio extends ActionBarActivity {
    private Usuario parametro;
    private String usuario;
    private String password;
    private TextView tV_usuario;
    private Spinner sp_categorias;

    private String[] categorias;
    private ArrayAdapter<String> adaptador;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.layout_inicio);
        iniciar_UI();
    }

    public void iniciar_UI(){
        parametro = (Usuario)getIntent().getExtras().getSerializable("Parametro");
        usuario = parametro.getUsuario();
        password = parametro.getPassword();
        tV_usuario = (TextView)findViewById(R.id.tV_usuario);
        sp_categorias = (Spinner)findViewById(R.id.sp_categorias);
        mostrar_usuario();
        imprimir_categorias();
    }
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_inicio, menu);
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
    public void mostrar_usuario(){
        tV_usuario.setText("Bienvenido: "+usuario);
    }

    public void imprimir_categorias(){
        String url = "http://192.168.3.3:5000/buscar_lista_categorias";
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
                        cargar_categorias(response);
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Log.i("Error:", error.toString());
            }
        });
        SingleTon.getInstance(getApplicationContext()).addToRequestQueue(stringRequest);
    }

    public void cargar_categorias(JSONObject response){
        try{
            String resultado = response.getString("categoria");
            categorias =  resultado.split("/");
            adaptador = new ArrayAdapter<String>(this,android.R.layout.simple_spinner_item,categorias);
            sp_categorias.setAdapter(adaptador);
        }catch(Exception e){
            Log.i("Error:",e.toString());
        }
    }//fin del metodo cargar categorias

    public void crear_categorias(View v){
        Intent nuevo = new Intent(Inicio.this,Crear_categoria.class);
        nuevo.putExtra("Parametro",parametro);
        startActivity(nuevo);
    }

}//fin de la clase del activity
