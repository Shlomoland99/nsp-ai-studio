import argparse
from .contracts import CreativeJob
from .registry import Registry
from .router import CapabilityRouter

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--capability", action="append", required=True)
    p.add_argument("--local-only", action="store_true")
    args = p.parse_args()
    provider = CapabilityRouter(Registry()).route(CreativeJob("cli", tuple(args.capability), local_only=args.local_only))
    print(provider)
if __name__ == "__main__": main()
