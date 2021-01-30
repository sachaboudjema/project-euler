-- 1 : Multiples of 3 and 5

-- multiples 3 5 1000
-- 233168
-- (0.01 secs, 479,456 bytes)

multiples :: Int -> Int -> Int -> Int
multiples x y z = sum [n | n <- [1..z-1], mod n x == 0 || mod n y == 0]

