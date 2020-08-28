import java.util.Scanner;

public class WeirdAlgorithm {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		long inputNumber = sc.nextLong();
		sc.close();
		while(inputNumber>=1) {
			System.out.print(inputNumber+" ");
			if(inputNumber ==1) {
				break;
			}
			else if(inputNumber%2==0) {
				inputNumber/=2;
			}
			else {
				inputNumber*=3;
				inputNumber+=1;
			}
		}
		

	}

}