# imgimgimg (1000 points)

#### by @dreb
![Alt text](_images/image.png)

From the attachment given, we saw that inside the zip file is another zip file, an extra file, and a folder.

![Alt text](_images/image-1.png)

When we tried to unzip the zip file (inside), it asks for a password. Not knowing what the password is, we tried to check the other files. after doing the file command on the file, it results to saying it is a jpeg image.

![Alt text](_images/image-2.png)

We changed the extension of the file to .jpeg. We then opened the image and it says:

![Alt text](_images/image-3.png)

`strings` did not show anything meaningful text, so we tried `binwalk` and it shows that there is a PNG file hidden inside. However using `binwalk -e` does not work.

![Alt text](_images/image-4.png)

We used foremost to carve the file out, instead.

![Alt text](_images/image-5.png)

The png file then displays the password needed for the locked zip.

![Alt text](_images/image-6.png)

When we unzip the locked zip, we get 16 PNG files

![Alt text](_images/image-7.png)

We see that the files are pieces of a qr code.

![Alt text](_images/image-8.png)

We can see that it has been split into 4x4. So we used `imagemagick` to connect the pictures together. We need to append all images horizontally using the +append command.

After appending, we get 4 images. Now all we need to do i just to connect them vertically using this command `./magick 1.png 2.png 3.png 4.png -append qr.png`

![Alt text](_images/image-9.png)

We now have the whole image ready to be scanned.

![Alt text](_images/image-10.png)

using `zbar image`, we are able to get the flag

![Alt text](_images/image-11.png)

**Flag:** ACS{1mage_4nd_Qu1ck_R3$pon5e_M4gic!}