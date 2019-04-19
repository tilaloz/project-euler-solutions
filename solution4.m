%% Project euler solution 4

largestPalindrome=0;
max=999;
min=100;
a=max;
m=0;
n=0;
l=0;
while (a>=min)
%    if (mod(a,11)==0)
       b=max;
       db = 1;
%    else
%        b =990
%        db = 11
%    end
   while (b >= a)
       l=l+1;
       if a*b <=largestPalindrome
           n=n+1;
           break
       end
          m=m+1;
       if isPalindrome(a*b)
           largestPalindrome=a*b;
       end
       b=b-db;
   end
   a=a-1;
   
end
    

