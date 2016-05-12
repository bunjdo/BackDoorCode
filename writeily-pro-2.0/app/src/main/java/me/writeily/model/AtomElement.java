package me.writeily.model;

/**
 * Created by user on 12.05.16.
 */
public class AtomElement {

    private double a;

    public AtomElement(double a) {

        this.a = a;
    }

    @Override
    public int hashCode() {
        return (int)Math.round(a / Math.PI);
    }
}
