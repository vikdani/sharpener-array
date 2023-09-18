
  ''' int arr[]=new int[n];
        int counter=0;
        int x=2;
        while(counter<n)
        {
            boolean prime=true;
            for(int j=2; j<x; j++)
            {
                if (x%j==0)
                {
                    prime=false;
                    break;
                }    
            }
            if(prime)
                {
                    arr[counter]=x;
                    counter=counter+1;
                }
            x=x+1;
        }
        return arr'''
        

        