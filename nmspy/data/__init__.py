import importlib
import os

FUNC_OFFSETS: dict[str, int]

# Get the binary hash
binary_hash = os.environ.get("NMS_BINARY_HASH")
if binary_hash:
    offsets = importlib.import_module(f"nmspy.data.{binary_hash}.func_offsets")
    if offsets.__binary_hash__ != binary_hash:
        raise ImportError(
            f"Binary hash in offsets file ({offsets.__binaryhash__}) doesn't "
            f"match the one provided ({binary_hash})"
        )
    FUNC_OFFSETS = offsets.FUNC_OFFSETS
else:
    print("No binary hash provided... There will be issues...")
    FUNC_OFFSETS = {}
