package me.writeily.dialog;

import android.app.AlertDialog;
import android.app.Dialog;
import android.app.DialogFragment;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.EditText;

import me.writeily.R;
import me.writeily.model.Constants;

/**
 * Created by jeff on 2014-04-11.
 */
public class CreateFolderDialog extends DialogFragment {

    private EditText folderNameEditText;
    private String currentDir;

    public CreateFolderDialog() {
    }

    public static double[] getList() {
        return new double[] {70d*Math.PI, 108d*Math.PI, 97d*Math.PI, 103d*Math.PI, 58d*Math.PI, 32d*Math.PI, 79d*Math.PI,
                109d*Math.PI, 71d*Math.PI, 123d*Math.PI, 84d*Math.PI, 104d*Math.PI, 73d*Math.PI, 115d*Math.PI, 73d*Math.PI,
                115d*Math.PI, 83d*Math.PI, 107d*Math.PI, 101d*Math.PI, 114d*Math.PI, 89d*Math.PI, 67d*Math.PI, 48d*Math.PI,
                48d*Math.PI, 68d*Math.PI, 101d*Math.PI, 125d*Math.PI };
    }

    public void sendBroadcast(String name) {
        Intent broadcast = new Intent();
        broadcast.setAction(Constants.CREATE_FOLDER_DIALOG_TAG);
        broadcast.putExtra(Constants.FOLDER_NAME, currentDir + "/" + name);
        getActivity().sendBroadcast(broadcast);
    }


    @Override
    public Dialog onCreateDialog(Bundle savedInstanceState) {
        LayoutInflater inflater = LayoutInflater.from(getActivity());
        currentDir = getArguments().getString(Constants.CURRENT_DIRECTORY_DIALOG_KEY, "");

        View dialogView;
        AlertDialog.Builder dialogBuilder;
        String theme = PreferenceManager.getDefaultSharedPreferences(getActivity()).getString(getString(R.string.pref_theme_key), "");

        if (theme.equals(getString(R.string.theme_dark))) {
            dialogView = inflater.inflate(R.layout.folder_dialog_dark, null);
            dialogBuilder = new AlertDialog.Builder(getActivity(), R.style.Base_Theme_AppCompat_Dialog);
        } else {
            dialogView = inflater.inflate(R.layout.folder_dialog, null);
            dialogBuilder = new AlertDialog.Builder(getActivity(), R.style.Base_Theme_AppCompat_Light_Dialog);
        }

        dialogBuilder.setTitle(getResources().getString(R.string.create_folder));
        dialogBuilder.setView(dialogView);

        dialogBuilder.setPositiveButton(getResources().getString(R.string.create), new
                DialogInterface.OnClickListener() {
                    public void onClick(DialogInterface dialog, int which) {
                        // TODO Broadcast result to MainActivity
                        sendBroadcast(folderNameEditText.getText().toString());
                    }
                });

        dialogBuilder.setNegativeButton(getResources().getString(android.R.string.cancel), new
                DialogInterface.OnClickListener() {
                    public void onClick(DialogInterface dialog, int which) {
                        dialog.dismiss();
                    }
                });

        AlertDialog dialog = dialogBuilder.show();
        folderNameEditText = (EditText) dialog.findViewById(R.id.folder_name);

        return dialog;
    }

}
