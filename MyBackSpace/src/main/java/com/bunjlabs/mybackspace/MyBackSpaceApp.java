package com.bunjlabs.mybackspace;

import com.bunjlabs.fugaframework.FugaApp;
import com.bunjlabs.mybackspace.logic.Database;


public class MyBackSpaceApp extends FugaApp {
    
    public static void main(String[] args) throws Exception {
        new MyBackSpaceApp().start();
    }

    @Override
    public void prepare() {
        getRouter().load("routes/default.routes");
        getConfiguration().load("configs/default.conf");
        
        getServiceManager().registerService(Database.class);
    }
    
}
