import java.util.Scanner;

public class IncreasingArray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int arrayLength = sc.nextInt();

		int previousNumber = sc.nextInt();
		int currentNumber = 0;
		long turn =0;
		for(int i=1; i<arrayLength;i++) {
			currentNumber = sc.nextInt();
//			System.out.println("hello");
//			System.out.println(previousNumber+" "+ currentNumber);
			if(currentNumber<previousNumber) {
				turn += previousNumber - currentNumber;
				continue;
			}
			previousNumber = currentNumber;
			
		}
		sc.close();
		System.out.println(turn);

	}
		
	}
