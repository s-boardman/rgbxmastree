import sys
from gpiozero.exc import NativePinFactoryFallback, PinFactoryFallback
import typer

from .commands.color_shuffle import app as color_shuffle_app


# Setup warning filtering
if not sys.warnoptions:
    import warnings

    warnings.filterwarnings("ignore", category=PinFactoryFallback)
    warnings.filterwarnings("ignore", category=NativePinFactoryFallback)

app = typer.Typer()

app.add_typer(color_shuffle_app)
