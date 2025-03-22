import socket
import os

# サーバのアドレスを定義します。
server_address = 'udp_socket_file'

# このクライアントのアドレスを定義します。
client_address = 'udp_client_socket_file'

# 既存のソケットファイルを削除
try:
    os.unlink(client_address)
except FileNotFoundError:
    pass

# UNIXドメインソケットとデータグラム（非接続）ソケットを作成します
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

# このクライアントのアドレスをソケットに紐付けます。
# これはUNIXドメインソケットの場合に限ります。
# このアドレスは、サーバによって送信元アドレスとして受け取られます。
sock.bind(client_address)

try:
    # サーバにメッセージを送信します
    # ユーザー入力を取得
    message = input("Enter message (or 'exit' to quit): ")

    # 'exit'と入力された場合は終了します
    if message == 'exit':
        print('Exiting...')
        exit()

    # サーバにメッセージを送信します
    sock.sendto(message.encode(), server_address)
    print(f"Sent: {message}")

    # サーバからの応答を待ち受けます
    print('waiting to receive')
    # 最大4096バイトのデータを受け取ります
    data, server = sock.recvfrom(4096)

    # サーバから受け取ったメッセージを表示します
    print('received {!r}'.format(data.decode()))

finally:
    # 最後にソケットを閉じてリソースを解放します
    print('closing socket')
    sock.close()
    os.unlink(client_address)  # 使用後にクリーンアップ