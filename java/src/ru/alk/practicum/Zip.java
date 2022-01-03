package ru.alk.practicum;

import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Zip {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int count = Integer.parseInt(in.nextLine());
        String line1 = in.nextLine();
        String line2 = in.nextLine();
//        String a = "1 4 6 7";
//        System.out.println("");
        List<String> list1 = Arrays.asList(line1.split(" "));
        List<String> list2 = Arrays.asList(line2.split(" "));

        for (int i = 0; i < count; i++) {
            System.out.print(list1.get(i) + " " + list2.get(i) + " ");
        }
    }
}
