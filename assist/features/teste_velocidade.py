import speedtest

try:
    st = speedtest.Speedtest()
except:
    print("Please check your internet connection.")
    pass


def velocidade_de_download():
    down = round(st.download() / 10 ** 6, 2)
    return down


def velocidade_de_upload():
    up = round(st.upload() / 10 ** 6, 2)
    return up


def ping():
    servernames = []
    st.get_servers(servernames)
    results = st.results.ping
    return results


def speed_test(*args, **kwargs):
    try:
        print("Checking internet speed. Please wait...")
        return "Velocidade de download: " + str(velocidade_de_download()) + "MB/s" + "\n Velocidade de Upload: " + str(
            velocidade_de_upload()) + " MB/s" + "\n Ping: " + str(ping()) + " ms"
    except Exception as e:
        print(e)
        return "Error in internet speed test"


if __name__ == '__main__':
    print(speed_test())
