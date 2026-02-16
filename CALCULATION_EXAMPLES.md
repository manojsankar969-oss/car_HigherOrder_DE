# 🧮 Complete Calculation Examples - Step by Step

**Purpose**: Show EVERY calculation with real numbers  
**Level**: Learning by doing with examples  
**Format**: Step-by-step worked problems

---

## 📝 Example 1: Basic Calculations for a Typical Car

### Given Data:
```
Car mass:           m = 1200 kg
Spring constant:    k = 25,000 N/m
Damping coefficient: c = 3,000 Ns/m
Initial bump:       x₀ = 0.1 m (10 cm)
```

### Step 1: Calculate Natural Frequency

**Formula:**
```
ωₙ = √(k/m)
```

**Calculation:**
```
ωₙ = √(25,000 / 1,200)
   = √(20.833)
   = 4.564 rad/s

Or in Hz (cycles per second):
f = ωₙ/(2π) = 4.564/(2 × 3.14159)
            = 4.564/6.283
            = 0.727 Hz
```

**What this means:**
- The car naturally wants to oscillate **0.727 times per second**
- Or one complete cycle every **1.38 seconds**
- This is determined only by mass and spring stiffness

---

### Step 2: Calculate Critical Damping

**Formula:**
```
c_crit = 2√(km)
```

**Calculation:**
```
c_crit = 2 × √(25,000 × 1,200)
       = 2 × √(30,000,000)
       = 2 × 5,477.2
       = 10,954.4 Ns/m
```

**What this means:**
- If damping = 10,954.4 Ns/m, the system is **perfectly tuned**
- Our car has c = 3,000 Ns/m, so it's **under-damped** (needs more damping)

---

### Step 3: Calculate Damping Ratio

**Formula:**
```
ζ = c / c_crit
```

**Calculation:**
```
ζ = 3,000 / 10,954.4
  = 0.2739
```

**What this means:**
- ζ = 0.2739 means **27.39% of critical damping**
- Since ζ < 1, system is **UNDERDAMPED** → **BOUNCY** 🌊
- Car will oscillate multiple times before settling
- Each oscillation loses energy to the damper

---

### Step 4: Calculate Damped Natural Frequency

**Formula:**
```
ωd = ωₙ √(1 - ζ²)
```

**Calculation:**
```
ωd = 4.564 × √(1 - 0.2739²)
   = 4.564 × √(1 - 0.0751)
   = 4.564 × √(0.9249)
   = 4.564 × 0.9617
   = 4.388 rad/s

Period: T = 2π/ωd = 6.283/4.388 = 1.432 seconds
```

**What this means:**
- The damping slightly **slows down** the oscillations
- Natural oscillation: 4.564 rad/s
- Damped oscillation: 4.388 rad/s
- Each bounce-cycle takes **1.43 seconds**

---

### Step 5: Calculate Decay Time Constant

**Formula:**
```
τ = 1 / (ζ × ωₙ)
```

**Calculation:**
```
τ = 1 / (0.2739 × 4.564)
  = 1 / 1.250
  = 0.8 seconds
```

**What this means:**
- The **envelope of oscillations** decays with time constant 0.8 seconds
- After τ = 0.8 s: amplitude drops to 37% of original
- After 3τ = 2.4 s: amplitude drops to 5% of original
- After 5τ = 4.0 s: amplitude drops to < 1% of original

---

### Step 6: Estimate Settling Time

**Formula (rough):**
```
t_settle ≈ 4τ to 5τ  for "settled" (< 2% amplitude)
```

**Calculation:**
```
t_settle ≈ 4 × 0.8 = 3.2 seconds
or
t_settle ≈ 5 × 0.8 = 4.0 seconds

So car should settle in about 3-4 seconds
```

**What this means:**
- After hitting the bump, the car bounces
- By **3-4 seconds**, oscillations are small enough to ignore
- After **5 seconds**, motion is essentially over

