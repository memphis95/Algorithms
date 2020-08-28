import java.util.Scanner;

public class TwoKnights1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		long n = sc.nextLong();
		sc.close();
		long i;
		long p, k , ans;
		for(i=1;i<=n;i++) {
			k = i*i;
			p = k*(k-1)/2;
			ans = p - 4*(i-1)*(i-2);
			System.out.println(ans);
			
		}
		

	}

}