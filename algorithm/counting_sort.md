# ๐งฉ์นด์ดํ ์ ๋ ฌ๐งฉ ์ฝ๋ฉ์ ๊ณ๋ค์ธ ํ๋ฏธ๊ฐ ๊ฐ๋ํ ์ค๋ช 

</br>

### ๊ฐ๋จ ์ค๋ช

> ์์ ๊ฐ ๋น๊ต์์ด ์ ๋ ฌ
>
> ๋ชจ๋  ์์๊ฐ ์์ ์ ์์ด๊ณ , ์ต๋๊ฐ์ ์๊ณ  ์์ ๋ ์ฌ์ฉ
>
> ์๊ฐ๋ณต์ก๋๊ฐ ์ ์ ๊ฒ์ด ์ฅ์  (ํ์ง๋ง ๋จธ๋ฆฌ๊ฐ ๋ณต์กํด์ง..)
>
> ๋์ ์ค์ฐํด๋ฅผ ์ญ์ ๋นํจ..๐

</br>

##### ๐์, ์์ ์ค๋ช์ ๋จธ๋ฆฟ์์์ ์ง์๋ฒ๋ฆฌ๊ณ  ์๋ ์ค๋ช๋ง ๋ด์๋ค.

---

์๋ฅผ ๋ค์ด, ๋ค์๊ณผ ๊ฐ์ด ์์๊ฐ ์๋ง์ธ `original` ๋ฆฌ์คํธ๊ฐ ์์ต๋๋ค. 

```python
orginal = [5, 0, 1, 1, 4, 3, 1, 4, 5, 2, 1]
```

์ฐ๋ฆฌ๋ ์ง๊ธ๋ถํฐ `original` ๋ฆฌ์คํธ๋ฅผ **์นด์ดํ ์ ๋ ฌ** ํ  ๊ฒ๋๋ค.

(๐๋จ, ์นด์ดํ ์ ๋ ฌ์ ํ  ๋์๋ ๋ฐ๋์ **์ต๋๊ฐ**์ ์ ์ ์์ด์ผํฉ๋๋ค!!)

</br>

์ `original` ๋ฆฌ์คํธ๋ฅผ ์นด์ดํ ์ ๋ ฌ์ ํ๋ค๋ฉด ์ต์ข๊ฒฐ๊ณผ๋ ๋ค์๊ณผ ๊ฐ์ต๋๋ค.

```python
result = [0, 1, 1, 1, 1, 2, 3, 4, 4, 5, 5]
```

</br>

์ด ๊ณผ์ ์์ 3๊ฐ์ง๋ง ๊ธฐ์ตํฉ์๋ค!

**โ๏ธ์ฒซ๋ฒ์งธ**, `original` ๋ฆฌ์คํธ ์์๋ค์ ๋น๋ ๊ฐ์ ์ธ์ด `counting` ๋ฆฌ์คํธ๋ฅผ ๋ง๋ค์ด์ค๋๋ค.

```python
counting = [1, 4, 1, 1, 2, 2]
```

โ๏ธ**๋๋ฒ์งธ**, `counting`์ ์์๊ฐ์ ์ง์  ์์๊ฐ์ ๋ํด์ค๋๋ค.

```python
counting = [1, 5, 6, 7, 9, 11]
```

๐ค**์ธ๋ฒ์งธ**, ์ด์  ์ฐ๋ฆฌ๋ `original` ๋ฆฌ์คํธ์ `counting` ๋ฆฌ์คํธ๋ฅผ ์ฌ์ฉํ์ฌ ์ต์ข๊ฒฐ๊ณผ๋ฌผ(`result`)์ ๋ง๋ค์ด๋ผ ๊ฒ ์๋๋ค.

```python
result = [0, 1, 1, 1, 1, 2, 3, 4, 4, 5, 5]
```

</br>

### ๐์ฒซ๋ฒ์งธ๋ฅผ ์ฝ๋ฉ์ผ๋ก!

---

```python
# ์ฒซ๋ฒ์งธ!
original = [5, 0, 1, 1, 4, 3, 1, 4, 5, 2, 1]

# original ๋ฆฌ์คํธ ์์๋ค์ ๋น๋ ๊ฐ ๋ฆฌ์คํธ ๋ง๋ค๊ธฐ!
counting = [0] * 6
for i in range(len(original):
	counting[original[i]] += 1
               
# counting = [1, 4, 1, 1, 2, 2]
```

์ฌ๊ธฐ์ ์ฐ๋ฆฌ๋ ์๋ก์ด ๋ฆฌ์คํธ `counting`์ ๋ง๋ค์ด ์ฃผ๊ณ , ์ฌ๊ธฐ์ **๋น๋ ๊ฐ**์ ๋ฃ์ ๊ฒ๋๋ค.

