import hashlib
import json
import os
import time

# Đường dẫn thư mục chứa các file dang*.py (nếu để cùng thư mục thì dùng ".")
FOLDER_DANG = "."


def tinh_md5(file_path):
    hasher = hashlib.md5()
    with open(file_path, "rb") as f:
        hasher.update(f.read())
    return hasher.hexdigest()


def tao_manifest():
    manifest = {
        "version": int(time.time()),
        "updated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "files": {},
    }

    count = 0
    for fname in os.listdir(FOLDER_DANG):
        # Lọc đúng các file dạng toán đuôi .py
        if fname.startswith("dang") and fname.endswith(".py"):
            fpath = os.path.join(FOLDER_DANG, fname)
            key = fname[:-3]  # Lấy tên dạng, bỏ đuôi .py
            manifest["files"][key] = tinh_md5(fpath)
            count += 1

    with open("manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(
        f"[Hoàn tất] Đã băm MD5 cho {count} file dạng toán vào 'manifest.json'."
    )


if __name__ == "__main__":
    tao_manifest()