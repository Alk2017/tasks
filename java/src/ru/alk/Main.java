package ru.alk;

public class Main {
    interface Foo {
        int i = 10;
    }
    public static void main(String[] args) {
        Foo.i = 20;
        System.out.println("Hello");
    }
}
