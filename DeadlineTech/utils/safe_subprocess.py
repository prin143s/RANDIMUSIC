import asyncio

async def safe_shell(cmd):
    try:
        proc = await asyncio.create_subprocess_shell(
            cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        out, err = await proc.communicate()
        return out, err
    except FileNotFoundError:
        print(f"[WARN] Command not found: {cmd}")
        return None, None
    except Exception as e:
        print(f"[ERROR] Subprocess failed: {e}")
        return None, None


async def safe_exec(cmd_list):
    try:
        proc = await asyncio.create_subprocess_exec(
            *cmd_list,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        out, err = await proc.communicate()
        return out, err
    except FileNotFoundError:
        print(f"[WARN] Command not found: {' '.join(cmd_list)}")
        return None, None
    except Exception as e:
        print(f"[ERROR] Subprocess failed: {e}")
        return None, None
