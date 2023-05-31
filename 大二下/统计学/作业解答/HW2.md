你需要掌握的基本概念:

* Gamma 分布族, Beta分布族(1.4-4几个常用分布族)
* 充分统计量(sufficient statistic)(1.7充分统计量-1-1)
* [支撑集](https://zh.wikipedia.org/wiki/%E6%94%AF%E6%92%91%E9%9B%86) (1.4-4 几个常用分布族)
* [指数型分布族(Exponential family)](https://en.wikipedia.org/wiki/Exponential_family)(1.4-4 几个常用分布族)
* 充分(Sufficient)
* 充分统计量(Sufficient Statistic)(1.7充分统计量)
  * 分解定理(Neyman)


**一般求统计的抽样分布时先在三大抽样分布中大致确定是哪一个, 确定独立性, 然后正推, 不要倒推.**

1.
$$
X_n-\bar{X}\sim \mathcal{N}(0,\frac{n+1}{n}\sigma^2)\\
\frac{(n){S_n}^2}{\sigma^2}\sim\chi^2(n-1)\\
\quad T\sim t(n-1)
$$
2.
$$
\sum_{i=1}^nX_i\sim \mathcal{N}(0,n\sigma^2)\\ U=\frac{\sum_{i=1}^nX_i}{\sqrt n \sigma}\sim \mathcal{N}(0,1)\quad V=\sum_{i=1}^n(\frac{X_i}{\sigma})^2\sim\chi^2(n)
$$
因此根据定义即可证明

4.
$$
\text{注意}X_i\text 与\bar{X}\text{不独立}
$$
重新组合
$$
V_i=X_i-\frac{X_i}{n+1}-\frac{1}{n+1}\sum_{\substack{j=1\\j\neq i}}^{n+1}X_i=\frac{nX_i}{n+1}-\frac{1}{n+1}\sum_{\substack{j=1\\j\neq i}}^{n+1}X_i
$$
此时相互独立, 那么可以直接用正态分布的性质来计算
$$
V_i\sim \mathcal{N}(0,\frac{n}{n+1}\sigma^2)
$$
5.
$$
U=\frac{a\bar{X}+b\bar{Y}-(a\mu_1+b\mu_2)}{\sqrt{(\frac{a^2}{m}+\frac{b^2}{n})\sigma^2}}\sim \mathcal{N}(0,1)
$$

$$
V=\frac{(m-1){S_{1m}}^2+(n-1){S_{1n}}^2}{\sigma^2}\sim \chi(n+m-2)
$$

计算即可
$$
c=\sqrt{\frac{mn(m+n-2)}{na^2+mb^2}}
$$
