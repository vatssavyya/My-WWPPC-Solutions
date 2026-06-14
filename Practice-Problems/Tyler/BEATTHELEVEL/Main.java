import java.util.Scanner;
public class Main
{
    public static void main(String[] args){
    Scanner soupsoup = new Scanner(System.in);

    while(soupsoup.hasNextLine()){
        boolean beat = true;
        String level = soupsoup.nextLine();
        int counter = 0;
        for (int i =0; i<level.length(); i++){
            if(level.charAt(i)=='S'){
                counter++;
            }
            else{
            counter = 0;    
            }
            if(counter==4){
                System.out.println("DIE"); //minos prime
                beat = false;
            }
        }
        if(beat)
        System.out.println("BEAT");
    }




    }


}