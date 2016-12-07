package co.brookesoftware.mike.trumpbot;

import android.app.AlertDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import com.android.volley.*;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import java.net.InetAddress;
import java.util.ArrayList;

public class ActivityChat extends AppCompatActivity {

    EditText txtMessage;
    Button btnSend;
    ListView lstMessages;
    ArrayList<String> messages;
    ArrayList<String> senders;
    ChatListAdapter chatListAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.app_bar_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        // Please don't judge our code - we were in a rush!

        messages = new ArrayList<>();
        senders = new ArrayList<>();
        chatListAdapter = new ChatListAdapter(this, messages);
        txtMessage = (EditText) findViewById(R.id.txtMessage);
        btnSend = (Button) findViewById(R.id.btnSend);
        lstMessages = (ListView) findViewById(R.id.lstMessages);

        lstMessages.setAdapter(chatListAdapter);

        btnSend.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                final String message = txtMessage.getText().toString();
                txtMessage.getText().clear();
                if (!message.trim().isEmpty()) {
                    addMessageToList(getString(R.string.You), message);

                    RequestQueue queue = Volley.newRequestQueue(getApplicationContext());
                    String url = "https://trumpedupkicks.herokuapp.com/response";
                    String uri = String.format("%1$s?q=%2$s", url, message);
                    StringRequest stringRequest = new StringRequest(Request.Method.GET, uri,
                            new Response.Listener<String>() {
                                @Override
                                public void onResponse(String response) {
                                    addMessageToList(getString(R.string.app_name), response);
                                }
                            }, new Response.ErrorListener() {
                        @Override
                        public void onErrorResponse(VolleyError error) {
                            addMessageToList(getString(R.string.app_name), "WROOONG!\n\n" +
                                    "Seriously though, this is an error message." +
                                    "Are you sure you're connected to the internet?");
                        }
                    });
                    queue.add(stringRequest);
                }
            }
        });
    }

    @Override
    protected void onStart() {
        super.onStart();
        if (!isNetworkAvailable()) {
            new AlertDialog.Builder(ActivityChat.this)
                    .setTitle("No Internet")
                    .setMessage("We couldn't find an active internet connection. " +
                            "Please double check your connection and try again!")
                    .setPositiveButton(android.R.string.ok, new DialogInterface.OnClickListener() {
                        public void onClick(DialogInterface dialog, int which) {
                            finish();
                        }
                    })
                    .setIcon(android.R.drawable.ic_dialog_alert)
                    .show();
        }
    }

    private void addMessageToList(String sender, String message) {
        senders.add(sender);
        messages.add(message);
        chatListAdapter.setUserdata(senders);
        chatListAdapter.setData(messages);
        chatListAdapter.notifyDataSetChanged();
        lstMessages.setSelection(chatListAdapter.getCount() - 1);
    }

    private boolean isNetworkAvailable() {
        ConnectivityManager connectivityManager
                = (ConnectivityManager) getSystemService(Context.CONNECTIVITY_SERVICE);
        NetworkInfo activeNetworkInfo = connectivityManager.getActiveNetworkInfo();
        return activeNetworkInfo != null && activeNetworkInfo.isConnected();
    }

    public void showShortToast(String msg) {
        Toast toast = Toast.makeText(getApplicationContext(), msg, Toast.LENGTH_SHORT);
        toast.show();
    }

    public void showLongToast(String msg) {
        Toast toast = Toast.makeText(getApplicationContext(), msg, Toast.LENGTH_LONG);
        toast.show();
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_activity_chat, menu);
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
            Intent intent = new Intent(this, SettingsActivity.class);
            startActivity(intent);
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
