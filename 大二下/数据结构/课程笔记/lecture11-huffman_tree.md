# Lecture11

## Huffman 树

### Basic Concept

1. 路径: 
2. 路径长度: <u>线的数目</u>
3. 树的路径长度: 根到所有结点的路径长度之和
4. 结点的权: 实际意义下赋予权
5. 带权路径长度: 路径长度×结点的权
6. 树的带权路径长度: 叶子结点带权路径之和

Q1: 什么样的二叉树路径长度最小?

A1: 完全二叉树或与完全二叉树同构的二叉树(最底层结点数相同), 路径长度为
$$
\sum_{k=1}^h[\log_2 k]
$$
其中h为结点的个数, 路径长度为i的结点最多有2^i个

Q2: 什么样的二叉树带权路径长度最小?

A2: Huffman Tree (最优二叉树)的带权路径长度最小

1. 相同权重的不同二叉树的带权路径长度不同
2. 具有最小带权路径长度的二叉树不唯一
3. 大多情况下不同的具有最小带权路径长度的二叉树深度相同

**<u>算法步骤</u>**:

1. 定义权值:{w1,w2,...,wn}, 构造森林F={T1,T2,...,Tn}, 其中Ti(i=1,2,..,n)为单根树, 根的权值为wi
2. **在F全体中选择两颗权值最小的二叉树**, 构成一颗新的二叉树, 标记新的二叉树的根结点信息为左右权之和
3. 在F中删除2中选中的两颗二叉树同时**将新的二叉树加入F中**
4. 重复2,3直到F中只有一棵树, 那么该树即为Huffman Tree

**考点1**: Huffman树没有度为1的结点, 则一棵有n个叶子的Huffman树有2n-1个结点, 可以用静态三叉链表存储. weight, parent, Lchild, Rchild

**考点2**: Huffman树->静态三叉链表的转换; 三叉链表->Huffman树的重构

## Huffman 编码

### Basic Concept

1. 前缀码: 若在编码系统中任何一个编码都不是其他编码的前缀部分, 那么称该编码系统中的编码是前缀的
2. Huffman编码: 记左0右1或左1右0来表示结点的编码

Theorem1: Huffman code is prefix code

Proof: Prove by contradiction. Suppose Huffman code is not prefix code. That means there exists a code that is the prefix part of some other code. In Huffman Tree, that means a node and its parent node but it is impossible because Huffman Tree focus on leaf node. Q.E.D

Theorem2: Huffman code is the optimal prefix code. i.e. Huffman code can minimize every correspongding binary string's mean length.

### Huffman 编码的功能

获得平均长度最短的编码. 我们可以使用二进制编码(定长编码), 但是长度太长, Huffman 编码(变长编码)可以减小长度. 让权值少的编码位数大, 权值大的编码维数小