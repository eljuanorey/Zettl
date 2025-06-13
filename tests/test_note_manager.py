import os
import sys
import datetime
from pathlib import Path
import importlib.util
import types

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "zettl.commands.note_manager",
    ROOT / "zettl" / "commands" / "note_manager.py",
)

# Provide a minimal fake 'zettl' package required by note_manager
fake_zettl = types.ModuleType("zettl")
fake_zettl.os = os
fake_zettl.datetime = datetime
sys.modules.setdefault("zettl", fake_zettl)

note_manager = importlib.util.module_from_spec(spec)
spec.loader.exec_module(note_manager)

def test_custom_naming_convention(monkeypatch, tmp_path):
    fixed_time = datetime.datetime(2023, 1, 2, 15, 30)
    class FixedDateTime(datetime.datetime):
        @classmethod
        def now(cls, tz=None):
            return fixed_time
    monkeypatch.setattr(note_manager, 'datetime', FixedDateTime)
    naming = "%Y-%m-%d_%H%M.md"
    note_manager.create_markdown_note(str(tmp_path), "Test Note", naming)
    expected = fixed_time.strftime(naming)
    assert (tmp_path / expected).exists()
