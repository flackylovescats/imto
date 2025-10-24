import java.util.Random;

public class Main {
    public static void main(String[] args) {
        short[] w = new short[8];
        double[] x = new double[20];
        double[][] l = new double[8][20];
        Random r = new Random();

        for (int i = 0; i < 8; i++) {
            w[i] = (short) (i * 2 + 7);
        }

        for (int i = 0; i < 20; i++) {
            x[i] = -6.0 + r.nextDouble() * (5.0 + 6.0);
        }

        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 20; j++) {
                if (w[i] == 11) {
                    l[i][j] = Math.cbrt(Math.sin(Math.exp(x[j])));
                } else if (w[i] == 9 || w[i] == 15 || w[i] == 17 || w[i] == 21) {
                    l[i][j] = Math.sin(Math.pow((1.0 / 3.0) / Math.pow((1.0 / 4.0) + x[j], x[j]), 3));
                } else {
                    l[i][j] = Math.exp((2.0 / 3.0) / (1 + (Math.pow(Math.pow(x[j], 2 * x[j]), (3.0 / 4.0) * (Math.sin(x[j]) + Math.PI)))));
                }
            }
        }

        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 20; j++) {
                System.out.printf("%.4f ", l[i][j]);
            }
            System.out.println();
        }
    }
}