import os

JOKE = "My AI coding agent deleted 2,000 lines of dead code. Turns out the dead code was the payment system."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
# Create the output dir when running outside the grader container.
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
