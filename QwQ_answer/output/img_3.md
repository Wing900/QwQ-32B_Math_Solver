1. 求以半径为 $R$ 的圆为底，平行且长度等于底圆直径的线段为顶，高为 $h$ 的正劈锥体 (图 9.19) 的体积。

解：
设底圆位于 $z=0$ 平面上，其方程为 $x^2 + y^2 = R^2$。设顶线位于 $z=h$ 平面上，且平行于 $x$ 轴，其长度为 $2R$，则顶线可表示为 $-R \le x \le R, y = 0, z = h$。

对于任意 $0 \le z \le h$，考虑横截面与平面 $z = z_0$ 的交线。该交线是一个椭圆，其半长轴为 $R$，半短轴为 $R\sqrt{1-\frac{z_0}{h}}$。因此，该椭圆的面积为 $\pi R^2 \sqrt{1 - \frac{z_0}{h}}$。

故正劈锥体的体积为
$$ V = \int_0^h \pi R^2 \sqrt{1 - \frac{z}{h}} dz = \pi R^2 \int_0^h \sqrt{1 - \frac{z}{h}} dz$$
令 $u = 1 - \frac{z}{h}$，则 $du = -\frac{1}{h} dz$，且 $z = 0$ 时 $u = 1$，$z = h$ 时 $u = 0$。因此
$$ V = \pi R^2 \int_1^0 \sqrt{u} (-h) du = \pi R^2 h \int_0^1 \sqrt{u} du = \pi R^2 h \left[ \frac{2}{3} u^{3/2} \right]_0^1 = \frac{2}{3} \pi R^2 h$$

2. 求由两个圆柱面 $x^2 + y^2 = a^2$ 与 $z^2 + x^2 = a^2$ 所围立体 (图 9.20) 的体积。

解：
所围立体的体积可以表示为
$$ V = 8 \int_0^a \int_0^{\sqrt{a^2 - x^2}} \sqrt{a^2 - x^2} dy dx $$
其中因子 8 是因为立体关于三个坐标平面都是对称的。首先计算内层积分：
$$ \int_0^{\sqrt{a^2 - x^2}} \sqrt{a^2 - x^2} dy = \sqrt{a^2 - x^2} \int_0^{\sqrt{a^2 - x^2}} dy = \sqrt{a^2 - x^2} \cdot \sqrt{a^2 - x^2} = a^2 - x^2 $$
因此，
$$ V = 8 \int_0^a (a^2 - x^2) dx = 8 \left[ a^2 x - \frac{1}{3} x^3 \right]_0^a = 8 \left( a^3 - \frac{1}{3} a^3 \right) = 8 \cdot \frac{2}{3} a^3 = \frac{16}{3} a^3 $$

3. 求由椭球面 $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$ 所围立体 (椭球) 的体积。

解：
可以通过三重积分求解椭球的体积。
$$V = \iiint_D dxdydz$$
其中 $D$ 是椭球面 $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} \le 1$ 所围的区域。
引入坐标变换：
$$ x = au, \quad y = bv, \quad z = cw $$
则有 $u^2 + v^2 + w^2 \le 1$，即单位球面。雅可比行列式为
$$ J = \frac{\partial(x, y, z)}{\partial(u, v, w)} = \begin{vmatrix} a & 0 & 0 \\ 0 & b & 0 \\ 0 & 0 & c \end{vmatrix} = abc$$
因此
$$V = \iiint_{u^2 + v^2 + w^2 \le 1} |J| dudvdw = abc \iiint_{u^2 + v^2 + w^2 \le 1} dudvdw = abc \cdot \frac{4}{3} \pi (1)^3 = \frac{4}{3} \pi abc$$
这里利用了单位球的体积为 $\frac{4}{3}\pi$。