---

### Step 7: Calculate Velocity at Impact

**Initial condition:** v₀ = 0 (car was at rest when it hit the bump)

But as the car bounces up, maximum velocity is:

**Formula:**
```
v_max = ωd × x₀  (at first peak)
```

**Calculation:**
```
v_max = 4.388 × 0.1 = 0.439 m/s = 1.58 km/h
```

**What this means:**
- Car moves upward at initially about 44 cm/s
- This generates the acceleration the passengers feel

---

### Step 8: Calculate Acceleration (What Passengers Feel)

**At initial impact, acceleration is maximum:**

**Formula:**
```
a_max = k × x₀ / m  (at initial displacement)
```

**Calculation:**
```
a_max = 25,000 × 0.1 / 1,200
      = 2,500 / 1,200
      = 2.083 m/s²
      
In G-forces: 2.083 / 9.81 = 0.212 G
```

**What this means:**
- Passengers experience **0.21 G** of acceleration
- This is mild (normal is 1 G standing on ground)
- Noticeable but comfortable
- This is why car suspensions work!

---

### Step 9: Build the Complete Solution

The displacement as a function of time is:

**Formula (Underdamped case):**
```
x(t) = e^(-ζωₙt) × [A cos(ωd·t) + B sin(ωd·t)]
```

With our numbers:
```
x(t) = e^(-0.2739 × 4.564 × t) × [A cos(4.388·t) + B sin(4.388·t)]
     = e^(-1.250t) × [A cos(4.388·t) + B sin(4.388·t)]
```

Using initial conditions (x₀ = 0.1 m, v₀ = 0):
```
A = 0.1 m
B = (v₀ + ζωₙ×x₀) / ωd = 0.0285 m
```

**Final displacement equation:**
```
x(t) = e^(-1.250t) × [0.1 cos(4.388t) + 0.0285 sin(4.388t)]  meters
```

---

### Step 10: Predict Motion at Key Times

```
t = 0.00 s:  x = 0.100 m  (initial impact)
t = 0.36 s:  x = 0.080 m  (first peak down)
t = 0.71 s:  x = -0.045 m (second peak down)
t = 1.07 s:  x = 0.025 m  (third peak up)
t = 1.43 s:  x = -0.014 m (third peak down)
t = 2.00 s:  x = 0.005 m  (small oscillation)
t = 3.00 s:  x = 0.001 m  (barely moving)
t = 5.00 s:  x ≈ 0.0 m    (settled)
```

---

## 📊 Example 2: Comparing Three Damping Cases

Same car (m=1200, k=25000) but different damping levels:

### Case A: Weak Damping (Underdamped)
```
c = 2,000 Ns/m
ζ = 2000 / 10,954.4 = 0.183 (UNDERDAMPED)
τ = 1 / (0.183 × 4.564) = 1.20 seconds
Settling time ≈ 6 seconds
Behavior: BOUNCY! Multiple oscillations
```

**Motion:** Big bounces that gradually get smaller ✌️

---

### Case B: Optimal Damping (Critically Damped)
```
c = 10,954.4 Ns/m (equal to c_crit)
ζ = 10,954.4 / 10,954.4 = 1.0 (CRITICAL)
τ = 1 / (1.0 × 4.564) = 0.219 seconds
Settling time ≈ 1 second
Behavior: OPTIMAL! Quick stop with no bounce
```

**Motion:** One smooth motion, returns to equilibrium fastest ✓✓

---

### Case C: Excess Damping (Overdamped)
```
c = 15,000 Ns/m
ζ = 15,000 / 10,954.4 = 1.370 (OVERDAMPED)
τ = 1 / (1.370 × 4.564) = 0.160 seconds
Settling time ≈ 2 seconds
Behavior: SLUGGISH! Slow return, like moving through honey
```

**Motion:** Very slow rise and fall, takes forever ⏱️

