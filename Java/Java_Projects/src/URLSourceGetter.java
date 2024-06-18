import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.net.*;

public class URLSourceGetter extends Frame implements ActionListener {
    TextField tf;
    TextArea ta;
    Button b;
    Label l;
    

    URLSourceGetter() {
        super("Source Getter Tool - BY ANJALI");
        l = new Label("Enter URL:");
        l.setBounds(30, 50, 70, 20);

        tf = new TextField();
        tf.setBounds(120, 50, 250, 20);

        b = new Button("Get Source");
        b.setBounds(120, 100, 120, 30);
        b.addActionListener(this);

        ta = new TextArea();
        ta.setBounds(30, 150, 340, 200);

        add(l);
        add(tf);
        add(b);
        add(ta);
        setSize(400, 400);
        setLayout(null);
        setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
        String urlStr = tf.getText();
        if (urlStr != null && !urlStr.isEmpty()) {
            try {
                // Check if the URL contains a protocol, if not, add "http://"
                if (!urlStr.startsWith("http://") && !urlStr.startsWith("https://")) {
                    urlStr = "http://" + urlStr;
                }

                URL url = new URL(urlStr);
                HttpURLConnection connection = (HttpURLConnection) url.openConnection();

                InputStream is = connection.getInputStream();
                InputStreamReader isr = new InputStreamReader(is);
                BufferedReader br = new BufferedReader(isr);
                StringBuilder sb = new StringBuilder();

                String line;
                while ((line = br.readLine()) != null) {
                    sb.append(line).append("\n");
                }
                br.close();

                String source = sb.toString();
                ta.setText(source);
            } catch (Exception ex) {
                System.err.println(ex);
            }
        }
    }

    public static void main(String[] args) {
        new URLSourceGetter();
    }
}
