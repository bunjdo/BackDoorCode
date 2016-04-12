package com.bunjlabs.qrcodereader;

import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.google.zxing.integration.android.IntentIntegrator;
import com.google.zxing.integration.android.IntentResult;
import com.journeyapps.barcodescanner.CaptureActivity;

public class MainActivity extends CaptureActivity {

    private IntentIntegrator integrator;
    private Toast toast;
    private static final CharSequence MSG_BAD_BARCODE = "QR-код не опознан. Попробуйте еще раз.";
    private int state;
    private SharedPreferences prefs;
    TextView textView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button clickButton = (Button) findViewById(R.id.button);
        textView = (TextView) findViewById(R.id.textView);
        clickButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                integrator.initiateScan();
            }
        });
        toast = Toast.makeText(getApplicationContext(), MSG_BAD_BARCODE, Toast.LENGTH_SHORT);
        integrator = new IntentIntegrator(this);
        integrator.setDesiredBarcodeFormats(IntentIntegrator.QR_CODE_TYPES);
        integrator.setPrompt("Просканируйте QR-код");
        integrator.setBeepEnabled(false);
        integrator.initiateScan();
        prefs = getSharedPreferences("mystorage", MODE_APPEND);
        state = prefs.getInt("state", 0);
    }


    public void onActivityResult(int requestCode, int resultCode, Intent intent) {
        IntentResult scanResult = IntentIntegrator.parseActivityResult(requestCode, resultCode, intent);
        if (scanResult != null && scanResult.getContents() != null) {
            String result = scanResult.getContents().trim();

            if (result.length() > 3 && result.startsWith("PHD")) {
                proccessResult(result.substring(3));
            } else {
                textView.setText("Это не мой QR-код!");
            }
        } else {
            textView.setText("QR-код не опознан. Попробуйте еще раз.");
        }

    }

    String key = "UH*JSFGdgrtger%t";
    String initVector = "RV9ty*3jupcf%tHk";

    private void proccessResult(String str) {
        String decrypted = Encryptor.decrypt(key, initVector, str);
        int decryptedState = Integer.parseInt(decrypted.substring(0, 1));
        if (decryptedState > this.state) {
            textView.setText("Еще не время меня сканировать!");
            return;
        }
        if (decryptedState == this.state) {
            this.state++;
            SharedPreferences.Editor editor = prefs.edit();
            editor.putInt("state", state);
            editor.apply();
            editor.commit();
        }
        textView.setText(decrypted.substring(1));
    }

}
