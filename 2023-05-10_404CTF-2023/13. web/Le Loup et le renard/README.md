[Le Loup et le renard](challenge_files/README.md) - web, intro, 1126 solves
===

**Author**: Artamis#7513 and V0odOo#3248    

## Solve

### Part 1: https://le-loup-et-le-renard.challenges.404ctf.fr/fable/partie-1-inspecteur

Viewing the source of the webpage, we find the username and pass in plaintext:

```javascript
  function auth() {
    if (
      document.getElementById("username").value === "admin" &&
      document.getElementById("password").value === "h5cf8gf2s5q7d"
    ) {
      window.location.href = "/fable/partie-2-cookie";
    }
  }
```

### Part 2: https://le-loup-et-le-renard.challenges.404ctf.fr/fable/partie-2-cookie

Checking cookies, we find that `isAdmin` is set with value `false`. Changing it to `true` and reloading the page redirects to:

### Part 3: https://le-loup-et-le-renard.challenges.404ctf.fr/fable/partie-3-redirect

Trying to log in sends a request to https://le-loup-et-le-renard.challenges.404ctf.fr/fable/partie-4-flag-final which quickly redirects back to the part 3 page, but the contents of the page are still loaded. You can directly see them with curl, or by pressing esc really fast after submitting on a browser, cancelling the redirection just before the page content is removed:

### Part 4: https://le-loup-et-le-renard.challenges.404ctf.fr/fable/partie-4-flag-final

```html
└─[$] curl https://le-loup-et-le-renard.challenges.404ctf.fr/fable/partie-4-flag-final

<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      rel="shortcut icon"
      href="../static/ico/favicon.ico"
      type="image/x-icon"
    />
    <link rel="stylesheet" href="../static/font/Inter/inter.css" />
    <link rel="stylesheet" href="../static/font/Metropolis/style.css" />
    <link rel="stylesheet" href="../static/css/home.css" />
    
    <title>Le Loup et le Renard | Partie 4</title>
    
  </head>
  <body>
    
<div class="back-to-home">
  <p><a href="/">&#8617; Retour</a></p>
</div>
<div class="title-section">
  <h1>Partie 4<br />Flag</h1>
</div>
<div class="fable">
  <p>Chers développeurs, n'oubliez pas cette leçon,</p>
  <p>Il est préférable de prendre son temps pour la protection.</p>
  <p>L'authentification en front-end est une mauvaise idée,</p>
  <p>Et peut laisser la porte ouverte aux pirates, c'est une réalité.</p>
</div>

<div class="fable">
  <p>Alors, méfiez-vous, chers amis développeurs,</p>
  <p>Et ne négligez jamais la sécurité de vos utilisateurs,</p>
  <p>Car un site rapide et performant, sans sécurité,</p>
  <p>Peut vite devenir une calamité.</p>
</div>
<div>Flag : 404CTF{N0_frOn1_3nD_auTh3nt1ficAti0n}</div>
<script>
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  if (urlParams.has("username") && urlParams.has("password")) {
    const username = urlParams.get("username");
    const password = urlParams.get("password");
    if (!(username === "admin" && password === "Fbqh96BthQ")) {
      document.location = "/fable/partie-3-redirect";
    }
  } else {
    document.location = "/fable/partie-3-redirect";
  }
</script>

  </body>
```

## Comments

Intro challenge. Cute, covers the basics, everyone should learn how to view source, check places where websites store and retrieve data, and check the network requests. Has anyone actually found a plaintext js login in the wild since the early 2000s?