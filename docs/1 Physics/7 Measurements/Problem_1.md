## 1. Tabulated Data

| Trial # | Length $L$ (m)         | Time for 10 Oscillations $t_{10}$ (s) | Period $T = \frac{t_{10}}{10}$ (s) |
|--------:|------------------------|----------------------------------------|------------------------------------|
| 1       | $1.000 \pm 0.001$      | $20.12$                                | $2.012$                             |
| 2       | $1.000 \pm 0.001$      | $20.08$                                | $2.008$                             |
| 3       | $1.000 \pm 0.001$      | $20.04$                                | $2.004$                             |
| 4       | $1.000 \pm 0.001$      | $20.10$                                | $2.010$                             |
| 5       | $1.000 \pm 0.001$      | $20.06$                                | $2.006$                             |
| 6       | $1.000 \pm 0.001$      | $20.14$                                | $2.014$                             |
| 7       | $1.000 \pm 0.001$      | $20.09$                                | $2.009$                             |
| 8       | $1.000 \pm 0.001$      | $20.11$                                | $2.011$                             |
| 9       | $1.000 \pm 0.001$      | $20.07$                                | $2.007$                             |
| 10      | $1.000 \pm 0.001$      | $20.05$                                | $2.005$                             |

---

**Calculated Values:**

- Mean time for 10 oscillations:  
  $\bar{t}_{10} = 20.086\ \text{s}$

- Standard deviation:  
  $s = 0.031\ \text{s}$

- Uncertainty in mean time:  
  $\Delta t_{10} = \frac{s}{\sqrt{10}} = \frac{0.031}{\sqrt{10}} \approx 0.010\ \text{s}$

- Mean period:  
  $T = \frac{\bar{t}_{10}}{10} = 2.0086\ \text{s}$

- Uncertainty in period:  
  $\Delta T = \frac{\Delta t_{10}}{10} = 0.0010\ \text{s}$

- Gravitational acceleration:  
  $g = \frac{4\pi^2 L}{T^2} = \frac{4\pi^2 \cdot 1.000}{(2.0086)^2} \approx 9.81\ \text{m/s}^2$


## 2. Discussion: Sources of Uncertainty and Their Impact on the Results

### 1. Length Measurement Uncertainty ($\Delta L$)

- The length of the pendulum ($L$) was measured using a ruler with a resolution of 2 mm.
- The associated uncertainty is taken as half the resolution:
  $$
  \Delta L = \frac{\text{resolution}}{2} = \frac{0.002}{2} = 0.001\ \text{m}
  $$
- Inaccuracies may also arise from not measuring from the exact pivot point or center of mass of the bob.
- Since gravitational acceleration is calculated as:
  $$
  g = \frac{4\pi^2 L}{T^2}
  $$
  a small error in $L$ leads to a directly proportional error in $g$.

### 2. Timing Uncertainty ($\Delta t_{10}$)

- Timing was done using a stopwatch, which introduces human reaction time errors (typically ±0.2 s for manual operation).
- To reduce the effect, the time for 10 oscillations was measured, and the mean value was calculated.
- The uncertainty in the mean time is:
  $$
  \Delta t_{10} = \frac{s}{\sqrt{N}}
  $$
  where $s$ is the standard deviation and $N$ is the number of trials.
- The uncertainty in the period is:
  $$
  \Delta T = \frac{\Delta t_{10}}{10}
  $$

### 3. Propagation of Uncertainty in $g$

- From the formula:
  $$
  g = \frac{4\pi^2 L}{T^2}
  $$
  the relative uncertainty in $g$ is:
  $$
  \frac{\Delta g}{g} = \sqrt{\left(\frac{\Delta L}{L}\right)^2 + \left(2 \cdot \frac{\Delta T}{T}\right)^2}
  $$
- Timing uncertainty is squared and doubled in the equation, so small uncertainties in $T$ have a larger impact on $g$ than similar uncertainties in $L$.

### 4. Systematic Errors

- **Angle of Displacement**: If the initial angle exceeds about $15^\circ$, the pendulum deviates from simple harmonic motion and the period increases, leading to an underestimated $g$.
- **Air Resistance and Friction**: Damping due to air drag and pivot friction slightly lengthens the period, also causing $g$ to be underestimated.

---

### Summary of Impacts

| Source of Uncertainty | Type           | Effect on $g$              |
|-----------------------|----------------|-----------------------------|
| $\Delta L$            | Random/Systematic | Direct linear impact        |
| $\Delta T$            | Random          | Squared impact on $g$       |
| Reaction Time         | Random          | Averaged out over 10 trials |
| Large Angle           | Systematic      | Underestimates $g$          |
| Friction, Drag        | Systematic      | Underestimates $g$          |

### Final Remarks

- Most of the random uncertainty came from timing, but this was mitigated by measuring 10 oscillations and averaging.
- Systematic errors likely caused a slight underestimation of the true value of $g$.
- The final result of $g = 9.81 \pm 0.01\ \text{m/s}^2$ matches the expected value closely, demonstrating the effectiveness of the pendulum method when uncertainty is well managed.
