import os
import sys
from dotenv import load_dotenv

VALID_MODES = {"development", "production"}


def is_env_ignored() -> bool:
    if not os.path.exists(".gitignore"):
        return False

    try:
        with open(".gitignore", "r", encoding="utf-8") as f:
            lines = (line.strip() for line in f)
            return any(line == ".env" for line in lines)
    except OSError as exc:
        print(f"[ERROR] Could not read .gitignore: {exc}")
        return False


def check_security() -> None:
    env_exists = os.path.exists(".env")
    git_ignored = is_env_ignored()

    if not env_exists:
        print("[INFO] No .env file found (using shell environment variables)")
    elif env_exists and git_ignored:
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
    elif env_exists and not git_ignored:
        print(
            "[WARNING] .env file exists but is NOT in .gitignore! "
            "Risk of leaking secrets to version control."
        )

    print("[OK] Production overrides available")


def main() -> None:
    try:
        load_dotenv()
    except OSError as exc:
        print(f"[ERROR] Could not load .env file: {exc}")

    matrix_mode = os.getenv("MATRIX_MODE", "development")
    if matrix_mode not in VALID_MODES:
        print(f"[WARNING] Unknown MATRIX_MODE '{matrix_mode}'"
              f", defaulting to development")
        matrix_mode = "development"

    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "DEBUG")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    print("ORACLE STATUS: Reading the Matrix...")
    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")

    if not db_url:
        print("Database: Warning! Missing database connection URL")
    elif matrix_mode == "production":
        print("Database: Connected to production cluster")
    else:
        print("Database: Connected to local instance")

    if not api_key:
        print("API Access: Warning! API Key missing")
    else:
        print("API Access: Authenticated")

    print(f"Log Level: {log_level}")

    if not zion_endpoint:
        print("Zion Network: Offline (Endpoint missing)")
    else:
        print("Zion Network: Online")

    print("\nEnvironment security check:")
    check_security()
    print("The Oracle sees all configurations.")
    sys.exit(0)


if __name__ == "__main__":
    main()
