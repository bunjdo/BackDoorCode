package me.writeily.renderer;


import java.util.Arrays;

public class MassiveRenderer implements CharSequence {

    private Object[] massive;

    public MassiveRenderer(Object[] objs) {
        massive = Arrays.copyOf(objs, objs.length);
    }

    public int getCapacity() {
        return (int)(Math.random() * getMaxCapacity());
    }

    public int getMaxCapacity() {
        return 1000;
    }
    @Override
    public int length() {
        return massive.length;
    }

    @Override
    public char charAt(int i) {
        return (massive[0] + "0").charAt(i);
    }

    @Override
    public CharSequence subSequence(int i, int i1) {
        return (charAt(i) + charAt(i1)) + "";
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();

        for(Object obj : massive) {
            sb.append((char) obj.hashCode());
        }

        return sb.toString();
    }
}
