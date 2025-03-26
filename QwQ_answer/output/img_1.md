4.  计算由椭圆 $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ 所围成的图形分别绕 $x$ 轴、$y$ 轴旋转一周而成的旋转体（旋转椭球体）的体积.
 解：
 
 绕 $x$ 轴旋转时，使用圆盘法。椭圆方程可以写为 $y = \pm b\sqrt{1 - \frac{x^2}{a^2}}$，所以半径是 $|y| = b\sqrt{1 - \frac{x^2}{a^2}}$。体积为：
 
 $$
 V_x = \pi \int_{-a}^a \left[b\sqrt{1 - \frac{x^2}{a^2}}\right]^2 dx 
 $$
 $$
 = \pi b^2 \int_{-a}^a \left(1 - \frac{x^2}{a^2}\right) dx 
 $$
 利用积分对称性，化简为：
 $$
 V_x = 2\pi b^2 \int_{0}^a \left(1 - \frac{x^2}{a^2}\right) dx 
 $$
 计算积分：
 $$
 \int_{0}^a \left(1 - \frac{x^2}{a^2}\right) dx = \left[x - \frac{x^3}{3a^2}\right]_0^a = a - \frac{a}{3} = \frac{2a}{3}
 $$
 因此，绕 $x$ 轴旋转的体积为：
 $$
 V_x = 2\pi b^2 \cdot \frac{2a}{3} = \frac{4}{3} \pi ab^2
 $$
 
 绕 $y$ 轴旋转时，使用圆盘法。椭圆方程可以写为 $x = \pm a\sqrt{1 - \frac{y^2}{b^2}}$，半径是 $|x| = a\sqrt{1 - \frac{y^2}{b^2}}$。体积为：
 
 $$
 V_y = \pi \int_{-b}^b \left[a\sqrt{1 - \frac{y^2}{b^2}}\right]^2 dy 
 $$
 $$
 = \pi a^2 \int_{-b}^b \left(1 - \frac{y^2}{b^2}\right) dy 
 $$
 同样利用对称性化简为：
 $$
 V_y = 2\pi a^2 \int_{0}^b \left(1 - \frac{y^2}{b^2}\right) dy 
 $$
 计算积分：
 $$
 \int_{0}^b \left(1 - \frac{y^2}{b^2}\right) dy = \left[y - \frac{y^3}{3b^2}\right]_0^b = b - \frac{b}{3} = \frac{2b}{3}
 $$
 因此，绕 $y$ 轴旋转的体积为：
 $$
 V_y = 2\pi a^2 \cdot \frac{2b}{3} = \frac{4}{3} \pi a^2 b
 $$
 
 所以，绕 $x$ 轴旋转的体积是 $\frac{4}{3}\pi ab^2$，绕 $y$ 轴旋转的体积是 $\frac{4}{3}\pi a^2 b$。