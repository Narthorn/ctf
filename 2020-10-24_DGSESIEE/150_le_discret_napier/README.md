Le discret Napier
=================

**Category** : Crypto  
**Score** : 150 points  
**Solved** : 138 times  

---

>Retrouvez x tel que : 17^x ≡ 183512102249711162422426526694763570228 [207419578609033051199924683129295125643]
>
>Le flag est de la forme : DGSESIEE{x} avec x la solution

---

Lets's be lazy and ask [sage](https://github.com/sagemath) to solve the discrete log for us:

```python
sage: %time Mod(183512102249711162422426526694763570228, 207419578609033051199924683129295125643).log(17)

CPU times: user 1min 42s, sys: 292 ms, total: 1min 42s
Wall time: 1min 43s

697873717765
```

Flag: `DGSESIEE{697873717765}`

---

#### Further thinking

I still don't know if sage is exploiting any special feature of the modulus here. n = 207419578609033051199924683129295125643 is a big prime, but only ~127 bits, so maybe that's weak enough to be attacked directly?

By Fermat's little theorem, for prime n, `z^(n-1) = 1 [n]`, so instead of working modulo n, we can work modulo n-1. The [Pohlig-Hellman algorithm](https://en.wikipedia.org/wiki/Pohlig%E2%80%93Hellman_algorithm) works best when n-1 factorizes into lots of small primes, which is not really the case here (n = 2 * 43 * 47 * 373 * 2707 * 2608763 * 19481470025232063548957)

According to [wikipedia](https://en.wikipedia.org/wiki/Discrete_logarithm_records#Integers_modulo_p), the current record for discrete logarithm with prime modulus is 3100 core years of a 2.1GHz Intel Xeon Gold 6130 CPU, with a 795-bits safe prime (a safe prime is a prime n where n-1 is written n-1 = 2 * p, with p also prime, so Pohlig-Hellman *really* doesn't help you here).

Now, their algorithm is probably very optimized and distributed in some way that you can start reaping benefits of scale over very large numbers, but if you ignore that, and for simplicity assume something equivalent to the best known discrete log algorithm, the Number Field Sieve for Discrete Logarithms, the complexity is something around this:

    c(n) = e^(((64/9)^(1/3) + o(1))*ln(2^n)^(1/3)*ln(ln(2^n))^(2/3))

which means that they should be able to solve a discrete log with 127bit prime modulus in around (3100 core years) / c(795) * c(127) ~= 5.45 core milliseconds, which is still 5 orders of magnitudes faster than sage!

Either the complexity estimate is too imprecise, or sage is way slow. Most likely both. I trust that sage, while presenting a python interface, still calls into native code to do the heavy lifting, but it would be interesting to directly write a naive implementation of NFSDL in a low-level language and see how fast you could make it go.

---

#### process

This challenge seemed too short to be hard, so I did it fairly early. My math is very rusty, so it took me a little longer than strictly needed to recognize this as "the" discrete log problem (title should have been a dead giveaway, if anything).

Once I did, I just tried a few software purporting to solve discrete logs; I knew the general problem was NP-hard (technically not proven to be NP-hard, but the entire planet relies on it being computationally unsolvable for large enough integers, or all public key cryptography is instantly broken and we have way bigger problems on our hands), so I did not expect an instant solve. 

But since I did not know how long it would actually take for a "smart" algorithm to exploit flaws in the modulus that I assumed would be there, I just left them running for the day while I went to solve other challenges.

After a whole day of no results, I started looking for better tools, and sage found the result very quickly.