---

### Comparison Table:

```
                Underdamped    Critical       Overdamped
                (c=2000)       (c=10954)      (c=15000)
─────────────────────────────────────────────────────────
ζ               0.183          1.000          1.370
Settling time   ~6 sec         ~1 sec         ~2 sec
Oscillation     YES (bouncy)   NO (smooth)    NO (sluggish)
Comfort         Poor           EXCELLENT ✓    Good
Response time   Moderate       FAST           Slow
Best for        Cheap cars     Normal cars    Trucks
```

---

## 🔢 Example 3: Energy Analysis

### Initial Energy Calculation:

When car is pushed up by 10 cm:

**Potential Energy stored in spring:**
```
E_spring = ½ k x₀²
         = ½ × 25,000 × (0.1)²
         = ½ × 25,000 × 0.01
         = 125 Joules
```

That's like lifting a 12.5 kg weight 1 meter up!

### Energy Loss Over Time:

Power dissipated by damper:
```
P = c × v²  (depends on velocity)
```

Over one oscillation cycle:
```
Energy lost ≈ c × ωd × A² / (some factor)
```

**For our car:**
- After 1 oscillation (1.43 sec): ~60% energy lost
- After 2 oscillations (2.86 sec): ~85% energy lost
- After 3 oscillations (4.29 sec): ~95% energy lost
- After 5 oscillations (7.15 sec): >99% energy lost → settled

**The damper slowly converts mechanical energy to heat!** 🔥

---

## 🚗 Example 4: Real Driving Scenario

### Scenario: Car hits a speed bump at v=50 km/h

**Data:**
```
Car mass:        m = 1200 kg
Speed:           50 km/h = 13.89 m/s
Bump height:     h = 0.1 m
Suspension:      m = 1200, k = 25000, c = 3000 (our example)
```

### What happens microsecond-by-microsecond:

```
t = 0.00 s:   Wheel touches bump
              Compression force transmitted to body
              
t = 0.02 s:   Car body pushed up 10 cm
              Peak upward velocity: 0.44 m/s
              Acceleration: 2.08 m/s² (passenger feels slight push)
              
t = 0.36 s:   First peak
              Car reaches 8 cm maximum height
              Velocity momentarily = 0
              Acceleration = 0
              
t = 0.71 s:   Car rebounds, now below equilibrium
              Velocity = 0.39 m/s downward
              Acceleration pulls downward
              
t = 1.07 s:   Second peak
              Car is 2.5 cm above equilibrium
              Velocity momentarily = 0
              Smaller than first peak (energy lost to damping)
              
t = 2.00 s:   Third oscillation starting to die
              Motion is barely noticeable
              
t = 4.00 s:   Motion essentially stopped
              Car back to normal driving
              Passengers barely aware anything happened
```

### Energy Accounting:

```
Initial spring energy from 10 cm compression: 125 J

After 1 sec:  ~75 J remains (50 J lost to damper)
After 2 sec:  ~20 J remains (most energy dissipated)
After 3 sec:  ~3 J remains (tiny oscillations)
After 4 sec:  <0.1 J (essentially zero)
```

**Total energy dissipated: 125 J** → converted to heat in shock absorber

---

## 🎓 Example 5: How to Solve the Differential Equation Numerically

### The Equation:
```
m(d²x/dt²) + c(dx/dt) + kx = F(t)
```

### Rearrange to get acceleration:
```
d²x/dt² = [F(t) - c(dx/dt) - kx] / m
        = [F(t) - cv - kx] / m
```

### Convert to two first-order equations:
```
dx/dt = v                    (definition of velocity)
dv/dt = [F(t) - cv - kx] / m (definition of acceleration)
```

### RK4 Algorithm: Solve starting from t=0

**Initial conditions:**
```
t₀ = 0 seconds
x₀ = 0.1 m (10 cm bump)
v₀ = 0 m/s (at rest)
```

