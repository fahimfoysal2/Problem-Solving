<?php

/**
 * A unit fraction contains 1 in the numerator . 
 * The decimal representation of the unit fractions with denominators 2 to 10 are given:
 * 
 * 1 / 2
 * =
 * 0.5
 * 1 / 3
 * =
 * 0.(3)
 * 1 / 4
 * =
 * 0.25
 * 1 / 5
 * =
 * 0.2
 * 1 / 6
 * =
 * 0.1(6)
 * 1 / 7
 * =
 * 0.(142857)
 * 1 / 8
 * =
 * 0.125
 * 1 / 9
 * =
 * 0.(1)
 * 1 / 10
 * =
 * 0.1
 * 
 * Where 0.1(6) means 0.166666..., and has a 1 - digit recurring cycle . It can be seen that 1 / 7 has a 6 - digit recurring cycle .
 * Find the value of d < 1000 for which 1 / d contains the longest recurring cycle in its decimal fraction part .
 * 
 * Answer: 983
 */

function reciprocalCycles($limit)
{
    $max = 0; // max cycle length
    $maxD = 0; // denominator with max cycle length
    for ($denominator = 1; $denominator < $limit; $denominator++) {
        $r = 1; // remainder
        $i = 0; // index
        $remainders = [];
        while ($r != 0) {
            $r = $r % $denominator; // remainder of division by denominator 
            if (isset($remainders[$r])) { // if remainder is already in array then we have a cycle 
                $cycle = $i - $remainders[$r]; // cycle length 
                if ($cycle > $max) { // if cycle length is greater than max cycle length then update max cycle length and max denominator
                    $max = $cycle;
                    $maxD = $denominator;
                }
                break;
            }
            $remainders[$r] = $i; // add remainder to array 
            $r *= 10; // multiply remainder by 10 because we are looking for the decimal part of the fraction
            $i++;
        }
    }
    return $maxD;
}

// test run
echo reciprocalCycles(1000);
echo "\n";
