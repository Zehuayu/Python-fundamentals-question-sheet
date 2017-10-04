#Write a program that prints the numbers from 1 to 100
# example   public static void main(String[] args){		
# 		for(int i = 1; i <= 100; i++){
# 			String test = "";
# 			test += (i % 3) == 0 ? "fizz" : "";
# 			test += (i % 5) == 0 ? "buzz" : "";
# 			System.out.println(!test.isEmpty() ? test : i);
# 		}
# 	}

for x in range(1,101):
    # Second, find all numbers fit condition 3 
    if x%3==0 and x%5==0:
        print("FizzBuzz")
    else:
        # Then, the rest numbers can just fit only one condition of 1 and 2
        if x%3==0:
            print("Fizz ")
        elif x%5==0:
            print("Buzz ")
        else:
            print(x)