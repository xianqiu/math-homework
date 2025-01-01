## 功能描述

**自动生成数学作业，并保存为PDF。**

### 加减法

`series = 'Add'`

| 等级 | 名称        | 公式                  | 说明         |
|----|-----------|---------------------|------------|
| 1  | 加法        | a+b=                | 20以内       |
| 2  | 减法        | a-b=                | 20以内       |
| 3  | 加法、减法     | a+b= 或 a-b=         | 20以内       |
| 4  | 连加        | a+b+c=              | 30以内       |
| 5  | 连减        | a-b-c=              | 30以内       |
| 6  | 连加、连减     | a+b+c= 或 a-b-c=     | 30以内       |
| 7  | 连加减       | a+b-c= 或 a-b+c=     | 30以内       |
| 8  | 负数相加      | -a-b=               | 30以内       |
| 9  | 加法、减法     | a-b=, -a+b=         | 30以内       |
| 10 | 加法、减法     | -a-b=, -a+b=, a-b=  | 30以内, a可负  |
| 11 | 连减法       | a-b-c= 或 -a-b-c=    | 30以内       |
| 12 | 连加减       | a+b-c= 或 a-b+c=     | 30以内       |
| 13 | 连加减       | -a+b-c= 或 -a-b+c=   | 30以内       |
| 14 | 负负得正      | a+(-b)= 或 a-(-b)=   | 40以内       |
| 15 | 负负得正      | -a+(-b)= 或 -a-(-b)= | 40以内       |
| 16 | 符号混合      | a+b+c=              | 45以内,abc可负 |
| 17 | 加法填空      | a+?=b 或 ?+a=b       | 40以内       |
| 18 | 减法填空      | a-?=b 或 ?-a=b       | 40以内       |
| 19 | 加法填空、减法填空 | a+?=b 或 a-?=b       | 40以内       |
| 20 | 加减法填空     | a@?=c, @ in {+,-}   | 60以内       |
| 21 | 加法填空、减法填空 | -a+?=b 或 -a-?=b     | 60以内       |
| 22 | 加减法填空     | a@b@?=d @ in {+,-}  | 60以内       |
| 23 | 加减法填空     | a-b+?=c             | 60以内, a可负  |
| 24 | 填空        | a@b@?=d, @ in {+,-} | 90以内，abc可负 |

### 乘除法

`series = 'Mult'`

| 等级 | 名称   | 公式                                | 说明          |
|----|------|-----------------------------------|-------------|
| 1  | 乘法基础 | a×b=                              | ab是1位数，非负   |
| 2  | 乘法基础 | a×b=                              | ab是1位数      |
| 3  | 乘法填空 | a×?=c                             | ab是1位数，非负   |
| 4  | 乘法填空 | a×?=c                             | ab是1位数      |
| 5  | 除法基础 | c÷a=                              | a是1位数，非负    |
| 6  | 除法基础 | c÷a=                              | a是1位数       |
| 7  | 除法填空 | c÷?=b 或 ?÷a=b                     | ab是1位数，非负   |
| 8  | 除法填空 | c÷?=b 或 ?÷a=b                     | ab是1位数      |
| 9  | 乘法加减 | a×b+c×d= 或 a×b-c×d=               | abcd是1位数    |
| 10 | 乘法填空 | a×?+c×d=e 或 a×b-?×d=e             | abcd是1位数    |
| 11 | 四则运算 | a×b+c÷d= 或 a×b-c÷d=               | abd是1位数     |
| 12 | 四则填空 | a×?+c÷d=e 或 a×b+c÷?=e 或 a×b-?÷d=e | abd是1位数     |
| 13 | 乘法加减 | a×(b+c)= 或 a×(b-c)=               | abc是1位数，c非负 |
| 14 | 四则填空 | (a+?)×c=d 或 (a-?)×c=d             | abc是1位数     |
| 15 | 四则运算 | (a+b)×(c+d)=                      | abcd是1位数    |
| 16 | 四则填空 | (a+?)×(c+d)=e                     | abcd是1位数    |
| 17 | 连乘   | a×b×c=                            | abc是1位数     |
| 18 | 连乘填空 | a×?×c=d 或 a×b×?=d                 | abc是1位数     |
| 19 | 乘法   | a×b=                              | ab是2位数      |
| 20 | 乘法填空 | a×?=c                             | a是2位数       |
| 21 | 除法   | a÷b=                              | b是2位数       |
| 22 | 除法填空 | a÷?=c 或 ?÷b=c                     | bc是2位数      |
| 23 | 四则运算 | a@b@c@d=, @ in {+,-,×,÷}          | 2位数，非负      |
| 24 | 四则运算 | a@b@c@d=, @ in {+,-,×,÷}          | 2位数         |
| 25 | 四则填空 | a@b@?@c=d, @ in {+,-,×,÷}         | 2位数，非负      |
| 26 | 四则填空 | a@b@?@c=d, @ in {+,-,×,÷}         | 2位数         |

### 分数

`series = 'Frac'`

