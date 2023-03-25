### 线性表的插入操作

**算法描述**: 要在带头结点的单链表 L 中第 `i` 个数据元素之前插入一个数据元素 `e`, 需要首先在单链表中找到第 `i-1` 个结点并由指针`pre`指示, 然后申请一个新的结点并由指针 `s` 指示, 其数据域的值为 `e` ,并修改第 `i-1` 的结点的指针使其指向 `s` , 然后使 `s` 结点的指针域指向第 `i` 个结点.

**代码实现**:

````c
void InsList(LinkList L, int i, ElemType e)
{
    Node *pre, *s;
    int k;
    pre=L; k=0;
    while (pre!=NULL && k<i-1)
    /* 在第 i 个元素之前插入, 则先找到第 i-1 个数据元素的存储位置, 使指针 Pre 指向它  */
    {
        pre=pre->next;
        k=k+1
    }
    if(!pre)
    /* 如当前位置 pre 为空, 表示已找完还未数到第 i 个, 说明插入位置不合理  */
    {
        print{"插入位置不合理!"};
        return ERROR;
    }
    s=(Node*)malloc(sizeof(Node));
    /* 为 e 申请一个新的结点并由 S 指向它  */
    s->data=e;
    /* 将待插入结点的值 e 赋给 s 的数值域 */
}
````

### 单链表的删除

**算法描述**: 欲在带头结点的单链表 L 中删除第 `i` 个结点, 则首先要通过计数方式找到第 `i-1` 个结点并使 p 指向第 `i-1` 个结点, 而后删除第 `i` 个结点并释放结点空间.

**代码实现**:

```c
void DelList(LinkList, int i,ElemType *e)
/* 在带头结点的单链表 L 中删除第 i 个元素, 并将删除的元素保存到变量 *e 中  */
{
    Node *p, *r;
    int k;
    p=L;k=0
    while(p->next!=NULL && k<i-1)
    /* 寻找被删除结点 i 的前驱结点 i-1 使 p 指向它 */
    {
        p=p->next;
        k=k+1;
    }
    if(k!=i-1)
    /* 即while循环时因为 p->next=NULL 而跳出的  */
    {
        print("删除结点的位置 i 不合理!");
        return;
    }
    r=p->next;
    p->next=p->next->next;
    *e=r->data;
    free(r); /* 释放被删除的结点所占用的内存空间  */
}
```

### 循环链表

循环链表(Circular Linked List) 是一个首尾相连的链表.

**特点**: 将单链表最后一个的结点的指针域由 `NULL` 改为指向头结点或线性表中的第一个结点, 就得到了单链形式的循环链表, 并称为循环单链表. 在循环单链表中, 表中所有结点被链在一个环上.

```
temp=RB->next
RB->next=RA
```



**循环单链表的合并算法**:

**算法描述**: 先找到两个链表的尾, 并分别由指针 `p`, `q`指向它们, 然后将第一个链表的尾与第二个表的第一个结点链接起来, 并修改第二个表的尾 `Q`, 使它们的链域指向第一个表的头结点.

### 双向链表

双向列表是给单链表的每个结点增加一个指向其前驱的指针后的新链表

**结构定义**:

```c
typedef struct Dnode
{
    ElemType data;
    struct DNode *prior, *next;
} DNode, *DoubleList;
```

**双向链表的插入**: 画图写代码

**双向链表的删除**: 画图写代码

### 静态链表

描述: 由于一些语言中并未提供 "指针" 类型, 静态链表采用数组模拟实现链表.

* 存储池: 定义一个较大的结构数组作为备用结点空间

* 结点结构:

  ```c
  typedef structure
  {
  ElemType data;
  int cursor;
  } Component, StaticList[Maxsize];
  ```

  游标机制: