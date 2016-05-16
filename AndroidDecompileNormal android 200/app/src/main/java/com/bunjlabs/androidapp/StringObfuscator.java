package com.bunjlabs.androidapp;


public class StringObfuscator {

    private static String source="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789{}";
    private static String target="Q9oA8sZxnfWS7Xbj{EDCr6eRyFqmVwT5GBYks4zHhaNtU3J2}MdI1igKuOpl0LPv";


    public static String obfuscate(String s) {
        char[] result= new char[s.length()];
        for (int i=0;i<s.length();i++) {
            char c=s.charAt(i);
            int index=source.indexOf(c);
            result[i]=target.charAt(index);
        }

        return new String(result);
    }

    public static String unobfuscate(String s) {
        char[] result= new char[s.length()];
        for (int i=0;i<s.length();i++) {
            char c=s.charAt(i);
            int index=target.indexOf(c);
            result[i]=source.charAt(index);
        }

        return new String(result);
    }

}
