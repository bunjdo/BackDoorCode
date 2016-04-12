package com.bunjlabs.mybackspace.logic;

import java.util.List;
import org.sql2o.Connection;

public class Post {

    private long id;
    private String title;
    private String content;
    private String key;

    public long getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public String getContent() {
        return content;
    }

    public String getKey() {
        return key;
    }

    public void setId(long id) {
        this.id = id;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public static List<Post> select(Database db, String key) {
        String sql = "SELECT * FROM posts WHERE key = :key";

        try (Connection con = db.getSql2o().open()) {
            return con.createQuery(sql).addParameter("key", key).executeAndFetch(Post.class);
        }
    }

    public void save(Database db) {
        String sql = "INSERT INTO posts VALUES ("
                + "NULL, :title, :content, :key"
                + ")";

        try (Connection con = db.getSql2o().open()) {
            con.createQuery(sql).bind(this).executeUpdate();
        }
    }
}
