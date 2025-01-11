# Vision Test

- Time limit: 0.5 seconds
- Memory limit: 256 MB

Mohammad Reza, who has finished his university entrance exam, wants to participate in all Quera programming contests; however, he is currently busy conducting vision tests for students applying for driving licenses.

Mohammad Reza places a word made up of English letters two meters away from the student, and the student must write it down exactly. Then, Mohammad Reza tells the student the number of incorrect letters as an indicator of the student's vision impairment.

Mohammad Reza is in a hurry to participate in the Quera contest and wants to perform the vision tests using a computer, so he has requested a program that takes the word placed in front of the student and the word written by the student as input, and outputs the number of mistakes made by the student.

## Input
The first line of the input contains a number \( n \) representing the number of letters in the words.

The second line contains a string consisting of uppercase and lowercase English letters, representing the word placed in front of the student.

The third line also contains a string consisting of uppercase and lowercase English letters, representing the word written by the student.

\( 1 \leq n \leq 100000 \)

## Output

The only line of the output should contain a non-negative integer which is the number of letters the student wrote incorrectly.

## Example

### Sample Input 1

```
3
ABC
aBD
```

### Sample Output 1

```
2
```

### Sample Input 2

```
21
MASIOJESTDYSLEKTYKIEM
MAsIOJSSTDXSIEKTYKLEM
```

### Sample Output 2

```
5
```


# تست بینایی

- محدودیت زمان: ۰.۵ ثانیه
- محدودیت حافظه: ۲۵۶ مگابایت

محمدرضاص که کنکورش را داده، میخواهد در همه‌ی مسابقات برنامه‌نویسی کوئرا شرکت کند؛ اما اکنون درگیر گرفتن تست بینایی از هنرجویان متقاضی گواهینامه‌ی رانندگی است.

محمدرضاص در فاصله‌ی دو متری هنرجو یک کلمه از حروف انگلیسی قرار میدهد و این هنرجو باید از روی آن عیناً بنویسد. سپس محمدرضاص تعداد حرف‌های اشتباه نوشته شده را بعنوان مقدار کوری این فرد به او بگوید.

محمدرضاص برای دادن مسابقه‌ی کوئرا عجله دارد و میخواهد بصورت کامپیوتری کارهای تست بینایی را انجام دهد، پس درخواست کرده که برنامه‌ای بنویسید که با ورودی گرفتن کلمه‌ی گذاشته‌شده در جلوی هنرجو و کلمه‌ی نوشته شده توسط هنرجو، تعداد اشتباه‌های هنرجو را خروجی دهد.

## ورودی
در سطر اول ورودی یک عدد n آمده است که نمایانگر تعداد حروف کلمات است.

در سطر دوم یک رشته متشکل از حروف کوچک و بزرگ انگلیسی آمده‌است که نمایانگر کلمه‌ی گذاشته‌شده جلوی هنرجوست.

در سطر دوم نیز یک رشته متشکل از حروف کوچک و بزرگ انگلیسی آمده‌است که نمایانگر کلمه‌ی نوشته شده توسط هنرجوست.

1 <= n <= 100000

## خروجی

تنها سطر خروجی باید شامل یک عدد صحیح نامنفی باشد که برابر تعداد حروفیست که هنرجو اشتباه نوشته است.

## مثال

### ورودی نمونه ۱

```
3
ABC
aBD
```

### خروجی نمونه ۱

```
2
``` 

### ورودی نمونه ۲

```
21
MASIOJESTDYSLEKTYKIEM
MAsIOJSSTDXSIEKTYKLEM
```

### خروجی نمونه ۲

```
5
``` 