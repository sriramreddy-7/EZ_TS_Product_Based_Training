import java.awt.*;
import java.util.Scanner;

public class TwoSum {

    public static void main (String args[])
    {
        int n,i,flag=0;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the N:");
        n=sc.nextInt();
        int[] array = new int[n];
        for(i=0;i<n;i++)
        {
            array[i]=sc.nextInt();
        }
        System.out.println("Enter the Target:");
        int target=sc.nextInt();
        int start=0,end=(array.length)-1;

        for(i=0;i<n;i++)
        {
            if(array[start]+array[end]==target)
            {
                System.out.printf("%d,%d\n",start,end);
                flag=1;
                break;
            }
            else if(array[start]+array[end]<target)
            {
                start+=1;
            }
            else {
                if(array[start]+array[end]>target)
                {
                    end-=1;
                }
            }
        }
        if (flag==0)
        {
            System.out.println("Not Found !");
        }
    }
}
