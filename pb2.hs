-- 2 : Even Fibonacci numbers

-- sum_even_fib 4000000
-- 4613732
-- (107.04 secs, 31,117,087,152 bytes)

fib :: Int -> Int
fib 0 = 0
fib 1 = 1
fib n = fib (n -1) + fib (n -2)

sum_even_fib :: Int -> Int
sum_even_fib n = sum $ takeWhile (< n) [fib x | x <- [1..], even (fib x)]

