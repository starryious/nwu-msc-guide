# Lecture3

## 指针与地址

**指针就是地址.**

指针的声明: 我们可以先声明一个指针再将地址赋给指针. 也可以直接声明一个带地址的指针

```c
type *p;
type *p = &a;
```

`type` 表示指针指向的值的类型. `*` 为间接操作符. `&` 为取地址符.

```c
p=&a; 
```

我们可以用 `*` 来访问指针地址的值并赋值给其他变量

```c
int val = *p;
```

我们可以通过 `*p` 来修改 `a` 的值

```
*p = 100;
```

得到 `a=100`

**数组名是地址**. 

多函数进行操作时, 可以用指针操作来改变原数组内容, 普通传值给子函数只传了一份拷贝. **教材p28 [程序示例 1.3]**

## 顺序存储结构的基本运算

* 查找操作

  * 按序号查找 `GetData(L,i)`, 要求查找线性表 `L` 中第 `i` 个数据元素, 其结果是 `L.elem[i-1]`, `L->elem[i-1]`, 前者是变量操作, 后者是指针操作.

    ```c
    int Locate(SeqList L, ElemType e)
    {
    i=0;
    while ((i <= L.last)&&(L.elem[i]!=e))
        i++;
        if (i<=L.last)
            return(i+1);
        else
            return(-1);
    }
    ```

​			仅定位, 不改变.

* 插入操作

  * 问题要求: 在线性表的第 `i` 个位置之间插入一个新元素 `e`.

    ```c
    int InsList(SeqList *L, int i, ElemType e)
    {
        int k;
        if((i<1)||(i>L->last+2))
        {
            printf("插入位置 i 值不合法!");
            return(ERROR);
        }
        if(L->last >= maxsize-1)
        {
            printf("表已满无法插入!");
            retuen(ERROR);
        }
        for(k=L->last;k>=i-1;k--)
            L->elem[k+1]=L->elem[k];
        L->elem[i-1]=e;
        L->last++;
        Return(OK);
    }
    ```

​			平均执行次数为: n/2

* 删除操作

  * 问题要求: 将线性表的第 `i` 个元素删除

    ```c
    int DelList(SeqList *L, int i, ElemType *e)
    {
        int k;
        if ((i<1)||(i> L->last+1))
        {
            printf("删除位置不合法!");
            return(ERROR);
        }
        *e= L->elem[i-1]; /*存储删除的元素*/
        for (k=i;k <= L->last;k++)
            L->elem[k-1]=L->elem[k];
        L->last--;
        Return(OK);
    }
    ```

    平均执行次数为: (n-1)/2

## 线性表顺序存储结构的优缺点分析

* 优点:
  * 无需为表示结点间的逻辑关系而增加额外的存储空间
  * 可以方便地随机存取表中的任一元素
* 缺点:
  * 插入或删除运算不方便, 除表尾的位置外, 在表的其他位置上进行插入或删除操作都必须移动大量的结点, 其效率较低
  * 由于顺序表要求占用连续的存储空间, 存储分配只能预先进行<u>静态分配</u>(长度基本已经分配). 因此当表长变化较大时, 难以确定合适的存储规模