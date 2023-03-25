# Lecture 4

## 2.3 线性表的链表存储

**链表定义:**

### 2.3.1 单链表

**结点**: 存储线性表的每个数据元素值的信息与元素间逻辑关系即后继结点地址信息的两部分存储映象

**单链表**: 每个结点只有一个指针域的链表. 包括数据域和指针域. 数值域用来存储结点的值, 指针域用来存储数据元素的直接后继的地址.

[![vgsAU.png](https://i.328888.xyz/2023/03/13/vgsAU.png)](https://imgloc.com/i/vgsAU)

**头指针**: 指向链表头结点的指针 

<u>在内存空间中并不是按顺序排列, 找到哪里有空的地方就开一个空间</u>.

**单链表的存储结构描述**: 

```c
typedef struct Node
{
EleType data;
struct Node *next;
}Node, *LinkList;
```

### 2.3.2 单链表上的基本运算(重点)

**建立单链表**: 

分为头插法和尾插法.

**算法描述**: 从一个空表开始, 重复读入数据, 生成新结点, 将读入数据存放到新结点的数据域中, 然后将新结点插入到当前链表的表头结点之后, 直至读入结束标志为止.

**头插法代码**:

```c
Linklist CreateFromHead(LinkList L)
{
    LinkList L;
    Node *s;
    char c;
    int flag = 1;
    /* 设置一个标志, 初值为1, 当输入 "$" 时, flag为0, 建表结束 */
    while(flag)
    {
        c=getchar();
        if(c!='$')
         {
          s=(Node*)malloc(sizeof(Node));
            /* 为读入的字符分配存储空间 */
            s->data=c;
            s->next=L->next;
            L->next=s;
         }
        else flag=0;
    }
}
```

**尾插法代码**:

```c
Linklist CreateFromTail(LinkList L)
{
    LinkList L;
    Node *r, *s;
    char c;
    int flag = 1;
    /* 设置一个标志, 初值为1, 当输入 "$" 时, flag为0, 建表结束 */
    r=L; /* r指针始终动态指向链表的当前表尾, 以便于做尾插入, 其初值指向头结点 */
    while(flag)
    {
        c=getchar();
        if(c!='$')
         {
          s=(Node*)malloc(sizeof(Node));
            /* 为读入的字符分配存储空间 */
            s->data=c;
            r->next=s;
            r=s;
         }
        else 
         { flag=0;
           r->next=NULL; /* 将最后一个结点的 next 链域置为空, 表示链表的结束 */
         }
    }  /* while */
}
```

**主函数代码**:

```c
main()
{
    Node *L1;
    L1=(Node*)malloc(sizeof(Node));
    L1->next=NULL;
    CreatFromHead(L1)''
}
```

对于单链表, 头指针永远不会动, 最后一个数据项一定为空.

**单链表查找**:

分为**按序号查找**和**按值查找**.

**按序号查找的算法功能**: 在带头结点长度为 `n` 的单链表中查找第 `i` 个结点

**按序号查找的算法描述**: 

* 单链表的头指针 `L` 出发, 从头结点 `(L->next)` 顺链扫描;
* 用指针 `P` 指向当前扫描到的结点, 初值指向头结点 `(PL->next)`
* 用 `j` 做计数器, 初值为 `0`
* 当 `j=i` 时, 指针 `p` 所指的结点就是要找的第 `i`个结点

**代码**:

```c
Node *Get(LinkList L,int i)
{
    /* 在带头结点的单链表L中查找第i个结点, 若找到(1<=i<=n), 则返回该结点的存储位置; 否则返回NULL*/
    int j;
    Node *p;
    p=L;
    j=0; /* 从头结点开始扫描 */
    while ((p->next!=NULL)&&(j<i))
     {
      p=p->next; /* 扫描下一结点*/
      j++; /* 已扫描结点计数器 */
     }
    if(i==j) return p; /* 找到了第i个结点 */
    else return NULL;
    	/* 找不到, i<=0 或 i>n */
}
```



**按值查找的算法描述**: 按值查找是指在单链表中查找是否有结点指等于 `e` 的结点, 若有的话, 则返回首次找到的值为 `e` 的结点的存储位置, 否则返回 `NULL`. 查找过程从单链表的头指针指向的头结点出发, 顺着链逐个将结点的值和给点值 `e` 作比较.

**代码**:

```c
Node *Locate(Linklist L, ElemType key)
{
    /* 在带头结点的单链表 L 中查找其结点值等于 key 的结点, 若找到则返回该结点的位置 p, 否则返回 NULL*/
    Node *p;
    p=L->next; /* 从表中第一个结点比较 */
    while(p!=NULL)
        if(p->data!=key)
            p=p->next;
    	else break;
    	/* 找到结点 key , 退出循环*/
    return p;
}
```


