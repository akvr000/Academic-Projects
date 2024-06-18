import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.HashMap;
import java.util.Map;

public class CurrencyConverter extends JFrame {
    private JTextField amountField, resultField;
    private JComboBox<String> sourceCurrencyComboBox, targetCurrencyComboBox;
    private JButton convertButton;

    private final Map<String, Double> exchangeRates;

    public CurrencyConverter() {
        setTitle("Currency Converter - BY ANJALI");
        setSize(400, 200);
        Image imageIcon = Toolkit.getDefaultToolkit().getImage("images/calculator_icon.png");
        setIconImage(imageIcon);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());

        // Predefined exchange rates
        exchangeRates = new HashMap<>();
        exchangeRates.put("USD", 1.0);
        exchangeRates.put("EUR", 0.92);
        exchangeRates.put("GBP", 0.79);
        exchangeRates.put("INR", 83.31); // 1 USD = 83.31 INR
        exchangeRates.put("JPY", 151.92); // 1 USD = 151.92 JPY
        exchangeRates.put("CAD", 1.36); // 1 USD = 1.36 CAD

        // Create components
        JLabel amountLabel = new JLabel("Amount:");
        amountField = new JTextField(10);
        JLabel fromLabel = new JLabel("From:");
        sourceCurrencyComboBox = new JComboBox<>(exchangeRates.keySet().toArray(new String[0]));
        JLabel toLabel = new JLabel("To:");
        targetCurrencyComboBox = new JComboBox<>(exchangeRates.keySet().toArray(new String[0]));
        convertButton = new JButton("Convert");
        JLabel resultLabel = new JLabel("Result:");
        resultField = new JTextField(10);
        resultField.setEditable(false);

        // Set default selection
        sourceCurrencyComboBox.setSelectedItem("USD");
        targetCurrencyComboBox.setSelectedItem("INR");

        // Add components to the frame
        add(amountLabel);
        add(amountField);
        add(fromLabel);
        add(sourceCurrencyComboBox);
        add(toLabel);
        add(targetCurrencyComboBox);
        add(convertButton);
        add(resultLabel);
        add(resultField);

        // Add action listener to the button
        convertButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                convertCurrency();
            }
        });

        setVisible(true);
    }

    private void convertCurrency() {
        try {
            String sourceCurrency = (String) sourceCurrencyComboBox.getSelectedItem();
            String targetCurrency = (String) targetCurrencyComboBox.getSelectedItem();
            double amount = Double.parseDouble(amountField.getText());

            double sourceRate = exchangeRates.get(sourceCurrency);
            double targetRate = exchangeRates.get(targetCurrency);

            // Perform conversion
            double result = (amount / sourceRate) * targetRate;
            resultField.setText(String.format("%.2f", result));
        } catch (Exception ex) {
            JOptionPane.showMessageDialog(this, "Error: " + ex.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                new CurrencyConverter();
            }
        });
    }
}
