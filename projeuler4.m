%% Project Euler

n=0;
m=0;
for C=999*999:-1:10000
    for x=ceil(sqrt(C)):999
        m=m+1;
        if mod(C,x)==0
            n=n+1;
            if isPalindrome(C)
            C
            return
            end
        end
    end
    
end