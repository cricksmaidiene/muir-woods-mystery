"""A set of configuration variables for the detective game."""

from dotenv import load_dotenv
from pathlib import Path
import os

PHASE_2_UNLOCKED: bool = False

dotenv_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")