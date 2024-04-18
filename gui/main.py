import tkinter

import customtkinter
from threading import Thread
from app import clicker, bind, about


def setup_gui():
    app = customtkinter.CTk()
    app.title("MasterClicker")
    app.geometry("448x165")
    app.attributes("-topmost", True)
    customtkinter.set_appearance_mode("system")
    # app.resizable(False, False)

    font = customtkinter.CTkFont(family="Poppins", size=16)

    start_btn = customtkinter.CTkButton(app,
                                        text="Start(F9)",
                                        fg_color="#18181B",
                                        hover_color="#2f2f31",
                                        text_color="#FFFFFF",
                                        width=200,
                                        height=40,
                                        font=font,
                                        command=clicker.toggle_auto_clicker
                                        )
    start_btn.grid(row=0, column=0, padx=7, pady=20)

    stop_btn = customtkinter.CTkButton(app,
                                       text="Stop(F9)",
                                       fg_color="#EF4444",
                                       hover_color="#f05656",
                                       text_color="#FFFFFF",
                                       height=40,
                                       width=200,
                                       font=font,
                                       command=clicker.toggle_auto_clicker
                                       )
    stop_btn.grid(row=0, column=1, padx=12, pady=20)

    line_width = 210 + 150 + 30 + 100
    line = tkinter.Canvas(app, height=1, width=400, bg="#E4E4E7", highlightthickness=0)
    line.grid(row=1, column=0, columnspan=2)
    line.create_line(0, 0, line_width, 0, fill="#E4E4E7", width=1)

    hotkey = customtkinter.CTkButton(app,
                                    text="Bind hotkeys",
                                    fg_color="#FFFFFF",
                                    hover_color="#E4E4E7",
                                    text_color="#000000",
                                    height=40,
                                    width=200,
                                    font=font,
                                    command=bind.rebind
                                    )
    hotkey.grid(row=2, column=0, pady=25, padx=12)

    info = customtkinter.CTkButton(app,
                                     text="About",
                                     fg_color="#FFFFFF",
                                     hover_color="#E4E4E7",
                                     text_color="#000000",
                                     height=40,
                                     width=200,
                                     font=font,
                                     command=about.show_about
                                     )
    info.grid(row=2, column=1, pady=25, padx=12)


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
