#Same simple algorithm written in every offered language. Variable a tells you the number of ways to reach the current step, and b tells you the number of ways
#to reach the next step. So for the situation one step further up, the old b becomes the new a, and the new b is the old a+b, since that new step can be reached by climbing 1 step from what b represented or 2 steps from what a represented.

#Ruby wins, and "the C languages" all look the same.

def climbStairs(self,n):
    a = b = 1
    for _ in range(n):
        a,b = b ,a + b
    return a
