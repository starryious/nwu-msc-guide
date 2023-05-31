你需要掌握清楚的基础概念:

* 统计, 统计学, 描述统计, 统计推断(1.0统计学导论,)

* 总体(Population) (1.0统计学导论,1.1总体与样本)

* 参数(Parameter) (1.0统计学导论)

* [样本(Sample)](https://en.wikipedia.org/wiki/Sampling_(statistics)) (1.0统计学导论,1.1总体与样本)

  *  简单随机样本

* 样本容量, 样本值 (1.1总体与样本)

* [统计量(Statistic) ](https://en.wikipedia.org/wiki/Statistic) (1.0统计学导论,1.2统计量及样本矩)

* 样本矩(1.2统计量及样本矩)

  *  样本均值, 样本方差, 样本相关系数

* [经验分布函数(Empirical Distribution Function)](https://zh.wikipedia.org/wiki/经验分布函数)(1.3经验分布函数)

  *  个人理解就相当是测度论中的simple function简单可测函数
  *  第二条性质
  *  Glivenko-Cantelli定理

* [顺序(次序)统计量(Order Statistic)](https://zh.wikipedia.org/wiki/顺序统计量)(1.8次序统计量)

  * Beta分布

* 抽样分布(R.A.Fisher)(1.4-1卡方分布)

* chi-square 分布(1.4-1卡方分布)

  * 掌握, 必须会做题

  * Cochran factorization theorem

  * Fisher, u为标准正态分布的上分位点
    $$
    \chi^2_{\alpha}(n)\approx\frac{1}{2}(u_{\alpha}+\sqrt{2n-1})^2\quad(n\to\infty)
    $$

  * 非中心chi-square分布

  * Gamma 分布

* Student-t分布(1.4-2t分布)

* Fisher-F分布
  $$
  F_{1-\alpha}(n_1,n_2)=\frac{1}{F_{\alpha(n_2,n_1)}}
  $$
  
* 样本中位数(Median)(1.8次序统计量)

* 样本极差(1.8次序统计量)

* [分位数(Quantile)](https://zh.wikipedia.org/wiki/%E5%88%86%E4%BD%8D%E6%95%B0)(1.4-1卡方分布)

* 正态总体统计量的分布
$$
\bar{X}\sim N(\mu, \frac{\sigma^2}{n})\quad \frac{\bar{X}-\mu}{\sigma/\sqrt{n}}\sim N(0,1)\\
\frac{(n-1)S^2}{\sigma^2}\sim \chi^2(n-1)\quad \bar{X},S^2\text{相互独立}\\
\frac{\bar{X}-\mu}{S/\sqrt {n}}\sim t(n-1)\\
\frac{\bar{X}-\bar{Y}-(\mu_1-\mu_2)}{\sqrt{\frac{(n_1-1)S_1^2+(n_2-1)S_2^2}{n_1+n_2-2}}\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}}\\
\frac{S_1^2/S_2^2}{\sigma_1^2/\sigma_2^2}\sim F(n_1-
1,n_2-1)
$$

1.

简单独立同分布计算
$$
f_{X_1,X_2,\cdots X_n}=p^{\sum_{i=1}^n x_i}(1-p)^{n-\sum_{i=1}^n x_i}
$$
2.
$$
\bar{Y}=\frac{1}{b}(\bar{X}-a)\quad {S_Y}^2=\frac{1}{b^2}{S_X}^2
$$
可以发现结果和正常的随机变量的变换一样, 即样本均值和样本方差是两个实实在在的<u>随机变量</u>, 进一步来讲, 是<u>统计量</u>

3.

加一项减一项的常用变换, 完全平方拆开等简单技巧

4.
$$
F_n(x)=\frac{1}{n}\sum_{i=1}^nI\{(x_i\le x)\}
$$

$$
E(F_n(x))=E(\frac{1}{n}\sum_{i=1}^nI\{(x_i\le x)\})=\frac{1}{n}\sum_{i=1}^nP(x_i\le x)=F(x)
$$

$$
\begin{align}
Var(F_n(x))&=E(F_n^2(x))-F^2(x)\\
&=\frac{1}{n^2}E(\sum_{i=1}^nI\{(x_i\le x)\})-F^2(x)\\
&=\frac{1}{n^2}\sum_{i=1}^nE(I)-F^2(x)\\
&=\frac{1}{n^2}\times n\times F(x)-F^2(x)\\
&=\frac{1}{n}F(x)(1-F(x))
\end{align}
$$

5.

数个数...

6.7

套公式

8.

小学生都会做

9.

套顺序统计量公式后计算

10.

正推

11.12. 见 R Tutorial