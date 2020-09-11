def firstPosition(arr,n):

  st=0
  lt=len(arr)-1
  index=-1

  while(st<=lt):
    mid = (st + lt)//2

    if(arr[mid]==n):
      index = mid
      lt=mid-1
    elif(arr[mid]>n):
      lt=mid-1
    else:
      st=mid+1

  if index!=-1:
    return index
  else:
    return 0 

def lastPosition(arr,n):

  st=0
  lt=len(arr)-1
  index=-1

  while(st<=lt):
    mid = (st + lt)//2

    if(arr[mid]==n):
      index = mid
      st=mid+1
    elif(arr[mid]>n):
      lt=mid-1
    else:
      st=mid+1
      
  if index!=-1:
    return index
  else:
    return 0   

while (1):
  l = int(input("Enter how many elements you want:"))
  if (0 <= l <= 10**5):
    break
  else:
    print("Invalid!! insert within 0 to 10^5")
    continue

print("Enter numbers in array:") 
arr = [] 
for i in range(l):
  while (1):
    c= int(input())
    if (-10**9 <= c <= 10**9):
      break
    else:
      print("Invalid!! insert within -10^9 to 10^9")
      continue
  arr.append(c)

while (1):
  t = int(input("Enter the target number:"))
  if (-10**9 <= t <= 10**9):
    break
  else:
    print("Invalid!! insert within -10^9 to 10^9")
    continue
    
arr.sort()
fIndex=firstPosition(arr,t)
lIndex=lastPosition(arr,t)
print(f"[{fIndex},{lIndex}]")