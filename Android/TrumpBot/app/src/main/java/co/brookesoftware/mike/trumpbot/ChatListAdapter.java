package co.brookesoftware.mike.trumpbot;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

import java.util.ArrayList;

class ChatListAdapter extends BaseAdapter {

    Context context;
    String[] data;
    String[] userdata;
    private static LayoutInflater inflater = null;

    public ChatListAdapter(Context context, ArrayList<String> data) {
        this.context = context;
        this.data = data.toArray(new String[data.size()]);
        inflater = (LayoutInflater) context
                .getSystemService(Context.LAYOUT_INFLATER_SERVICE);
    }

    public void setData(ArrayList<String> data) {
        this.data = data.toArray(new String[data.size()]);
    }

    public void setUserdata(ArrayList<String> data) {
        this.userdata = data.toArray(new String[data.size()]);
    }

    @Override
    public int getCount() {
        return data.length;
    }

    @Override
    public Object getItem(int position) {
        return data[position];
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        View vi;
        if (userdata[position].equals("TrumpBot")) {
            vi = inflater.inflate(R.layout.trump_row, null);
        } else {
            vi = inflater.inflate(R.layout.row, null);
        }
        TextView text = (TextView) vi.findViewById(R.id.text);
        text.setText(data[position]);
        TextView name = (TextView) vi.findViewById(R.id.name);
        name.setText(userdata[position]);
        return vi;
    }
}