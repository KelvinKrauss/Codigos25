def _sum(arr):
   sum = 0

   for i in arr:
      sum = sum + i
   return(sum)

if __name__ == "__main__":
   arr = [12, 14, 17]
   n = len(arr)
   ans = _sum(arr)
   print ('Sum of the array ', ans)