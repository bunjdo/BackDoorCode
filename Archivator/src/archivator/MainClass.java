package archivator;


public class MainClass {

    static String key = "UH*JSFGdgrtger%t";
    static String initVector = "RV9ty*3jupcf%tHk";
    
    public static void main(String[] args) {
        System.out.println("PHD" + Encryptor.encrypt(key, initVector, "0test0"));
        System.out.println("PHD" + Encryptor.encrypt(key, initVector, "1test1"));
        System.out.println("PHD" + Encryptor.encrypt(key, initVector, "2flag"));
    }
    
}