***(์ฐธ๊ณ )***

> ๊ทผ๋ฐ ์ฌ๊ธฐ์ ์๋ฌธ์ ์ด ์๊ธธ ์ ์์ด์.
>
> ์ **[0] * 6** ์ด๋ผ๋ ๋ฐ์ดํฐ๋ฅผ ๋ฏธ๋ฆฌ ๋ฃ์ด์ฃผ์ง? ๊ทธ๋ฆฌ๊ณ  ์ **[0]**์ **6๋ฒ** ๋ฃ์ด์ฃผ์ง??
>
> </br>
>
> ๊ทธ ์ด์ ๋ ๋ฏธ๋ฆฌ ๋ฐ์ดํฐ๋ฅผ ๋ฃ์ด์ฃผ์ง ์์ผ๋ฉด <u>์ค๋ฅ๊ฐ ๋ฐ์ํ๊ธฐ ๋๋ฌธ์๋๋ค.</u>
>
> ๋ง์ฝ ๋น๋ฆฌ์คํธ๋ก ์ค์ ํ๊ณ  for ๋ฌธ์ ์๋ ฅํ๋ค๋ฉด... ( `counting = []` )
>
> ```python
> for i in range(len(original):
> 	counting[original[i]] += 1
> ```
>
> for ๋ฌธ์ **์ฒซ๋ฒ์งธ i ๊ฐ = 0**
>
> **original[0] = 5**
>
> **counting[5]** 
>
> </br>
>
> ์ฌ๋ฌ๋ถ, <u>๋น๋ฆฌ์คํธ์ **5๋ฒ์งธ ๊ฐ**์ด๋ผ๋ ๊ฒ์ด ์กด์ฌํ ๊น์?</u> ์๋์ฃ ..๐ฑ
>
> ๊ทธ๋์ ์ฐ๋ฆฌ๋ ์ค๋ฅ ๋ฐฉ์ง๋ฅผ ์ํด ์์๋ก **[0] * 6**์ด๋ผ๋ **์์์ ๋ฐ์ดํฐ**๋ฅผ ๋ฃ์ด์ฃผ๋ ๊ฒ์๋๋ค.
>
> ๊ทธ๋ฆฌ๊ณ  ์์์ ๊ฐฏ์๊ฐ **0~5**, ์ฆ 6๊ฐ์ด๋๊น **[0]**์ **6๊ฐ** ์๋ ฅํด์ฃผ๋ ๊ฒ์ด์ง์~ 

</br>

### ๐๋๋ฒ์งธ๋ฅผ ์ฝ๋ฉ์ผ๋ก!!

---

```python
# ์ฒซ๋ฒ์งธ!
original = [5, 0, 1, 1, 4, 3, 1, 4, 5, 2, 1]

# original ๋ฆฌ์คํธ ์์๋ค์ ๋น๋ ๊ฐ ๋ฆฌ์คํธ ๋ง๋ค๊ธฐ!
counting = [0] * 6
for i in range(len(original):
	counting[original[i]] += 1
               
# counting = [1, 4, 1, 1, 2, 2]
               
############################################
# ๋๋ฒ์งธ!!
# counting ์์๊ฐ์ ์ง์  ์์๊ฐ์ ๋ํด์ฃผ๊ธฐ!
for i in range(len(counting)-1):
	counting[i+1] += counting[i]
               
# counting = [1, 5, 6, 7, 9, 11]
```

์ฌ๊ธฐ์ **range**๋ฅผ ์ค์ ํ  ๋, ๋ฐ๋์ **len(counting)**์ **-1**์ ํด์ค์ผ ํฉ๋๋ค. 

๋ง์ฝ ๊ทธ๋ฅ **len(counting)**์ผ๋ก ์ค์ ํ๊ฒ ๋๋ฉด ์๋ **counting[i+1]**์์ <u>range ๋ฒ์๋ฅผ ๋ฒ์ด๋๊ฒ ๋์ด ์ค๋ฅ๊ฐ ๋ฐ์ํฉ๋๋ค.</u>

๊ทธ๋ฆฌ๊ณ  **counting[i+1]**๋ก ์ค์ ํ์ฌ ๋ง์ง๋ง ๊ฐ๊น์ง ๋๋ฌํ๊ฒ ํฉ๋๋ค.

</br>

### ๐์ธ๋ฒ์งธ๋ฅผ ์ฝ๋ฉ์ผ๋ก!!!

---

