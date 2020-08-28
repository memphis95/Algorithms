import java.util.Scanner;

public class MissingNumber {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		long number = sc.nextInt();
//		long numberArray[] = new long[number];
		long sum =0;
		for(long i=0;i<number-1;i++) {
//			numberArray[i]= sc.nextLong();
			sum += sc.nextInt();
		}
		long difference = (number*(number+1))/2 - sum;
		sc.close();
		System.out.println(difference);
		
		
		
	}

}
