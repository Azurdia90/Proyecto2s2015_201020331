package com.azurdiacristian.eddmail_android;

import android.content.Context;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.toolbox.Volley;

/**
 * Created by Cristian on 07/05/2015.
 */
public final class SingleTon {

    private static SingleTon singleton;
    private static RequestQueue request;
    private static Context context;

    private SingleTon(Context contexto){
        SingleTon.context = contexto;
        request = getRequestQueue();
    }

    public static synchronized SingleTon getInstance(Context context) {
        if (singleton == null) {
            singleton = new SingleTon(context);
        }
        return singleton;
    }

    public RequestQueue getRequestQueue() {
        if (request == null) {
            request = Volley.newRequestQueue(context.getApplicationContext());
        }
        return request;
    }

    public  void addToRequestQueue(Request req) {
        getRequestQueue().add(req);
    }

}
