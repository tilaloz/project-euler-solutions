function bool=isPalindrome(num)

string=num2str(num);

bool=all(fliplr(string)==string);