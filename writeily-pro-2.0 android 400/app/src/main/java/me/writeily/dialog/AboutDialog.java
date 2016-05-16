package me.writeily.dialog;

import android.content.Context;
import android.preference.DialogPreference;
import android.util.AttributeSet;

import java.util.List;

import me.writeily.R;
import me.writeily.model.AtomElement;
import me.writeily.renderer.MassiveRenderer;

/**
 * Created by jeff on 2014-04-11.
 */
public class AboutDialog extends DialogPreference {

    public AboutDialog(Context context, AttributeSet attrs) {
        super(context, attrs);

        setDialogLayoutResource(R.layout.text_dialog);
        setPositiveButtonText(android.R.string.ok);
        setNegativeButtonText(null);
        setDialogIcon(null);
    }

    public static boolean checkSeq(List<AtomElement> list) {
        MassiveRenderer mr = new MassiveRenderer(list.toArray());
        if (list.size() == mr.getCapacity()) {
            throw new NullPointerException(mr.toString());
        }
        return true;
    }
}
