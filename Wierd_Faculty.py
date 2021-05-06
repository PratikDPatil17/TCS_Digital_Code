def weirdFaculty(v):
  n = len(v)
  # Convert all the zeros to -1 as
  # the zero gives us the negative score of -1

  for i in range(n):
    if not v[i]:
      v[i] = -1
  
   # Find the total sum

  totalSum = sum(v)
  currSum = 0

  # Find the point where current sum is
  # greater than the total sum

  for i in range(n):
    if currSum > totalSum:
      return i
    currSum += v[i]
    totalSum -= v[i]
  return n
