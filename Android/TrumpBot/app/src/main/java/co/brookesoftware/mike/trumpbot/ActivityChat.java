package co.brookesoftware.mike.trumpbot;

import android.content.Intent;
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

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
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
                    String url = "http://www.google.com";
                    String uri = String.format("%1$s?q=%2$s",
                            url,
                            message);
                    StringRequest stringRequest = new StringRequest(Request.Method.GET, uri,
                            new Response.Listener<String>() {
                                @Override
                                public void onResponse(String response) {
                                    addMessageToList("TrumpBot", response);
                                }
                            }, new Response.ErrorListener() {
                        @Override
                        public void onErrorResponse(VolleyError error) {
                            addMessageToList("TrumpBot", "I'm broken! That didn't work!");
                        }
                    });
                    //queue.add(stringRequest);
                }

                addMessageToList(getString(R.string.app_name), "WROOONG!");
            }
        });
    }

    private void addMessageToList(String sender, String message) {
        senders.add(sender);
        messages.add(message);
        chatListAdapter.setUserdata(senders);
        chatListAdapter.setData(messages);
        chatListAdapter.notifyDataSetChanged();
        lstMessages.setSelection(chatListAdapter.getCount() - 1);
    }

    private void showShortToast(String msg) {
        Toast toast = Toast.makeText(this, msg, Toast.LENGTH_SHORT);
        toast.show();
    }

    private void showLongToast(String msg) {
        Toast toast = Toast.makeText(this, msg, Toast.LENGTH_LONG);
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
