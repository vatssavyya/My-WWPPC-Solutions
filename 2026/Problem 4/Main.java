import java.util.Scanner;
public class Main
{
    public static void main(String[] args){
    Scanner soupsoup = new Scanner(System.in);

    int cases = soupsoup.nextInt();
    for(int j = 0; j<cases; j++){
        int plants = soupsoup.nextInt();
            int tallPlant = 0;
            int total = 0;
            for  (int i = 0; i<plants; i++){
                int currentPlant = soupsoup.nextInt();
                total += currentPlant;
                if (currentPlant > tallPlant){
                tallPlant = currentPlant;
                }
            }
            if((plants*tallPlant-total)%2==0){
                System.out.println("YES");
            }
            else{
                System.out.println("NO");
            }
            
        }

    }
   
}

