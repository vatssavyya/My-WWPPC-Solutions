import java.util.Scanner;
public class Main
{
    public static void main(String[] args){
    Scanner soupsoup = new Scanner(System.in);
    String output = "";
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
                output+="YES"+"\n";
            }
            else{
                output+="NO"+"\n";
            }

        }
    System.out.println(output);
    }
   
}
// basically just take the largest plant, find the difference between if all plants were that height and subtract that from the current total height. if that's divisible by 2 yes if not than no
