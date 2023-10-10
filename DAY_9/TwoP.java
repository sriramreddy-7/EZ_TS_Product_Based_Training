import java.util.*;
class TwoP
{
 public static void main(String args[])
    {
        int n;
        Scanner sc = new Scanner(System.in);
        n=sc.nextInt();
        int[] arr = new int[n];
        int i;
        for(i=0;i<n;i++)
        {
            arr[i]=sc.nextInt();
        }
        System.out.println("Enter the Target");
        int target=sc.nextInt();
        int start=0,end=(arr.length)-1;
        for(i=0;i<n;i++)
        {
            if (arr[start]+arr[end]>target)
            {
                end=end-1;
            }
            else if(arr[start]+arr[end]<target)
            {
                start=start+1;
            }
            else
            {
               if(arr[start]+arr[end]==target)
               {
                System.out.printf("%d"+"%d",start+1,end+1);
                break;
               }
            }
        }


    
    }
}