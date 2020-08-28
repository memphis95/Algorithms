import java.util.Scanner;

public class Permutations {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		StringBuilder builder = new StringBuilder();
		int number = sc.nextInt();
		sc.close();
		if(number==1){
            System.out.println("1");
        }
		else if(number<4) {
			System.out.println("NO SOLUTION");
		} else if (number==4) {
			System.out.println("3 1 4 2");
		}else {
			for(int i=2;i<=number;i+=2) {
				builder.append(i);
				builder.append(' ');
			}
			for(int i=1;i<=number;i+=2) {
				builder.append(i);
				builder.append(' ');
			}
			System.out.println(builder.toString());
			
		}
		
	}

}
