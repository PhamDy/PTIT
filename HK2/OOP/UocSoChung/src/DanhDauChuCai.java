import java.util.Scanner;

public class DanhDauChuCai {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.nextLine();
        System.out.println(s.chars().distinct().count());
    }

}
