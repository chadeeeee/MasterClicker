import customtkinter
from threading import Thread
from app import clicker

def setup_gui():
    app = customtkinter.CTk()
    app.title("Autoclicker")
    app.geometry("444x83")
    # app.iconbitmap('images/icon.ico')
    app.attributes("-topmost", True)
    customtkinter.set_appearance_mode("system")
    app.resizable(False, False)

    font = customtkinter.CTkFont(family="Poppins", size=16)

    start_btn = customtkinter.CTkButton(app, text="Start(F6)",
                                        fg_color="#18181B",
                                        hover_color="#2f2f31",
                                        width=200,
                                        height=40,
                                        font=font,
                                        command=clicker.toggle_auto_clicker
                                        )
    start_btn.grid(row=0, column=0, padx=9, pady=20)

    stop_btn = customtkinter.CTkButton(app, text="Stop(ESC)",
                                       fg_color="#EF4444",
                                       hover_color="#f05656",
                                       height=40,
                                       width=200,
                                       font=font,
                                       command=clicker.toggle_auto_clicker
                                       )
    stop_btn.grid(row=0, column=1, padx=19, pady=20)

    return app


def main():
    listener_thread = Thread(target=clicker.start_listener)
    listener_thread.start()

    app = setup_gui()
    app.mainloop()

    clicker.running = False
    clicker.stop_thread = True
    listener_thread.join()


if __name__ == '__main__':
    main()
