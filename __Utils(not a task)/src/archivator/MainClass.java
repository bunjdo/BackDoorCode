package archivator;

public class MainClass {

    static String key = "UH*JSFGdgrtger%t";
    static String initVector = "RV9ty*3jupcf%tHk";

    public static void main(String[] args) {
        //System.out.println(SimpleEncryptor.obfuscate("DvCTF{1mSkndF1H}"));
        //System.out.println(SimpleEncryptor.unobfuscate("ImmaloginOneoNE01rfhtsdfvsr"));
        //System.out.println(SimpleEncryptor.obfuscate("1mmapaSsfordl0katMeeeee"));
        System.out.println("PHD" + Encryptor.encrypt(key, initVector, "0Did you noticed that we have TVs with slides?"));
        System.out.println("PHD" + Encryptor.encrypt(key, initVector, "1Wanna cook? There is kitchen ower there."));
        System.out.println("PHD" + Encryptor.encrypt(key, initVector, "2Do you know that organizers are responsible even for toilet paper and paper towels? How much towels did you used today? Lets count it."));
        System.out.println("PHD" + Encryptor.encrypt(key, initVector, "3Organizers are hiding you flag. But who? Ask them all! Password is 'Are you selling slavic wardrobe?'"));
        System.out.println("PHD" + Encryptor.encrypt(key, initVector, "4Good job! Your key is DvCTF{ImmaSherl0ckH0lmes}"));
    }

}
