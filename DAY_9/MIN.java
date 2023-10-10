import java.util.Scanner;
public class MIN {
    public  static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the N-VALUE :");
        int n=sc.nextInt();
        int i;
        int[] nums = new int[n];
        int sum=0,check=0;
        for(i=0;i<n-1;i++)
        {
            System.out.println("Enter the Num-"+(i+1)+" ");
            nums[i]=sc.nextInt();
            sum=sum+nums[i];
        }
        check=((n*(n+1))/2)-sum;
        System.out.println("Missing Number is: "+check);
    }
}
/*
N=10
arr=[1,8,4,3,5,2,6,10,9]
[1-m]
temp_array=[X,1,1,1,1,1,1,1,0,1,1,1]


 */