**Time step:** Δt = 0.01 seconds

### Iteration 1 (t = 0.00 s → 0.01 s):

**At current state (t=0, x=0.1, v=0):**

Calculate forces:
```
F_external = 0         (free case, no bump force)
F_spring = -kx = -25,000 × 0.1 = -2,500 N
F_damping = -cv = -3,000 × 0 = 0 N
F_total = -2,500 N
```

Acceleration:
```
a = F_total / m = -2,500 / 1,200 = -2.083 m/s²
```

**RK4 Step Calculation** (4 stages):

Stage 1 (k₁):
```
y = [x, v] = [0.1, 0]
k1 = f(t, y) = [v, a] = [0, -2.083]
```

Stage 2 (k₂):
```
y_temp = y + (Δt/2)×k1 = [0.1, 0] + 0.005×[0, -2.083]
       = [0.1, -0.0104]
       
Recalculate forces at y_temp:
a = (-25000×0.1 - 3000×(-0.0104)) / 1200
  = (-2500 + 31.3) / 1200 = -2.057 m/s²
  
k2 = [−0.0104, -2.057]
```

Stage 3 (k₃):
```
Similar calculation...
k3 = [−0.0104, -2.057]
```

Stage 4 (k₄):
```
y_temp = y + Δt×k3
Calculate new acceleration...
k4 = [−0.0207, -2.031]
```

**Update solution:**
```
y_new = y + (Δt/6)×(k1 + 2k2 + 2k3 + k4)
      = [0.1, 0] + (0.01/6)×([0,-2.083] + 2[−0.0104,-2.057] + 2[−0.0104,-2.057] + [−0.0207,-2.031])
      = [0.09896, -0.02065]
```

This gives us:
```
t = 0.01 s:  x = 0.09896 m, v = -0.02065 m/s
```

### Iteration 2 (t = 0.01 s → 0.02 s):

Repeat the same 4 stages with new starting values...

```
t = 0.02 s:  x = 0.09784 m, v = -0.04128 m/s
```

### Continue for 1000 iterations:

```
t = 0.00:  x = 0.10000 m
t = 0.01:  x = 0.09896 m
t = 0.02:  x = 0.09784 m
t = 0.03:  x = 0.09665 m
...
t = 0.35:  x = 0.08000 m  (first peak)
...
t = 0.71:  x = -0.04500 m (second peak)
...
t = 10.00: x ≈ 0.00000 m  (settled)
```

---

## 💡 Quick Reference: Formula Cheat Sheet

| Concept | Formula | Units |
|---------|---------|-------|
| Natural Frequency | ωₙ = √(k/m) | rad/s |
| In Hz | f = ωₙ/(2π) | Hz |
| Critical Damping | c_crit = 2√(km) | Ns/m |
| Damping Ratio | ζ = c/c_crit | - |
| Damped Frequency | ωd = ωₙ√(1-ζ²) | rad/s |
| Time Constant | τ = 1/(ζωₙ) | s |
| Settling Time | t_s ≈ 4/τ | s |
| Spring Force | F_s = -kx | N |
| Damping Force | F_d = -cv | N |
| Max Acceleration | a_max = kx₀/m | m/s² |
| Spring Energy | E = ½kx² | J |

---

## 🎓 Summary: The Big Picture

**What you've learned:**

1. ✅ Every calculation is based on physics principles (Newton's laws)
2. ✅ Mass, spring, and damping work together to create motion
3. ✅ The damping ratio (ζ) determines whether car bounces or settles smoothly
4. ✅ Energy gradually dissipates through the damper
5. ✅ Computer simulations solve equations we can't solve by hand
6. ✅ Engineering is about balance: speed, comfort, safety, cost

**The key insight:** By understanding these calculations, you understand WHY car suspensions work the way they do! 🚗✨

Now go back to the simulator and try changing parameters - you know exactly what will happen! 📈
