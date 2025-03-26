5. 用积分方法证明图9.21中球缺的体积为 $$V = \pi H^2 (R - \frac{H}{3})$$.

解：
考虑半径为 $R$ 的球，从顶部截取高度为 $H$ 的球缺。为方便计算，将球心置于坐标原点 $(0,0,0)$。球缺的底面位于 $z = R - H$ 处。在 $z$ 处，横截面圆的半径 $r$ 满足 $r^2 + z^2 = R^2$，所以 $r^2 = R^2 - z^2$。

球缺的体积可以通过积分得到：
$$V = \int_{R-H}^{R} \pi r^2 dz = \int_{R-H}^{R} \pi (R^2 - z^2) dz$$

计算积分：
$$V = \pi \left[ R^2 z - \frac{1}{3} z^3 \right]_{R-H}^{R}$$
$$V = \pi \left[ (R^3 - \frac{1}{3} R^3) - (R^2(R-H) - \frac{1}{3}(R-H)^3) \right]$$
$$V = \pi \left[ \frac{2}{3} R^3 - (R^3 - R^2 H - \frac{1}{3}(R^3 - 3R^2H + 3RH^2 - H^3)) \right]$$
$$V = \pi \left[ \frac{2}{3} R^3 - R^3 + R^2 H + \frac{1}{3}R^3 - R^2 H + RH^2 - \frac{1}{3} H^3 \right]$$
$$V = \pi \left[ -\frac{1}{3} R^3 + R^2 H + \frac{1}{3}R^3 - R^2 H + RH^2 - \frac{1}{3} H^3 \right]$$
$$V = \pi \left[ RH^2 - \frac{1}{3} H^3 \right]$$
$$V = \pi H^2 \left(R - \frac{H}{3}\right)$$

因此，球缺的体积为 $$V = \pi H^2 (R - \frac{H}{3})$$。

6. 求由曲线 $$x = a\cos^3 t, y = a\sin^3 t$$ 所围图形绕 $$x$$ 轴旋转一周所得立体的体积。

解：
曲线的参数方程为 $$x = a\cos^3 t, y = a\sin^3 t$$，其中 $0 \le t \le 2\pi$。当曲线绕 $x$ 轴旋转时，旋转体的体积可以由以下公式计算：

$$V = \pi \int_{x_1}^{x_2} y^2 dx$$

这里需要将积分变量从 $x$ 转换为 $t$。首先求出 $dx/dt$:
$$\frac{dx}{dt} = -3a\cos^2 t \sin t$$
因此，$dx = -3a\cos^2 t \sin t dt$。

然后确定积分的上下限。由于曲线关于 $x$ 轴对称，我们可以只计算上半部分的体积，然后乘以 2。在上半部分，$$t$$ 的范围是 $$0$$ 到 $$\pi$$。但是注意到当 $t$ 从 $0$ 变化到 $\pi/2$ 时，$x$ 从 $a$ 变化到 $0$，而当 $t$ 从 $\pi/2$ 变化到 $\pi$ 时，$x$ 从 $0$ 变化到 $-a$。我们可以利用对称性，只考虑 $t$ 从 $0$ 到 $\pi/2$ 的部分，此时 $x$ 从 $a$ 变化到 $0$。因此，
$$V = 2\pi \int_{a}^{0} y^2 dx = 2\pi \int_{0}^{\pi/2} (a\sin^3 t)^2 (-3a\cos^2 t \sin t) dt$$
$$V = -6\pi a^3 \int_{0}^{\pi/2} \sin^7 t \cos^2 t dt$$

