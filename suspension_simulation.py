"""
Car Suspension System Simulation
A project demonstrating Higher Order Differential Equations

This program simulates a car suspension system modeled as a spring-mass-damper system.
The governing equation is: m(d²x/dt²) + c(dx/dt) + kx = F(t)

Author: Student Mini Project
Date: February 2026
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import sys
import os

# Set up plotting style
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (12, 10)
plt.rcParams['font.size'] = 10


class CarSuspension:
    """
    A class to model and simulate a car suspension system.
    """
    
    def __init__(self, mass, damping, spring_constant):
        """
        Initialize the suspension system parameters.
        
        Parameters:
        -----------
        mass : float
            Mass of the car body (kg)
        damping : float
            Damping coefficient (Ns/m)
        spring_constant : float
            Spring stiffness (N/m)
            
        Raises:
        -------
        ValueError: If parameters are invalid
        """
        # Validate inputs
        if not isinstance(mass, (int, float)) or mass <= 0:
            raise ValueError(f"Mass must be a positive number, got {mass}")
        if not isinstance(damping, (int, float)) or damping < 0:
            raise ValueError(f"Damping must be non-negative, got {damping}")
        if not isinstance(spring_constant, (int, float)) or spring_constant <= 0:
            raise ValueError(f"Spring constant must be positive, got {spring_constant}")
        
        self.m = float(mass)
        self.c = float(damping)
        self.k = float(spring_constant)
        
        # Calculate derived parameters
        try:
            self.omega_n = np.sqrt(self.k / self.m)  # Natural frequency
            self.c_critical = 2 * np.sqrt(self.k * self.m)  # Critical damping
            self.zeta = self.c / self.c_critical  # Damping ratio
            
            # Validate derived parameters
            if not np.isfinite(self.omega_n) or not np.isfinite(self.zeta):
                raise ValueError("Calculated parameters are not finite")
        except Exception as e:
            raise ValueError(f"Error calculating system parameters: {e}")
        
        # Determine damping type
        if self.zeta < 1:
            self.damping_type = "Underdamped"
        elif abs(self.zeta - 1) < 1e-6:
            self.damping_type = "Critically Damped"
        else:
            self.damping_type = "Overdamped"
    
    def display_parameters(self):
        """Display system parameters and characteristics."""
        print("=" * 60)
        print("CAR SUSPENSION SYSTEM PARAMETERS")
        print("=" * 60)
        print(f"Mass (m):                    {self.m:.2f} kg")
        print(f"Damping Coefficient (c):     {self.c:.2f} Ns/m")
        print(f"Spring Constant (k):         {self.k:.2f} N/m")
        print(f"\nNatural Frequency (ω_n):     {self.omega_n:.4f} rad/s")
        print(f"Critical Damping (c_crit):   {self.c_critical:.2f} Ns/m")
        print(f"Damping Ratio (ζ):           {self.zeta:.4f}")
        print(f"\nDamping Type:                {self.damping_type}")
        print("=" * 60)
        print()
    
    def homogeneous_solution(self, x0, v0, t_max=10, n_points=1000):
        """
        Solve the homogeneous equation: m(d²x/dt²) + c(dx/dt) + kx = 0
        
        Parameters:
        -----------
        x0 : float
            Initial displacement (m)
        v0 : float
            Initial velocity (m/s)
        t_max : float
            Maximum simulation time (s)
        n_points : int
            Number of time points
            
        Returns:
        --------
        t : array
            Time array
        x : array
            Displacement array
        v : array
            Velocity array
            
        Raises:
        -------
        ValueError: If parameters are invalid
        Exception: If integration fails
        """
        try:
            # Validate inputs
            if not isinstance(x0, (int, float)):
                raise ValueError(f"Initial displacement must be numeric, got {x0}")
            if not isinstance(v0, (int, float)):
                raise ValueError(f"Initial velocity must be numeric, got {v0}")
            if t_max <= 0 or n_points <= 1:
                raise ValueError(f"t_max must be positive and n_points > 1")
            
            # Define the system of first-order ODEs
            def system(state, t):
                x, v = state
                dxdt = v
                dvdt = -(self.c/self.m) * v - (self.k/self.m) * x
                return [dxdt, dvdt]
            
            # Initial conditions
            state0 = [x0, v0]
            
            # Time array
            t = np.linspace(0, t_max, n_points)
            
            # Solve ODE
            solution = odeint(system, state0, t, full_output=False)
            
            if solution is None or len(solution) == 0:
                raise Exception("ODE integration returned empty solution")
            
            x = solution[:, 0]
            v = solution[:, 1]
            
            # Check for NaN or Inf
            if np.any(np.isnan(x)) or np.any(np.isinf(x)):
                raise Exception("Solution contains NaN or Inf values")
            
            return t, x, v
        except Exception as e:
            print(f"Error in homogeneous solution: {e}")
            raise
    
    def non_homogeneous_solution(self, x0, v0, force_function, t_max=10, n_points=1000):
        """
        Solve the non-homogeneous equation: m(d²x/dt²) + c(dx/dt) + kx = F(t)
        
        Parameters:
        -----------
        x0 : float
            Initial displacement (m)
        v0 : float
            Initial velocity (m/s)
        force_function : callable
            External force as a function of time F(t)
        t_max : float
            Maximum simulation time (s)
        n_points : int
            Number of time points
            
        Returns:
        --------
        t : array
            Time array
        x : array
            Displacement array
        v : array
            Velocity array
            
        Raises:
        -------
        ValueError: If parameters are invalid
        TypeError: If force_function is not callable
        Exception: If integration fails
        """
        try:
            # Validate inputs
            if not callable(force_function):
                raise TypeError("force_function must be callable")
            if not isinstance(x0, (int, float)):
                raise ValueError(f"Initial displacement must be numeric, got {x0}")
            if not isinstance(v0, (int, float)):
                raise ValueError(f"Initial velocity must be numeric, got {v0}")
            if t_max <= 0 or n_points <= 1:
                raise ValueError(f"t_max must be positive and n_points > 1")
            
            # Define the system of first-order ODEs with forcing
            def system(state, t):
                x, v = state
                try:
                    F = force_function(t)
                    if not isinstance(F, (int, float)):
                        raise ValueError(f"Force function must return numeric value, got {type(F)}")
                except Exception as e:
                    print(f"Error evaluating force function at t={t}: {e}")
                    raise
                
                dxdt = v
                dvdt = (F - self.c * v - self.k * x) / self.m
                return [dxdt, dvdt]
            
            # Initial conditions
            state0 = [x0, v0]
            
            # Time array
            t = np.linspace(0, t_max, n_points)
            
            # Solve ODE
            solution = odeint(system, state0, t, full_output=False)
            
            if solution is None or len(solution) == 0:
                raise Exception("ODE integration returned empty solution")
            
            x = solution[:, 0]
            v = solution[:, 1]
            
            # Check for NaN or Inf
            if np.any(np.isnan(x)) or np.any(np.isinf(x)):
                raise Exception("Solution contains NaN or Inf values")
            
            return t, x, v
        except Exception as e:
            print(f"Error in non-homogeneous solution: {e}")
            raise


def save_plot(filename, dpi=300):
    """
    Save plot with error handling.
    
    Parameters:
    -----------
    filename : str
        Path to save the plot
    dpi : int
        DPI for the saved image
    """
    try:
        # Ensure directory exists
        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
        
        plt.savefig(filename, dpi=dpi, bbox_inches='tight')
        print(f"✓ Plot saved as '{os.path.basename(filename)}'")
    except Exception as e:
        print(f"✗ Error saving plot: {e}")
    finally:
        plt.close()


def compare_damping_cases():
    """
    Compare underdamped, critically damped, and overdamped responses.
    """
    
    try:
        # Common parameters
        m = 1000  # kg
        k = 20000  # N/m
        
        # Initial conditions
        x0 = 0.1  # 10 cm initial displacement
        v0 = 0.0  # Released from rest
        
        # Calculate critical damping
        c_critical = 2 * np.sqrt(k * m)
        
        # Three damping cases
        c_under = 0.3 * c_critical  # Underdamped
        c_critical_exact = c_critical  # Critically damped
        c_over = 2.0 * c_critical  # Overdamped
        
        # Create suspension objects
        suspension_under = CarSuspension(m, c_under, k)
        suspension_critical = CarSuspension(m, c_critical_exact, k)
        suspension_over = CarSuspension(m, c_over, k)
        
        # Solve for each case
        t1, x1, v1 = suspension_under.homogeneous_solution(x0, v0, t_max=5)
        t2, x2, v2 = suspension_critical.homogeneous_solution(x0, v0, t_max=5)
        t3, x3, v3 = suspension_over.homogeneous_solution(x0, v0, t_max=5)
        
        # Plot comparison
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
        
        # Displacement plot
        ax1.plot(t1, x1*100, 'b-', linewidth=2, label=f'Underdamped (ζ = {suspension_under.zeta:.2f})')
        ax1.plot(t2, x2*100, 'g-', linewidth=2, label=f'Critically Damped (ζ = {suspension_critical.zeta:.2f})')
        ax1.plot(t3, x3*100, 'r-', linewidth=2, label=f'Overdamped (ζ = {suspension_over.zeta:.2f})')
        ax1.axhline(y=0, color='k', linestyle='--', alpha=0.3)
        ax1.set_xlabel('Time (seconds)', fontsize=12)
        ax1.set_ylabel('Displacement (cm)', fontsize=12)
        ax1.set_title('Comparison of Damping Cases - Displacement vs Time', fontsize=14, fontweight='bold')
        ax1.legend(fontsize=11)
        ax1.grid(True, alpha=0.3)
        
        # Velocity plot
        ax2.plot(t1, v1, 'b-', linewidth=2, label=f'Underdamped (ζ = {suspension_under.zeta:.2f})')
        ax2.plot(t2, v2, 'g-', linewidth=2, label=f'Critically Damped (ζ = {suspension_critical.zeta:.2f})')
        ax2.plot(t3, v3, 'r-', linewidth=2, label=f'Overdamped (ζ = {suspension_over.zeta:.2f})')
        ax2.axhline(y=0, color='k', linestyle='--', alpha=0.3)
        ax2.set_xlabel('Time (seconds)', fontsize=12)
        ax2.set_ylabel('Velocity (m/s)', fontsize=12)
        ax2.set_title('Comparison of Damping Cases - Velocity vs Time', fontsize=14, fontweight='bold')
        ax2.legend(fontsize=11)
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        output_path = 'c:/workspace/maths_new_real/car_suspension_project/damping_comparison.png'
        save_plot(output_path)
        
    except Exception as e:
        print(f"✗ Error in damping comparison: {e}")


def simulate_speed_breaker():
    """
    Simulate a car hitting a speed breaker (impulse force).
    """
    print("\n" + "=" * 60)
    print("SIMULATING CAR HITTING A SPEED BREAKER")
    print("=" * 60 + "\n")
    
    try:
        # Car parameters (typical sedan)
        m = 1200  # kg
        c = 3000  # Ns/m (good shock absorbers)
        k = 25000  # N/m
        
        # Create suspension system
        suspension = CarSuspension(m, c, k)
        suspension.display_parameters()
        
        # Define impulse force (speed breaker)
        def speed_breaker_force(t):
            """Impulse force occurring between 0 and 0.1 seconds"""
            if 0 <= t <= 0.1:
                return 5000  # 5000 N force
            else:
                return 0
        
        # Initial conditions (car at rest)
        x0 = 0.0
        v0 = 0.0
        
        # Solve
        t, x, v = suspension.non_homogeneous_solution(x0, v0, speed_breaker_force, t_max=5)
        
        # Calculate acceleration
        a = np.gradient(v, t)
        
        # Create plots
        fig, axes = plt.subplots(3, 1, figsize=(12, 12))
        
        # Displacement
        axes[0].plot(t, x*100, 'b-', linewidth=2)
        axes[0].axhline(y=0, color='k', linestyle='--', alpha=0.3)
        axes[0].set_ylabel('Displacement (cm)', fontsize=12)
        axes[0].set_title('Car Response to Speed Breaker - Displacement', fontsize=14, fontweight='bold')
        axes[0].grid(True, alpha=0.3)
        axes[0].fill_between([0, 0.1], axes[0].get_ylim()[0], axes[0].get_ylim()[1], 
                              alpha=0.2, color='red', label='Speed Breaker Impact')
        axes[0].legend()
        
        # Velocity
        axes[1].plot(t, v, 'g-', linewidth=2)
        axes[1].axhline(y=0, color='k', linestyle='--', alpha=0.3)
        axes[1].set_ylabel('Velocity (m/s)', fontsize=12)
        axes[1].set_title('Car Response to Speed Breaker - Velocity', fontsize=14, fontweight='bold')
        axes[1].grid(True, alpha=0.3)
        axes[1].fill_between([0, 0.1], axes[1].get_ylim()[0], axes[1].get_ylim()[1], 
                              alpha=0.2, color='red', label='Speed Breaker Impact')
        axes[1].legend()
        
        # Acceleration
        axes[2].plot(t, a, 'r-', linewidth=2)
        axes[2].axhline(y=0, color='k', linestyle='--', alpha=0.3)
        axes[2].set_xlabel('Time (seconds)', fontsize=12)
        axes[2].set_ylabel('Acceleration (m/s²)', fontsize=12)
        axes[2].set_title('Car Response to Speed Breaker - Acceleration', fontsize=14, fontweight='bold')
        axes[2].grid(True, alpha=0.3)
        axes[2].fill_between([0, 0.1], axes[2].get_ylim()[0], axes[2].get_ylim()[1], 
                              alpha=0.2, color='red', label='Speed Breaker Impact')
        axes[2].legend()
        
        plt.tight_layout()
        
        output_path = 'c:/workspace/maths_new_real/car_suspension_project/speed_breaker_response.png'
        save_plot(output_path)
        
    except Exception as e:
        print(f"✗ Error in speed breaker simulation: {e}")


def simulate_bumpy_road():
    """
    Simulate a car on a bumpy road (periodic force).
    """
    print("\n" + "=" * 60)
    print("SIMULATING CAR ON BUMPY ROAD")
    print("=" * 60 + "\n")
    
    try:
        # Car parameters
        m = 1200  # kg
        c = 3000  # Ns/m
        k = 25000  # N/m
        
        # Create suspension system
        suspension = CarSuspension(m, c, k)
        
        # Define periodic force (bumpy road)
        omega_force = 8  # rad/s (frequency of road bumps)
        F0 = 2000  # N (amplitude)
        
        def bumpy_road_force(t):
            """Sinusoidal force representing periodic bumps"""
            return F0 * np.sin(omega_force * t)
        
        # Initial conditions
        x0 = 0.0
        v0 = 0.0
        
        # Solve
        t, x, v = suspension.non_homogeneous_solution(x0, v0, bumpy_road_force, t_max=10)
        
        # Calculate the force at each time point
        force = np.array([bumpy_road_force(ti) for ti in t])
        
        # Create plot
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
        
        # Force input
        ax1.plot(t, force/1000, 'orange', linewidth=2)
        ax1.axhline(y=0, color='k', linestyle='--', alpha=0.3)
        ax1.set_ylabel('External Force (kN)', fontsize=12)
        ax1.set_title('Bumpy Road Input Force (Periodic)', fontsize=14, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        
        # Displacement response
        ax2.plot(t, x*100, 'b-', linewidth=2)
        ax2.axhline(y=0, color='k', linestyle='--', alpha=0.3)
        ax2.set_xlabel('Time (seconds)', fontsize=12)
        ax2.set_ylabel('Displacement (cm)', fontsize=12)
        ax2.set_title('Car Displacement Response on Bumpy Road', fontsize=14, fontweight='bold')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        output_path = 'c:/workspace/maths_new_real/car_suspension_project/bumpy_road_response.png'
        save_plot(output_path)
        
        # Analyze resonance
        road_freq_hz = omega_force / (2 * np.pi)
        natural_freq_hz = suspension.omega_n / (2 * np.pi)
        
        print(f"\nRoad bump frequency: {road_freq_hz:.2f} Hz")
        print(f"Natural frequency:   {natural_freq_hz:.2f} Hz")
        
        freq_ratio = omega_force / suspension.omega_n
        if abs(freq_ratio - 1.0) < 0.2:
            print("\n⚠ WARNING: Road frequency is close to natural frequency!")
            print("   This can cause RESONANCE and large amplitudes.")
            print(f"   Frequency ratio (ω_force/ω_n): {freq_ratio:.2f}")
        else:
            print("\n✓ Road frequency is sufficiently different from natural frequency.")
            print(f"   Frequency ratio (ω_force/ω_n): {freq_ratio:.2f}")
        
    except Exception as e:
        print(f"✗ Error in bumpy road simulation: {e}")


def main():
    """
    Main function to run all simulations.
    """
    print("\n" + "=" * 60)
    print("CAR SUSPENSION SYSTEM SIMULATION")
    print("Higher Order Differential Equations Project")
    print("=" * 60)
    
    try:
        # Run all simulations
        print("\n[1/3] Comparing Damping Cases...")
        compare_damping_cases()
        
        print("\n[2/3] Simulating Speed Breaker Impact...")
        simulate_speed_breaker()
        
        print("\n[3/3] Simulating Bumpy Road...")
        simulate_bumpy_road()
        
        print("\n" + "=" * 60)
        print("ALL SIMULATIONS COMPLETE!")
        print("=" * 60)
        print("\nGenerated files:")
        print("  1. damping_comparison.png")
        print("  2. speed_breaker_response.png")
        print("  3. bumpy_road_response.png")
        print("\nThese plots demonstrate:")
        print("  ✓ How damping affects car motion")
        print("  ✓ Response to sudden bumps (impulse)")
        print("  ✓ Response to periodic disturbances")
        print("\n" + "=" * 60 + "\n")
        
    except Exception as e:
        print(f"\n✗ Simulation failed with error: {e}")
        sys.exit(1)



if __name__ == "__main__":
    main()
