import os
import sys
import pyzipper

def encrypt_and_split(input_zip, password, part_size_mb):
    encrypted_zip = input_zip.replace('.zip', '_encrypted.zip')
    print(f"\n加密 {input_zip} 为 {encrypted_zip}...")

    with pyzipper.AESZipFile(encrypted_zip,
                              'w',
                              compression=pyzipper.ZIP_LZMA,
                              encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(password.encode())
        with open(input_zip, 'rb') as f:
            zf.writestr(os.path.basename(input_zip), f.read())
    print(f"加密完成: {encrypted_zip}")

    print("\n开始分片...")
    part_size = part_size_mb * 1024 * 1024
    with open(encrypted_zip, 'rb') as f:
        i = 1
        while chunk := f.read(part_size):
            part_file = f"{encrypted_zip}.part{i}"
            with open(part_file, 'wb') as pf:
                pf.write(chunk)
            print(f"生成分片: {part_file}")
            i += 1
    print("\n加密 + 分片完成 ✅")

def merge_and_decrypt(part_prefix, password, output_dir):
    merged_zip = 'merged_encrypted.zip'
    print(f"\n开始合并以 {part_prefix} 开头的分片...")
    part_files = sorted([f for f in os.listdir('.') if f.startswith(part_prefix)])
    if not part_files:
        print("❌ 未找到分片文件！")
        return
    with open(merged_zip, 'wb') as f:
        for part in part_files:
            with open(part, 'rb') as pf:
                f.write(pf.read())
            print(f"合并分片: {part}")
    print(f"\n合并完成: {merged_zip}")

    print(f"\n开始解密到 {output_dir}...")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with pyzipper.AESZipFile(merged_zip) as zf:
        zf.setpassword(password.encode())
        zf.extractall(output_dir)
    print(f"\n解密完成 ✅ 内容已提取到 {output_dir}/")

def menu_mode():
    while True:
        print("\n=== 文件加密分片工具 ===")
        print("[1] 加密并分片")
        print("[2] 合并并解密")
        print("[0] 退出")
        choice = input("请选择功能：")

        if choice == '1':
            input_zip = input("请输入源zip文件名（例如 data.zip）：").strip()
            password = input("请输入加密密码：").strip()
            part_size_mb = int(input("请输入分片大小（MB，比如10）：").strip())
            encrypt_and_split(input_zip, password, part_size_mb)
        elif choice == '2':
            part_prefix = input("请输入分片前缀（例如 encrypted.zip.part）：").strip()
            password = input("请输入解密密码：").strip()
            output_dir = input("请输入解压输出目录（例如 output_folder）：").strip()
            merge_and_decrypt(part_prefix, password, output_dir)
        elif choice == '0':
            print("退出程序，再见！👋")
            break
        else:
            print("无效的选择，请重新输入！")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        menu_mode()
    else:
        command = sys.argv[1]

        if command == "enc" and len(sys.argv) == 5:
            input_zip = sys.argv[2]
            password = sys.argv[3]
            part_size_mb = int(sys.argv[4])
            encrypt_and_split(input_zip, password, part_size_mb)
        elif command == "dec" and len(sys.argv) == 5:
            part_prefix = sys.argv[2]
            password = sys.argv[3]
            output_dir = sys.argv[4]
            merge_and_decrypt(part_prefix, password, output_dir)
        else:
            print("参数错误！正确用法如下：")
            print("加密+分片: python zip_tool.py enc 文件名.zip 密码 分片大小(MB)")
            print("合并+解密: python zip_tool.py dec 分片前缀 密码 输出目录")
