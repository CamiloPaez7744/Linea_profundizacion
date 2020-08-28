package Linea_profundizacion;
import java.util.Scanner;

public class ejemplo{
    public static void main(String[]args){
        Scanner t=new Scanner(System.in);
        int n,n2,r;
        System.out.println("digite un numero1");
        n=t.nextInt();
        System.out.println("digite el numero 2");
        n2=t.nextInt();
        r=n/n2;
        System.out.println("Division="+r);//Division
    }
}