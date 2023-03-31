# Lecture7

#### 3.1.2 栈的表示和实现

<u>栈</u>在计算机中主要有两种基本的存储结构: 

* 顺序存储结构
* 链式存储结构

##### 顺序栈定义:

* 用一组连续的存储单元依次存放自栈底到栈顶的数据元素
* 设一个位置指针 `top` (栈顶指针) 动态指示栈顶元素在顺序栈中的位置
* `top = -1` 表示空栈

**C语言代码**:

```C
 # define True 1
 # define FALSE 0
 # define Stack_Size 50
typedef struct
{
    StackElementType elem[Stack_Size];
    int top;
} SeqStack;
```

**顺序栈基本操作的实现**

* 初始化

  ```c
  void InitStack(SeqStack *S)
  {
      S->top=-1 /* 构造一个空栈*/
  }
  ```

* 判栈空

  ```c
  int IsEmpty(SeqStack *S)
  {
    return(S->top == 1?TRUE:FALSE); /*判断S为空栈时返回真, 否则返回假*/
  }
  ```

* 判栈满

  ```c
  int IsFull(SeqStack *S)
  {
      return(S->top == Stack_Size-1?TRUE:FALSE); /*判断S为满时返回真, 否则返回假*/
  }
  ```

* 进栈

  ```c
  int Push(SeqStack *S, StackElementType x)
  {
      if(S->top == Stack_Size) return(FALSE); /*栈已满*/
      S->top++;
     	S->elem[S->top]=x;
      return(TRUE);
  }
  ```

* 出栈

  ```c
  int Pull(SeqStack *S, StackElementType *e)
  {
      if(S->top == -1) return(FALSE); /*栈已空*/
      else
      {
      *e = S->elem[S->top];
      S = top--;
      return(TRUE);
      }
  }
  ```

* 取栈顶元素

  ```c
  int GetTop(SeqStack *S, StackElementType *x)
  {
     if(S->top == -1) return(FALSE); /*栈已空*/
      else{
      *x = S->elem[S->top];
   	return(TRUE);
      }
  }
  ```

* 两栈共享的数据结构

  * **两栈共享的数据结构定义**:

    ```c
    # define M 100
    typedef struct
    {
        StackElementTypeStack[M];
        StackElementTypetop[2];
        /* top[0],top[1]分别为两个指示器*/
    }DqStack
    ```

  * 初始化操作算法

    ```c
    void InitStack(DqStack *S)
    {
        S->top[0] = -1
        S->top[1] = M
    }
    ```

  * 进栈操作算法

    ```c
    int Push(DqStack *S, StackElementType x, int i)
    {
        if(S->top[0] +1 == S->top[1] return(FALSE); /*两栈已满*/
        else{
        switch(i)
           {
               case 0 :
                S->top[0]++;
               	S->Stack[S->top[0]] = x;
                break;
               case 1 :
               S->top[0]--;
               S->Stack[S->top[1]] = x;
                break;
            default: return(FALSE)
           }
        return(TRUE);
        }
    }
    ```

  * 出栈操作算法

    ```c
    int Pop(DqStack *S. StackElementType *x, int i)
    {
        switch(i)
        {
            case 0: if (S->top[0] == -1)   			             return(FALSE); 
                *x = S->Stack[S->top[0]]; 
                S->top[0] --; 
                break;
            case 1: if(S->top[1] == M)
                return (FALSE);
                *x = S->Stack[S->top[1]];
                S->top[1]++;
                break;
            default: return(FALSE);
        }
        return(TRUE);
    }
    ```

##### 链栈

采用头结点的单链表实现链栈. 头指针就作为栈顶指针. 

* `top` 为栈顶指针, 始终指向当前栈顶元素前面的头结点.
* 若 `top->next=NULL`, 则代表空栈.

**C语言代码**:

```c
typedef struct node
{
    StackElementType data;
    struct node *next;
}LinkStackNode;

typedef LinkStackNode *LinkStack; /* 替换上述链表 */
```

**链栈的进栈操作**

```c
int Push(LinkStacktop, StackElementType x)
    /* 将数据元素x压入栈top中 */
{
    LinkStackNode *temp;
    temp = (LinkStackNode*)malloc(sizeof(LinkStackNode));
    if(temp==NULL) return(FALSE); /* 申请空间失败 */
    else
    {
    temp->data=x;
    temp->next=top->next;
    top->next=temp; /*修改当前栈指针*/
    return(TRUE);
    }
}
```

**链栈的出栈操作**

```c
int Pop(LinkStacktop, StackElementType *x)
{
    /* 将栈top的栈顶元素弹出, 放到x所指的存储空间中*/
    LinkStackNode *temp; temp=top->next;
    if(temp == NULL) /* 栈为空 */
        return(FALSE);
    else{
        top->next=temp->next; 
        *x=temp->data;
        free(temp);
    }
    return(TRUE);
}
```

**多栈运算**

将多个链栈的栈顶指针放在一个一维指针数组中来统一管理, 从而实现同时管理和使用多个栈.

```c
#define M 10 /* M个链栈 */
typedef struct node
{
    StackElementType data;
    struct node *next;
} LinkStackNode *LinkStack;
```

##### 括号匹配问题

算法思想: 在检验算法中设置一个栈, 若读入的是左括号, 则直接入栈, 等待相匹配的同类右括号; 若读入的是右括号, 且与当前栈顶的左括号同类型, 则二者匹配, 将栈顶的左括号出栈, 否则属于不合法的情况.

```c
voidBracketMatch(char *str)
{
    Stack S; int i; char ch;
    InitStack (& S);
    for(i=0;str[i]!='\0';i++)
    {
        switch(str[i])
        {
                case '(':
            case '[':
            case '{':
                	Push(&S,str[i]);
                	break;
                case '(':
                case '[':
                case '{':
                if(IsEmpty(S))
                {printf("\n右括号多余!");return;}
              else
              {GetTop(&S,&ch);}
              if(Match(ch,str[i]))
              Pop(&S,&ch);
              else
              {
               print("\n 对应的左右括号不同类");
                  return;
              }
              }
                /* swith */
        } /* for */
        if(IsEmpty(S))
            printf("\n括号匹配!");
        else
            printf("\n左括号多余!")
    
}
```

