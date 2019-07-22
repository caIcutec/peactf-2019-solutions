This image contains some steganographic data that we need to find. Checking the file we find it's a PNG, and a brief glance at the encoded data shows nothing out of the ordinary. Running a zsteg analysis shows nothing either, so the solution is either simpler or much more difficult. Thankfully, no bit operations or checksums are needed to solve this problem - Opening the file in stegsolve.jar and scrolling through different filters, we can see hex numbers in certain values of the red plane. Translating from hex to ascii yields us the flag.

flag{peactf_where_the_wind_blows}