```python
# ์ฒซ๋ฒ์งธ!
original = [5, 0, 1, 1, 4, 3, 1, 4, 5, 2, 1]

# original ๋ฆฌ์คํธ ์์๋ค์ ๋น๋ ๊ฐ ๋ฆฌ์คํธ ๋ง๋ค๊ธฐ!
counting = [0] * 6
for i in range(len(original):
	counting[original[i]] += 1
               
# counting = [1, 4, 1, 1, 2, 2]
               
############################################
# ๋๋ฒ์งธ!!
# counting ์์๊ฐ์ ์ง์  ์์๊ฐ์ ๋ํด์ฃผ๊ธฐ!
for i in range(len(counting)-1):
	counting[i+1] += counting[i]
               
# counting = [1, 5, 6, 7, 9, 11]

############################################
# ์ธ๋ฒ์งธ!!!    
# original๊ณผ counting ๋ฆฌ์คํธ๋ฅผ ์ฌ์ฉํด์ ์ต์ข๊ฒฐ๊ณผ๋ฌผ์ ๋ง๋ค๊ธฐ!
result = [0] * len(original)
for i in original:
	result[counting[i]-1] = i
	counting[i] -= 1
               
# result = [0, 1, 1, 1, 1, 2, 3, 4, 4, 5, 5]
```

~~**์ธ๋ฒ์งธ**๋ถํฐ ๋ง์ ๋ถ๋ค์ ๋จธ๋ฆฟ์์์ ***๋ํ์ฅํํฐ***๊ฐ ๋ฒ์ด์ง๋๋ค.~~ ๐คฌ๐ฟ๐ฅถ๐บ

์ด์  ์ฐ๋ฆฌ๋ `original` ๋ฆฌ์คํธ์ `counting` ๋ฆฌ์คํธ๋ฅผ ์ฌ์ฉํ์ฌ ์ต์ข๊ฒฐ๊ณผ๋ฌผ(`result` ๋ฆฌ์คํธ)์ ๋ง๋ค์ด๋ผ ๊ฒ ์๋๋ค.

๊ทธ๋ฌ๋ ๋ฐ๋์ **์ฒซ๋ฒ์งธ์ ๋๋ฒ์งธ for ๋ฌธ**์ ์๋ฒฝํ๊ฒ ์ดํดํ๊ณ  **์ธ๋ฒ์งธ**๋ฅผ ๋ฐ๋ผ๋ด์๋ค!

</br>

1. ์ค๋ฅ ๋ฐฉ์ง๋ฅผ ์ํด `result` ๋ฆฌ์คํธ์ ์์ ๋ฐ์ดํฐ **[0] * len(original)**์ ๋ฃ์ด์ค๋๋ค.

   </br>

2. ๊ทธ๋ฆฌ๊ณ  `original`๊ณผ `counting` ๋ฆฌ์คํธ๋ฅผ ์ด๋ ๊ฒ ๋ฐ๋ผ๋ด์๋ค.

   ```python
   for i in original:
   	result[counting[i]-1] = i
   ```

   > ๐โโ๏ธ`original`์ **๊ฐ(i) 5** => **counting[5]**์ **11**์ด๋๊น **5**์ **์ดํ๋ฒ์งธ**๋ก ๊ฐ์ผํด!!
   >
   > ๐โโ๏ธ`original`์ **๊ฐ(i) 0** => **counting[0]**์ **1**์ด๋๊น **0**์ **์ฒซ๋ฒ์งธ**๋ก ๊ฐ์ผํด!!
   >
   > ๐โโ๏ธ`original`์ **๊ฐ(i) 1** => **counting[1]**์ **5**์ด๋๊น **1**์ **๋ค์ฏ๋ฒ์งธ**๋ก ๊ฐ์ผํด!!
   >
   > ๐โโ๏ธ**===>>>** ***ํ์ง๋ง,*** `original`์ **๊ฐ(i) 1** => **counting[1]** ์ฅ? ๋ ๋์๋ค ์ด๋กํ์ง??

   </br>

3. ์, **2๋ฒ**์ ๋ง์ง๋ง์ฒ๋ผ ๊ฐ์ ๊ฐ์ด ๋ค์ ๋์ฌ ๊ฒ์ ๋๋นํ์ฌ **counting(i)** ๊ฐ์ **1**์ฉ ์ค์ฌ์ค๋๋ค. 

   ```python
   result[counting[i]-1] = i
   ```

   ๋ค์์ `original`์ **๊ฐ์ ์์(๊ฐ)**๊ฐ ๋์จ๋ค๋ฉด **์ด์  ๋์ผ ์์์ ์(์ )**์ ์์นํ๊ฒ ๋ฉ๋๋ค.

</br>