由于积分结果为负数，我们取绝对值。积分 $$\int_{0}^{\pi/2} \sin^m t \cos^n t dt$$ 可以用 Wallis 积分公式求解：
$$\int_{0}^{\pi/2} \sin^m t \cos^n t dt = \frac{\Gamma(\frac{m+1}{2}) \Gamma(\frac{n+1}{2})}{2\Gamma(\frac{m+n+2}{2})}$$
或者使用递推公式：
$$\int_{0}^{\pi/2} \sin^m t \cos^n t dt = \frac{m-1}{m+n} \int_{0}^{\pi/2} \sin^{m-2} t \cos^n t dt$$
也可以查表得到
$$\int_{0}^{\pi/2} \sin^7 t \cos^2 t dt = \frac{2}{9} \cdot \frac{4}{7} \cdot \frac{6}{5} \cdot 1 = \frac{16}{315}$$
因此，
$$V = 6\pi a^3 \cdot \frac{16}{315} = \frac{32\pi a^3}{105}$$

7. 求由 $$r = a(1 + \cos\theta)$$ ($$a > 0$$) 绕极轴旋转一周所围立体的体积。

解：
极坐标方程为 $$r = a(1 + \cos\theta)$$，其中 $0 \le \theta \le \pi$ 绕极轴旋转一周。旋转体的体积可以用以下公式计算：

$$V = \frac{2\pi}{3} \int_{0}^{\pi} r^3 \sin\theta d\theta$$

将 $$r = a(1 + \cos\theta)$$ 代入：
$$V = \frac{2\pi}{3} \int_{0}^{\pi} [a(1 + \cos\theta)]^3 \sin\theta d\theta$$
$$V = \frac{2\pi a^3}{3} \int_{0}^{\pi} (1 + \cos\theta)^3 \sin\theta d\theta$$
$$V = \frac{2\pi a^3}{3} \int_{0}^{\pi} (1 + 3\cos\theta + 3\cos^2\theta + \cos^3\theta) \sin\theta d\theta$$

令 $u = \cos\theta$，则 $du = -\sin\theta d\theta$。当 $\theta = 0$ 时，$u = 1$；当 $\theta = \pi$ 时，$u = -1$。
$$V = \frac{2\pi a^3}{3} \int_{1}^{-1} (1 + 3u + 3u^2 + u^3) (-du)$$
$$V = \frac{2\pi a^3}{3} \int_{-1}^{1} (1 + 3u + 3u^2 + u^3) du$$
$$V = \frac{2\pi a^3}{3} \left[ u + \frac{3}{2} u^2 + u^3 + \frac{1}{4} u^4 \right]_{-1}^{1}$$
$$V = \frac{2\pi a^3}{3} \left[ (1 + \frac{3}{2} + 1 + \frac{1}{4}) - (-1 + \frac{3}{2} - 1 + \frac{1}{4}) \right]$$
$$V = \frac{2\pi a^3}{3} \left[ 2 + 2 \right] = \frac{2\pi a^3}{3} \left[ 4 \right] = \frac{8\pi a^3}{3}$$

因此，体积为 $$V = \frac{8\pi a^3}{3}$$。

8. 证明由平面图形 $$0 \le a \le x \le b, 0 \le y \le f(x)$$ 绕 $$y$$ 轴旋转一周所成的旋转体的体积为 $$V = 2\pi \int_a^b xf(x) dx$$，其中 $$f(x)$$ 在 $$[a, b]$$ 上连续。

解：
考虑平面图形 $$0 \le a \le x \le b, 0 \le y \le f(x)$$ 绕 $$y$$ 轴旋转一周。我们可以使用柱壳法来计算旋转体的体积。

想象将区间 $$[a, b]$$ 分割成许多小区间，每个小区间的宽度为 $$\Delta x$$。对于每个小区间，我们可以构造一个高度为 $$f(x)$$，半径为 $$x$$ 的薄圆柱壳。这个薄圆柱壳的体积近似为 $$2\pi x f(x) \Delta x$$。

将所有这些薄圆柱壳的体积加起来，并取 $$\Delta x \to 0$$ 时的极限，就可以得到旋转体的体积：

$$V = \int_{a}^{b} 2\pi x f(x) dx = 2\pi \int_{a}^{b} x f(x) dx$$

因此，由平面图形 $$0 \le a \le x \le b, 0 \le y \le f(x)$$ 绕 $$y$$ 轴旋转一周所成的旋转体的体积为 $$V = 2\pi \int_a^b xf(x) dx$$。