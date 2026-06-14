import java.util.Scanner;
public class Main
{
    public static void main(String[] args){
    Scanner soupsoup = new Scanner(System.in);

    int cases = soupsoup.nextInt();
    for(int i = 0; i<cases; i++){
        int d = -soupsoup.nextInt();
        int c = -soupsoup.nextInt();
        if(c<0){
            c=0;
        }
        if(d<0){
            d=-d;
        }
        System.out.println(c+" "+d);
    }





    }


}