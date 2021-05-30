def deci_to_any_string(n, radix):
  if n<=0 or radix<2 or radix>16:
    print("Wrong Input!!!")
  
  else:
    remain_list=[]

    quotient = n
    while quotient>radix:
      remain = quotient % radix
      quotient = quotient//radix
      remain_list.append(str(remain))

    remain_list.append(str(quotient%radix))
    remain_list.append(str(quotient//radix))
    remain_list.reverse()
    
    answer = ''.join(remain_list)
    print(f"{n} in based 10 is {answer} in base {radix}")

n = int(input("Enter a number : "))
radix = int(input("Enter a radix : "))
deci_to_any_string(n, radix)
