以下是各题的详细解答：

---

**第(1)题：**  
\(\int_0^1 \ln(x + \sqrt{x^2+1})dx\)

设 \(u = \ln(x + \sqrt{x^2+1})\)，\(dv = dx\)，则 \(du = \frac{1 + \frac{x}{\sqrt{x^2+1}}}{x + \sqrt{x^2+1}}dx = \frac{1}{\sqrt{x^2+1}}dx\)，\(v = x\)。

应用分部积分公式：
\[
\int u dv = uv - \int v du
\]
\[
= x \ln(x + \sqrt{x^2+1}) \bigg|_0^1 - \int_0^1 \frac{x}{\sqrt{x^2+1}}dx
\]

计算各部分：
\[
x \ln(x + \sqrt{x^2+1}) \bigg|_0^1 = 1 \cdot \ln(1 + \sqrt{2}) - 0 = \ln(1 + \sqrt{2})
\]
\[
\int_0^1 \frac{x}{\sqrt{x^2+1}}dx = \sqrt{x^2+1} \bigg|_0^1 = \sqrt{2} - 1
\]

所以：
\[
\int_0^1 \ln(x + \sqrt{x^2+1})dx = \ln(1 + \sqrt{2}) - (\sqrt{2} - 1)
\]

结果为：
\[
\boxed{\ln(1+\sqrt{2}) - \sqrt{2} + 1}
\]

---

**第(2)题：**  
\(\int_0^1 x^2 \arctan x dx\)

设 \(u = \arctan x\)，\(dv = x^2 dx\)，则 \(du = \frac{1}{1+x^2}dx\)，\(v = \frac{x^3}{3}\)。

应用分部积分公式：
\[
\int u dv = uv - \int v du
\]
\[
= \frac{x^3}{3} \arctan x \bigg|_0^1 - \int_0^1 \frac{x^3}{3} \cdot \frac{1}{1+x^2}dx
\]

计算各部分：
\[
\frac{x^3}{3} \arctan x \bigg|_0^1 = \frac{1}{3} \cdot \frac{\pi}{4} = \frac{\pi}{12}
\]
\[
\int_0^1 \frac{x^3}{1+x^2}dx = \int_0^1 \left(x - \frac{x}{1+x^2}\right)dx = \left[\frac{x^2}{2} - \frac{1}{2}\ln(1+x^2)\right]_0^1 = \frac{1}{2} - \frac{1}{2}\ln 2
\]

所以：
\[
\int_0^1 x^2 \arctan x dx = \frac{\pi}{12} - \frac{1}{3}\left(\frac{1}{2} - \frac{1}{2}\ln 2\right)
\]
\[
= \frac{\pi}{12} - \frac{1}{6} + \frac{\ln 2}{6}
\]

结果为：
\[
\boxed{\frac{\pi}{12} - \frac{1}{6} + \frac{\ln 2}{6}}
\]

---

**第(3)题：**  
\(\int_{-\frac{\pi}{3}}^{\frac{\pi}{3}} e^x \cos x dx\)

使用分部积分法：
\[
\int e^x \cos x dx = e^x \sin x - \int e^x \sin x dx
\]
\[
\int e^x \sin x dx = -e^x \cos x + \int e^x \cos x dx
\]

代入回原式：
\[
\int e^x \cos x dx = e^x \sin x + e^x \cos x - \int e^x \cos x dx
\]
\[
2 \int e^x \cos x dx = e^x (\sin x + \cos x) + C
\]
\[
\int e^x \cos x dx = \frac{e^x (\sin x + \cos x)}{2} + C
\]

计算定积分：
\[
\left[\frac{e^x (\sin x + \cos x)}{2}\right]_{-\frac{\pi}{3}}^{\frac{\pi}{3}}
\]
\[
= \frac{e^{\frac{\pi}{3}} (\sin \frac{\pi}{3} + \cos \frac{\pi}{3})}{2} - \frac{e