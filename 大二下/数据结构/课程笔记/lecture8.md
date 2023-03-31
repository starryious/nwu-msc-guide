# Lecture8

## 3.2 队列

### 3.2.1 队列的定义

队列(Queue)是只允许在表的一端插入元素, 而在另一端删除元素的另一种限定性的线性表. 允许删除的一端称为**队头**, 允许插入的一端称为队尾.

**特性**: 先进先出 (First In Fist Our, FIFO).

队列的**抽象数据类型**定义(ADT Queue)

**数据元素**: 属于同一个数据对象的任意类型数据.

**关系**: 队列中的数据元素之间是线性关系.

**基本操作**: 

* `InitQueue(& Q)`

* `IsEmpty (Q)`

* `IsFull(Q)`

* `EnterQueue(&Q, x)`

* `DeleteQueue(&Q,&x)`

* `GetHead(Q,&x)`

* `ClearQueue(&Q)`

* `DestroyQueue(&Q)`

### 3.1.2 队列的表示和实现

队列有顺序表示和链式表示两种表示方法

1. **链队列**: 用链表表示的队列称为链队列.

   ```c
   #define TRUE 1
   #define FALSE 0
   typedef struct Node
   {
       QueueElementType data /* 数据域 */
       struct Node *next /* 指针域 */
   } LinkQueueNode;
   typedef struct
   {
       LinkQueueNode *front;
       LinkQueueNode *rear;
   } LinkQueue;
   ```


* 初始化操作

  ```c
  int InitQueue(LIinkQueue *Q)
  {
  /* 将Q初始化为一个空的链队列*/
      Q->front=(LinkQueueNode*)malloc(sizeof(LinkQueueNode));
      if(Q->front!=NULL)
      {
          Q->rear=Q->front;Q->front->next=NULL;
          return(TRUE);
      }
      else return(FALSE); /* 溢出! */
  }
  ```

* 入队操作

  ```c
  itn EnterQueue(LinkQueue *Q, QueueElementType x)
  {
      /* 将数据元素x插入到队列Q中 */
      LinkQueueNode *NewNode;
      NewNode=(LinkQUeueNode)malloc(sizeof(LinkQueueNode));
      if(NewNode!=NULL)
      {
          NewNode->data=x;
          NewNode->next=NULL;
          Q->rear->next=NewNode;
          Q->rear=NewNode;
          return(TRUE);
      }
      else return(FALSE); /* 溢出 */
  }
  ```

* 出队操作

  ```c
  int DeleteQueue(LinkQueue* Q, QueueElementType *x)
  {
  /* 将队列Q的队头元素出队, 并存放到x所指的存储空间中 */
      LinkQueueNode *p;
      if(Q->front==Q->rear) return(FALSE)
          p=Q->fornt->next;
      	Q->front->next=p->next; /* 队头元素p出队 */
      if(Q->rear==p) /* 如果队中只有一个元素p, 则p出队后为空队*/
          Q->rear=Q->front;
      	*x=p->data;
      	free(p); /* 释放空间*/
      return(TRUE)
  }
  ```

2. **循环队列**:
   * 用一维数组`Queue[MAXSIZE]`存放从队头到队尾的元素.
   
   * 附设两个指针`front`和`rear`, 分别指示队头元素和队尾元素在数组中的位置.
   
   * 由于只能在队头出队, 在队尾入队, 所以会产生**假溢出**的现象
   
     为了解决这个问题, 可以将顺序队列的数组看成一个环状空间, 用取余操作.
     
     判断空队列
     
     ```c
     if(Q->front==Q->rear) return(TRUE)
     ```
     
     判断满队列
     
     ```c
     if(Q->(rear+1) % M == Q->front ) return(TRUE)
     ```

### 3.3.1

* 堆栈和队列, 都是操作受限制的线性表, 它们共同点是操作的位置限制在表的端点
* 堆栈具有LIFO的特定, 限定元素的运算位置只在表尾(栈顶)端进行
* 队列具有FIFO的特性. 限定元素的运算位置分别在表的两端进行

顺序和链式的两种存储方式

* 对进栈操作来说, 顺序栈收到**事先开辟的栈区容量**限制, 以避免上溢. 链栈方式下, 只有当**整个系统无法申请到可用空间**时, 才无法进栈, 队列操作亦同.
* 循环队列是一种**顺序队列**. 通过模运算将其看成一个首位相连的环. 求队列的长度是模运算, 为区分队列的空和满, 有两种典型的解决方法: 一种是**损失一个空间**的方法; 另一种是**设置标志位**的方法
* 链队列的操作实现与单链表的操作实现类似, 而链队列除了**头指针**, 还设一个**尾指针**, 并且通常封装在一个结构体里.

栈和队列

1. 利用栈和队列都可以控制解决问题的顺序
2. 凡是对元素的保存次序与使用顺序相反的, 都可以使用栈; 凡是对元素的保存次序与使用顺序相同的, 可以使用队列.

### 3.1.4 栈与递归的实现

<u>递归</u>: 在定义自身的同时又出现了对自身的调用

<u>直接递归函数</u>: 如果一个函数在其定义体内直接调用自己, 则称直接递归函数.

<u>间接递归函数</u>: 如果一个函数经过一系列的中间调用语句, 通过其他函数间接调用自己, 则称间接递归函数.