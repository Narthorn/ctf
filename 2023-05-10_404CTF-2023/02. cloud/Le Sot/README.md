[Le Sot](challenge_files/README.md) - cloud, intro, 332 solves
===

**Author**: [Smyler#7078](https://github.com/SmylerMC)    

## Solve

We're given an S3 endpoint, https://s3.gra.io.cloud.ovh.net/, and a bucket name, `cloud-intro-challenge`.

Without looking too much into S3 or AWS, we can find that the way to access the public files of an s3 bucket is by prepending the bucket name as a subdomain of the s3 endpoint url, like so: https://cloud-intro-challenge.s3.gra.io.cloud.ovh.net/

Going there on a web browser yields an xml blob that lists the contents of the bucket:

```xml
<ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Name>cloud-intro-challenge</Name>
    <Prefix/>
    <Marker/>
    <MaxKeys>1000</MaxKeys>
    <IsTruncated>false</IsTruncated>
    <Contents>
        <Key>les-moutons.json</Key>
        <LastModified>2023-05-12T13:56:48.000Z</LastModified>
        <ETag>"d642390a5d6f695d958015801e585cb1"</ETag>
        <Size>1767</Size>
        <Owner>
            <ID/>
            <DisplayName/>
        </Owner>
        <StorageClass>STANDARD</StorageClass>
    </Contents>
</ListBucketResult>
```

This shows a single file, `les-moutons.json`, which we can access at https://cloud-intro-challenge.s3.gra.io.cloud.ovh.net/les-moutons.json: 

```
{
    "sheeps": [
        {
            "name": "Ivy",
            "canSwim": false,
            "canFly": false,
            "sex": "male",
            "treat": "follower"
        },
        {
            "name": "Sweetie",
            "canSwim": false,
            "canFly": false,
            "sex": "female",
            "treat": "follower"
        },
        {
            "name": "Pine",
            "canSwim": false,
            "canFly": false,
            "sex": "male",
            "treat": "follower"
        },
        {
            "name": "Cinnamon",
            "canSwim": false,
            "canFly": false,
            "sex": "male",
            "treat": "follower"
        },
        {
            "name": "Shaggy",
            "canSwim": false,
            "canFly": false,
            "sex": "female",
            "treat": "follower"
        },
        {
            "name": "Khaki",
            "canSwim": false,
            "canFly": false,
            "sex": "female",
            "treat": "follower"
        },
        {
            "name": "Sugar",
            "canSwim": false,
            "canFly": false,
            "sex": "male",
            "treat": "follower"
        },
        {
            "name": "Sponge",
            "canSwim": true,
            "canFly": true,
            "sex": "female",
            "treat": "leader"
        },
        {
            "name": "Flufkins",
            "canSwim": false,
            "canFly": false,
            "sex": "demale",
            "treat": "follower"
        },
        {
            "name": "Ruth",
            "canSwim": false,
            "canFly": false,
            "sex": "male",
            "treat": "follower"
        }
    ],
    "flag": "404CTF{D35_m0utOns_D4n5_13s_NU@g3s}"
}
```

## Comments

I actually went down a rabbit hole trying to make aws-cli work, but since we're not given any credentials, it doesn't really let us interact with the bucket at all. Theoretically, you should be able to call some public APIs like ListObjects using aws-cli with --no-sign-request, but I couldn't make that work with OVH's s3 endpoint, I was getting Invalid Request all the time. Truly, doing web requests to list files is a complex and delicate art.
