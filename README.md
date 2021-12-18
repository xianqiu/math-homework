## 功能描述

**自动生成学前班数学作业（加减法），并保存为PDF。**

作业按照知识点为多个等级，如下表所示：

|等级|名称| 公式 | 说明|
|-|-|-|-|
|1|加法| a+b= | 20以内，非负|
|2|减法| a-b= | 20以内，非负|
|3|加法、减法| a+b= 或 a-b= | 20以内，非负|
|4|连加|a+b+c=| 30以内，非负|
|5|连减|a-b-c=| 30以内，非负|
|6|连加、连减| a+b+c= 或 a-b-c=| 30以内，非负|
|7|连加减| a+b-c= 或 a-b+c=| 30以内，非负|
|8|减法| a-b=| 30以内，可以为负|
|9|加法、减法| -a-b= 或 -a+b= 或 a-b=| 30以内|
|10|连减法| a-b-c= 或 -a-b-c= | 30以内|
|11|连加减| a+b-c= 或 a-b+c= | 30以内|
|12|连加减| -a+b-c= 或 -a-b+c= | 30以内|
|13|加法填空| a+?=b | 40以内|
|14|减法填空| a-?=b | 40以内|
|15|加法填空、减法填空| a+?=b 或 a-?=b | 40以内|
|16|加后填空|a+b+?=c 或 a+b-?=c| 40以内|
|17|负负得正| a+(-b)= 或 a-(-b)=| 40以内|
|18|负负得正| -a+(-b)= 或 -a-(-b)=| 40以内|
|19|加法填空、减法填空| -a+?= 或 -a-?=| 40以内|
|20|减后填空|a-b+?=c 或 a-b-?=c|40以内|
|21|减后填空|-a-b+?=c 或 -a-b-?=c| 40以内|
|22|加后、减后填空| -a+b+?=c 或 -a-b+?=c 或 |40以内|

## 使用方法

```python
from mathw import MathWork

if __name__ == '__main__':
    # 生成作业并保存成PDF
    MathWork(
        level=4,  # 等级
        pageNum=40  # 页数
    ).go()
```
