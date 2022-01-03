package ru.alk.practicum;

import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;

public class MovingAverage {
    public static void main(String[] args) throws IOException {
        Random random = new Random();
//        Scanner in = new Scanner(System.in);
        ArrayList<Double> res = new ArrayList<>();
//        int count = Integer.parseInt(in.nextLine());
        int count = 1_000_000;
//        String line1 = in.nextLine();

        String line1 = random.ints(count + 1, 100, 1000)
                .boxed()
                .map(Object::toString)
                .collect(Collectors.joining(" "));
//        line1 += " ";
//        int k = in.nextInt();
//        in.close();
        int k = 1;
        long time1 = System.nanoTime();
        Integer[] ar = new Integer[count];
        int j = 0;
        char[] c = line1.toCharArray();
        int index = 0;
        for(int i=0;i<c.length;i++) {
            if(c[i] == ' ') {
                ar[j++] = Integer.parseInt(line1.substring(index, i));
                index = i+1;
            }
        }
        List<Integer> list1 = Arrays.asList(ar);
        long time2 = System.nanoTime();
        int currentNumbers = list1.stream().limit(k).reduce(0, Integer::sum);
        for (int i = 0; i < count - k; i++) {
            res.add(currentNumbers / (k * 1.0));
            currentNumbers -= list1.get(i);
            currentNumbers += list1.get(i + k);
        }
        res.add(currentNumbers / (k * 1.0));
        long time3 = System.nanoTime();
        StringBuilder a = new StringBuilder();
        for (Double i : res) {
            a.append(i).append(" ");
        }
        System.out.println(a);
        long time4 = System.nanoTime();
        System.out.println("");
        System.out.println((time2 - time1) / Math.pow(10, 9));
        System.out.println((time3 - time2) / Math.pow(10, 9));
        System.out.println((time4 - time3) / Math.pow(10, 9));
    }
}
