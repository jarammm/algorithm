import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
        // 입력 받기
		Scanner sc = new Scanner(System.in);
	
		int n = sc.nextInt();
		int k = sc.nextInt();
		
		int[] temp = new int [n];
		for ( int i=0; i<n; i++) {
			temp[i] = sc.nextInt();
		}
		sc.close();
        
        // num, ans base case 생성
        int num = 0;
		for ( int i=0; i<k; i++) {
			num += temp[i];
		}
        int ans = num;

        // 최대 누적합 구하기
		for ( int i=0; i<n-k; i++) {
			num = num - temp[i] + temp[i+k];
			if (num > ans){
                ans = num;
            }
		}
		
		System.out.println(ans);
	}
}