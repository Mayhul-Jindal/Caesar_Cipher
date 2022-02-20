# **CAESAR CIPHER DECRYPTER**

This is a simple decypter which chooses brute-force method to give you all possible decoded strings.

## **Stegonagraphy Detection**

Here I used linux strings command, which primarily focuses on determining the contents of and extracting text from the binary files (non-text file).

![Screenshot 2022-02-21 001213](https://user-images.githubusercontent.com/95216160/154859022-99526013-4c0d-4820-af8e-897137a69a35.jpg)

![Screenshot 2022-02-21 001251](https://user-images.githubusercontent.com/95216160/154859034-5eb01806-0581-4fcb-81f1-a7fcc38cdb3f.jpg)

Now here I found the last string, bit like a flag so I tried it decrypting using my script and it comes out to be
```
CSI{c0nGr@tz_qTp1e}
```

## **Demo**

https://user-images.githubusercontent.com/95216160/154858810-4c13158a-994c-407d-922d-e476fc819fb9.mp4

## **Setup**

Install all the dependencies by
```
pip install -r requirements.txt
```
