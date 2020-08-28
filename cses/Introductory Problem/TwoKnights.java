import java.math.BigInteger;
import java.util.Scanner;

public class TwoKnights {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		StringBuilder builder = new StringBuilder();
		int number = sc.nextInt();
		sc.close();
		
//		System.out.println(result);
		for(int i =1;i<=number;i++) {
			BigInteger bInt = new BigInteger(Integer.toString(i));
			long resultPart = 4*(i-1)*(i-2);
			BigInteger result2 = new BigInteger(Long.toString(resultPart));
//			BigInteger result = ((i*i)*(i*i -1))/2 - (4*(i-1)*(i-2));
			
			BigInteger result = bInt.multiply(bInt);
			result = result.multiply((bInt.multiply(bInt)).subtract(BigInteger.ONE)).divide(BigInteger.TWO);
			result = result.subtract(result2);
			builder.append(result);
			builder.append("\n");
		}
		System.out.println(builder.toString());
		

	}

}
