import java.lang.annotation.Target;
import java.util.Scanner;

public class ThreePointer {
    public static void main(String args[])
    {
        int n,i,flag=0;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the N:");
        n=sc.nextInt();
        int[] array = new int[n];
        System.out.println("Enter the Array Elements:");
        for(i=0;i<n;i++)
        {
            array[i] = sc.nextInt();
        }
        System.out.println("Enter the Target:");
        int target=sc.nextInt();
        int start,next,end;
        for(start=0;start<n;start++)
        {
            next=start+1;
            end=n-1;
            while (next<end)
            {
                if(array[start]+array[next]+array[end]== target)
                {

                    System.out.printf("%d,%d,%d\n",array[start],array[next],array[end]);
                    flag=1;
                    break;
                }
                else if (array[start]+array[next]+array[end]>target)
                {
                    end=end-1;
                }
                else
                {
                    if (array[start]+array[next]+array[end]<target)
                    {
                        next=next+1;
                    }

                }
            }
        }
        if (flag==0)
        {
            System.out.println("Not Found !");
        }
    }
}
