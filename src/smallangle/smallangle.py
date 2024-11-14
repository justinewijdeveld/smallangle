import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def smallangle():
    """Generate values for sine or tangent between 0 and 2π."""
    pass

@smallangle.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help='Number of steps between 0 and 2π',
    show_default=True,
    type=int)
def sin(number):
    """Calculate the sine of values between 0 and 2π.

    Args:
        number (int): Number of steps between 0 and 2π
    """    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@smallangle.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help='Number of steps between 0 and 2π',
    show_default=True,
    type=int)
def tan(number):
    """Calculate the tangent of values between 0 and 2π.

    Args:
        number (int): Number of steps between 0 and 2π
    """    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    smallangle()