>์ด ๋ชจ๋  ๊ณผ์ ์ ์๋ฃํ๋ฉด `result` ๋ฆฌ์คํธ๋ ๋ค์๊ณผ ๊ฐ๊ฒ ๋ฉ๋๋ค.
>
>```python
>result = [0, 1, 1, 1, 1, 2, 3, 4, 4, 5, 5]
>```

</br>

### ๐งท ์ ๋ฆฌ 

---

์นด์ดํ ์ ๋ ฌ์ ํ๊ธฐ ์ ์.. 

> ์๋ณธ ๋ฆฌ์คํธ๊ฐ ๋ชจ๋ **์์ ์ ์**๋ก ์ด๋ฃจ์ด์ ธ์๋์ง
>
> (max ํจ์๋ฅผ ์ฐ์ง ์๋ ์ ์ ํ์) **์ต๋๊ฐ**์ ํ๋ฒ์ ์์๋ณผ ์ ์๋์ง 

์นด์ดํ ์ ๋ ฌ ์ค์..

> ๐ **3๊ฐ์ง ์์**๋ง ์ ์ดํดํ์!
>
> 1. ์๋ณธ ๋ฆฌ์คํธ ์์ ๊ฐฏ์ ์ธ์ **์นด์ดํ ๋ฆฌ์คํธ๋ก ๋ง๋ค๊ธฐ**
>
> 2. ์นด์ดํ ๋ฆฌ์คํธ ์์๋ค์ ์ธ๋ฑ์ค ์์๋๋ก **๋์ ์ผ๋ก ํฉํ๊ธฐ**
>
> 3. ์๋ณธ ๋ฆฌ์คํธ์ ์นด์ดํ ์์๋ฅผ ์ฌ์ฉํ์ฌ **์ต์ข ๋ฆฌ์คํธ ๋ง๋ค๊ธฐ**
>
>    โ๏ธ <u>์ฆ, for ๋ฌธ 3๊ฐ๋ฅผ ์จ์ผํ๋ค๋ ๊ฒ!!</u>

์นด์ดํ ์ ๋ ฌ ํ์..

>***์๋ฆฌ ๋ฒ๊ณ  ํฌํฐ ์ง๋ฌ~~***๐๐

</br>

```html
<h1>๊ณ ์ํ์จ์ด์, ์ฌ๋ฌ๋ถ</h1>
<p>์ด๋ฒ ์ค ์ฐํด ์ ๋ณด๋ด์จ๋์? 
    ์  ์ด๋ฒ 4์ผ ๋์ 
    ๋ฒ๋ธ, ์นด์ดํ ์ ๋ ฌ ๋ณต์ต 
    & ์๊ณ ๋ฆฌ์ฆ ๊ณผ์  ๋ฐ ํ๋ จ 
    & WEB ๋ณต์ต
    & ๊ฐ์ธ ๋ธ๋ก๊ทธ ๋ง๋ค๊ธฐ
    ...๋ผ๋ ์ฐฝ๋ํ ๊ณํ์ ์ธ์ ์ง๋ง, ์นด์ดํ ์ ๋ ฌ๋ง ํ๋ค๋ณด๋ ์ง๊ธ ์์ ์์ 3์๊ฐ ์ ์ด๋ค์..
    ์ ๋ง ํ๋ณตํ๊ตฐ์!
    ์ฌ์ค ๊ตฌ๊ธ๋ง๊ณผ ๋ค์ด๋ฒ๋ง์ ํตํด ์นด์ดํ ์ ๋ ฌ์ ๊ธ๋ฐฉ ๋๋ผ ์ค ์์๋๋ฐ,
    ์ฝ๊ฒ ์ค๋ช๋ ์๋ฃ๊ฐ ์์ด์ ์ ๊ฐ ์ง์  ๋ง๋ค์ด๋ณด์์ด์.
    ์  ์ค๋ช์ด ์๋ฒฝํ์ง๋ ์์ง๋ง ์ฌ๋ฌ๋ถ๋ค์ด ์ดํดํ๋ ๊ณผ์ ์์ ์กฐ๊ธ์ด๋ผ๋ ๋์์ด ๋์์ผ๋ฉด ์ข๊ฒ ์ด์.
    ์ฌ๋ฌ๋ถ๋ค ์ํด ๋ณต ์ข ๊ณผํ๋ค ์ถ์ ์ ๋๋ก ๋ง์ด ๋ฐ์ผ์๊ณ , ํญ์ ๊ฑด๊ฐํ์ธ์~
    ์ ๋ ์ ๊น ์๊ณ  ์ฌ๊ป์! 
    3์๊ฐ ๋ค์ ๋ด์..ใใ ์๋~ </p>
```

