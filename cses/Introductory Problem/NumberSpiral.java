import java.util.Scanner;

public class NumberSpiral {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		StringBuilder builder = new StringBuilder();
		int test= sc.nextInt();

		for(int i =0; i<test;i++) {
			long a = sc.nextInt();
			long b = sc.nextInt();
			long m = Math.max(a, b);
			long result = m*(m-1) + 1 + ((long)Math.pow(-1, m))*(a-b);

			builder.append(result);
			builder.append("\n");
			}
		sc.close();
//		for(int i=0; i<test;i++) {
//			System.out.println(array[i]);
//		}
		System.out.println(builder.toString());
//			

	}

}