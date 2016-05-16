package com.bunjlabs.mybackspace;

import com.bunjlabs.fugaframework.dependency.Inject;
import com.bunjlabs.fugaframework.foundation.Controller;
import com.bunjlabs.fugaframework.foundation.Response;
import com.bunjlabs.fugaframework.templates.TemplateNotFoundException;
import com.bunjlabs.fugaframework.templates.TemplateRenderException;
import com.bunjlabs.mybackspace.logic.Database;
import com.bunjlabs.mybackspace.logic.Post;
import java.nio.charset.Charset;
import java.util.List;
import org.json.JSONObject;

public class MainController extends Controller {

    @Inject
    public Database db;

    public Response index(String key) throws TemplateNotFoundException, TemplateRenderException {

        List<Post> posts = Post.select(db, key);

        ctx.put("posts", posts);
        ctx.put("key", key);
        return ok(view("index.html"));
    }

    public Response add(String key) throws TemplateNotFoundException, TemplateRenderException {
        ctx.put("key", key);

        return ok(view("add.html"));
    }

    public Response addProcess(String key) throws TemplateNotFoundException, TemplateRenderException {
        ctx.put("key", key);

        JSONObject json = new JSONObject(ctx.getRequest().getContent().toString(Charset.forName("UTF-8")));

        Post post = new Post();

        post.setTitle(json.getString("title"));
        post.setContent(json.getString("content").replaceAll("\\</?(.*)script(.*)/?\\>", ""));
        post.setKey(key);

        post.save(db);

        return ok(new JSONObject().put("status", "ok").put("url", urls.that(key, "")).toString()).asJson();
    }

}