| 等级 | 名称    | 公式                        | 说明        |
|----|-------|---------------------------|-----------|
| 1  | 加减法   | a+b=, a-b=                | ab是分数，非负  |
| 2  | 连加减   | a+b-c=, a-b+c=            | abc是分数，非负 |
| 3  | 加减法填空 | a@?@b=c, @ in {+,-}       | abc是分数    |
| 4  | 乘法    | a×b=                      | ab是分数     |
| 5  | 除法    | a÷b=                      | ab是分数     |
| 6  | 乘除法   | a×b÷c=, a÷b×c=            | abc是分数    |
| 7  | 乘除法填空 | a@?@b=c, @ in {×,÷}       | abc是分数    |
| 8  | 四则运算  | a@b@c@d=, @ in {+,-,×,÷}  | abcd是分数   |
| 9  | 四则填空  | a@b@?@c=d, @ in {+,-,×,÷} | abcd是分数   |
| 10 | 加减法   | a+b=, a-b=                | ab是1位小数   |
| 11 | 加减法   | a@b@c=, @ in {+,-}        | abc是1位小数  |
| 12 | 加减法填空 | a@b@?=c, @ in {+, -}      | abc是2位小数  |
| 13 | 乘法    | a×b=                      | ab是1位小数   |
| 14 | 除法    | a÷b=                      | b是1位小数    |
| 15 | 乘除法   | a×b÷c=                    | ac是1位小数   |
| 16 | 乘除法填空 | a×b÷?=c, a×?÷b=c          | abc是分数    |
| 17 | 四则运算  | a@b@c@d=, @ in {+,-,×,÷}  | abcd是小数   |
| 18 | 四则填空  | a@?@b@c=d, @ in {+,-,×,÷} | abcd是小数   |

### 解方程

`series = 'Form'`

| 等级 | 名称    | 公式                        | 说明         |
|----|-------|---------------------------|------------|
| 1  | 一元方程  | ax+b=c                    | abcx是整数    |
| 2  | 一元方程  | ax+b=c                    | abc是分数     |
| 3  | 一元方程  | ax+b=c                    | abc是小数     |
| 4  | 二元方程组 | ax+by=c, dx+ey=f          | abxydef是整数 |
| 5  | 二元方程组 | ax+by=c, dx+ey=f          | abdef是整数   |
| 6  | 二元方程组 | ax+by=c, dx+ey=f          | abcdef是小数  |
| 7  | 二次展开  | (ax+b)(ax-b)=             | ab是整数      |
| 8  | 因式分解  | a^2x^2-b^2=               | ab是整数      |
| 9  | 二次展开  | (ax+b)^2=                 | ab是整数      |
| 10 | 因式分解  | a^2x^2+2abx+b^2=          | ab是整数      |
| 11 | 二次方程  | ax^2+b=c                  | abc是整数     |
| 12 | 因式分解  | ax^2+bx=,a(x+b)^2+c(x+b)= | abc是整数     |
| 13 | 二次方程  | e(ax+b)^2+c=d             | abcde是整数   |
| 14 | 二次方程  | x^2 + (b+c)x + bc = 0     | bc是整数      |
| 15 | 二次方程  | ax^2+bx+c=0               | abc是整数     |

### 函数

`series = 'Func'`

| 等级 | 名称      | 公式                       | 说明             |
|----|---------|--------------------------|----------------|     
| 1  | 一元一次函数  | f(x) = ax + b, f(n) =    | ab是整数, 计算 f(n) |
| 2  | 一元一次方程  | af(x) + bx = c           | abc是整数         |
| 3  | 函数相加    | f(x) + xg(x) = 0         | g(x)=c/x, 解方程  | 
| 4  | 函数相除    | f(x) / g(x) = c          | c 是常数, 解方程     |
| 5  | 函数相乘    | f(x)g(x) = c             | c是常数, 解方程      |
| 6  | 二元一次方程  | f(x,y)=0, g(x,y)=0       | a,b是常数, 解方程    |
| 7  | 复合函数    | f(f(x)) = a              | a是常数, 解方程      |
| 8  | 复合函数    | f(f(x)) = f(x)           | 解方程            |
| 9  | 复合函数    | f(f(x), y) = 0           | 解方程            |
| 10 | 反函数     | f^{-1}(x) =              | 求表达式           |
| 11 | 反函数     | f^{-1}f(x) + f(x) = 0    | 解方程            |
| 12 | 反函数     | f^{-1}(x)f(x) =          | 求表达式           |
| 13 | 反函数复合函数 | f(f^{-1}(x)) =           | 求表达式           |
| 14 | 反函数复合函数 | f^{-1}(f(x)) = f^{-1}(x) | 解方程            |

## 使用方法

```python
from mathw import MathWork

if __name__ == '__main__':
    # 生成作业并保存成PDF
    MathWork(
        # Add - 加减法；Mult - 乘除法
        # Frac - 分数; Form - 解方程
        # Func - 函数;
        series='Form',
        level=4,  # 等级
        pageNum=20  # 页数
    ).go()
```