import importlib.metadata


def check_dependencies() -> bool:
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    required: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
    }

    missing: list[str] = []
    all_ok = True

    for lib, desc in required.items():
        try:
            version = importlib.metadata.version(lib)
            print(f"[OK] {lib} ({version}) - {desc}")
        except importlib.metadata.PackageNotFoundError:
            print(f"[MISSING] {lib} - Required for the Matrix")
            missing.append(lib)
            all_ok = False

    if not all_ok:
        print("\nERROR: Incomplete loading. Programs missing.")
        print("To fix with pip: pip install -r requirements.txt")
        print("To fix with Poetry: poetry install")
        return False
    return True


def run_analysis() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    data_size = 1000
    print(f"Processing {data_size} data points...")

    raw_data = np.random.standard_normal((data_size, 2))
    df = pd.DataFrame(raw_data, columns=["Signal A", "Signal B"])

    print("Generating visualization...")
    plt.figure(figsize=(10, 6))
    plt.hexbin(df["Signal A"], df["Signal B"], gridsize=30, cmap="Greens")
    plt.title("Matrix Signal Analysis")
    plt.colorbar(label="Intensity")

    output_file = "matrix_analysis.png"
    try:
        plt.savefig(output_file)
    except OSError as exc:
        print(f"[ERROR] Could not save visualization: {exc}")
        return

    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


def show_management_diff() -> None:
    print("\n" + "=" * 40)
    print("KNOWLEDGE TRANSFER: PIP VS POETRY")
    print("=" * 40)
    print("PIP: Standard, imperative, uses requirements.txt.")
    print("POETRY: Modern, declarative, handles environments and lockfiles.")
    print("Poetry ensures that every Alchemist has the EXACT same versions.")
    print("=" * 40)


def main() -> None:
    if check_dependencies():
        run_analysis()
        show_management_diff()


if __name__ == "__main__":
    main()
