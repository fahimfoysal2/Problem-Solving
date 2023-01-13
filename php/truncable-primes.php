<?php

/**
 * The number 3797 has an interesting property . Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
 * Find the sum of the only eleven primes that are both truncatable from left to right and right to left .
 * NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes .
 * 
 * // Answer: 748317
 */

function isTruncatablePrime($n)
{
    $n = (string) $n; // convert to string to be able to use substr()
    $len = strlen($n);
    for ($i = 0; $i < $len; $i++) {
        $left = substr($n, $i);
        $right = substr($n, 0, $len - $i);
        if (!isPrime($left) || !isPrime($right)) {
            return false;
        }
    }
    return true;
}

function isPrime($n)
{
    // maybe use a sieve of eratosthenes to speed up the process but that's not the goal now

    if ($n == 1) {
        return false;
    }
    if ($n == 2) {
        return true;
    }
    if ($n % 2 == 0) {
        return false;
    }
    $limit = sqrt($n);
    for ($i = 3; $i <= $limit; $i += 2) {
        if ($n % $i == 0) {
            return false;
        }
    }
    return true;
}


function truncablePrimes()
{
    $count = 0;
    $sum = 0;
    $n = 11; // starting from 11 because 2, 3, 5, and 7 are not considered to be truncatable primes
    while ($count < 11) {
        if (isTruncatablePrime($n)) {
            $count++;
            $sum += $n;
        }
        $n += 2; // only odd numbers can be truncatable primes
    }
    return $sum;
}

// test run
echo truncablePrimes();
echo "\n";
