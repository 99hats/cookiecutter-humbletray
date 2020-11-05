from humbletray import systray
import justpy as jp

wp = jp.WebPage()


def start_server(queue):
    wp.q = queue
    jp.Hello(a=wp)
    jp.justpy(lambda: wp)


if __name__ == "__main__":
    systray.run_gui(start_server, menu=None, fig=systray.fig_full_path, schedule=None)
