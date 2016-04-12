package com.bunjlabs.mybackspace.logic;

import com.bunjlabs.fugaframework.configuration.Configuration;
import com.bunjlabs.fugaframework.dependency.Inject;
import com.bunjlabs.fugaframework.services.Service;
import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.sql2o.Connection;
import org.sql2o.Sql2o;

public class Database extends Service {

    private static final Logger log = LogManager.getLogger(Database.class);

    private Sql2o sql2o;

    @Inject
    public Configuration config;

    @Override
    public void onCreate() {
        HikariConfig hikariConfig = new HikariConfig();
        hikariConfig.setJdbcUrl(config.get("mbs.db.jdbcurl"));
        hikariConfig.setUsername(config.get("mbs.db.username"));
        hikariConfig.setPassword(config.get("mbs.db.password"));

        HikariDataSource ds = new HikariDataSource(hikariConfig);

        this.sql2o = new Sql2o(ds);
        init();
    }

    private void init() {
        String posts
                = "CREATE TABLE IF NOT EXISTS posts ("
                + "id INTEGER PRIMARY KEY AUTO_INCREMENT,"
                + "title TEXT NOT NULL,"
                + "content TEXT NOT NULL,"
                + "key VARCHAR(16) NOT NULL"
                + ")";

        try (Connection c = sql2o.open()) {
            c.createQuery(posts).executeUpdate();
        }
    }

    public Sql2o getSql2o() {
        return sql2o;
    }
}
