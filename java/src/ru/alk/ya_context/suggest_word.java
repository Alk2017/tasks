package ru.alk.ya_context;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Scanner;

public class suggest_word {
    static final String CORRECT = "correct";
    static final String ABSENT = "absent";
    static final String PRESENT = "present";
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        char[] key = in.nextLine().toCharArray();
        char[] attempt = in.nextLine().toCharArray();
        ArrayList<String> answers = new ArrayList<>(Collections.nCopies(key.length, ""));
        HashMap<Character, ArrayList<Integer>> keyAsMap = new HashMap<>();
        for (int i = 0; i < key.length; i++) {
            if (keyAsMap.containsKey(key[i])) {
                keyAsMap.get(key[i]).add(i);
            } else {
                keyAsMap.put(key[i], new ArrayList<>(Collections.singletonList(i)));
            }
        }

        for (int i = 0; i < attempt.length; i++) {
            if (answers.get(i).equals("")) {
                if (!keyAsMap.containsKey(attempt[i])) {
                    answers.set(i, ABSENT);
                } else if (attempt[i] == key[i]) {
                    answers.set(i, CORRECT);
                    keyAsMap.get(attempt[i]).removeAll(Collections.singletonList(i));
                } else {
                    if (keyAsMap.get(attempt[i]).isEmpty()) {
                        answers.set(i, ABSENT);
                    } else {
                        checkPresentOrAbsent(key, attempt, keyAsMap, i, answers);
                    }
                }
            }

        }
    }

    private static void checkPresentOrAbsent(char[] k, char[] a, HashMap<Character, ArrayList<Integer>> kAM, int in, ArrayList<String> answs) {
        for (int f_i:kAM.get(a[in])) {
            if (a[f_i] != k[f_i]) {
                answs.set(in, PRESENT);
                kAM.get(a[in]).removeAll(Collections.singletonList(f_i));
                return;
            } else {
                answs.set(f_i, CORRECT);
                kAM.get(a[in]).removeAll(Collections.singletonList(f_i));
            }
        }
        answs.set(in, ABSENT);
    }
}
