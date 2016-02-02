package com.bunjlabs;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

public class LetsObfuscate {

    private final static String YOUWIN = "You win";
    private final static String HASHALG = "SHA1";

    private static void load() throws InterruptedException {
        System.out.print('.');
        Thread.sleep(500);
    }

    private static boolean verify(String pass) {
        System.out.println("Sorry, I fogot to say - I'm very lasy so I don't wahna check your pass. I don't know you. You are definetly giving me wrong one.");
        return pass.isEmpty();
    }

    public static void main(String[] args) throws InterruptedException, NoSuchAlgorithmException {
        for (int i = 0; i < 3; i++) {
            load();
        }
        System.out.println("\nWelcome to my brand new java application!");
        System.out.println("I'll ask you password, you'll give it to me and that's it! No cheating, no confusion, no sense.");
        System.out.println("Please enter the pass:");
        Scanner sc = new Scanner(System.in);
        String pass = sc.nextLine();
        pass += "1";
        if (verify(pass)) {
            System.out.println(ok(YOUWIN));
        }
    }

    private static String ok(String input) throws NoSuchAlgorithmException {
        MessageDigest mDigest = MessageDigest.getInstance(HASHALG);
        byte[] result = mDigest.digest(input.getBytes());
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < result.length; i++) {
            sb.append(Integer.toString((result[i] & 0xff) + 0x100, 16).substring(1));
        }
        System.out.print("The key is: ");
        return sb.toString();
    }

}
