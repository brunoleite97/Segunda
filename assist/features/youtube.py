import pywhatkit as kit


def yt_play(*arg, **kwargs):
    inp_command = kwargs.get("query")
    kit.playonyt('the pretender foof fighters')
    return "Playing Video on Youtube"


if __name__ == "__main__":
    yt_play('play on youtube shape of you')
