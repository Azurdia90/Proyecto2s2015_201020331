package com.azurdiacristian.eddmail_android;

import android.os.Bundle;
import android.support.v7.app.ActionBarActivity;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.Spinner;


public class Actividad_principal extends ActionBarActivity {
    private Spinner sp_dominios;
    private Button b_login;
    private ArrayAdapter<String> list_dominios;
    private EDD_Get mostrar;
    private String[] dominios;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.layout_principal);
        iniciar_UI();
    }

    public void iniciar_UI(){
        sp_dominios = (Spinner) findViewById(R.id.sp_dominios);
        b_login = (Button) findViewById(R.id.b_login);
        //mostrar = new EDD_Get();
        //dominios = mostrar.imprimir_dominios();
        //list_dominios = new ArrayAdapter<String>(this,android.R.layout.simple_spinner_item,dominios);
        //sp_dominios.setAdapter(list_dominios);
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

}
