import flet as ft

import controller
import model as md


class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None
        self._dd = None
        self._dd2 = None
        self._txt = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here
        t = ft.Text()
        self._dd = ft.Dropdown(
            label="Select language",
            width=720,
            options=[
                ft.dropdown.Option("Italian"),
                ft.dropdown.Option("English"),
                ft.dropdown.Option("Spanish")
            ]
        )
        t2 = ft.Text()
        self._dd2 = ft.Dropdown(
            label="Select Modality",
            width=200,
            options=[
                ft.dropdown.Option("Default"),
                ft.dropdown.Option("Linear"),
                ft.dropdown.Option("Dichotomic")
            ]
        )
        self._txt = ft.TextField(
            label="Add your sentence here")
        lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

        def manageSentence(e):
            txtIn = self._txt.value.lower()
            language = self._dd.value.lower()
            modality = self._dd2.value
            (lista_parole, time) = self.__controller.handleSentence(txtIn, language, modality)
            lv.controls.append(ft.Text(f"Frase inserita: {txtIn}"))
            lv.controls.append(ft.Text(f"Parole errate: {lista_parole}"))
            lv.controls.append(ft.Text(f"Tempo richiesto dalla ricerca {time}"))
            self.page.update()

        btn = ft.ElevatedButton("Spell check", on_click=manageSentence)

        def languageChanged(e):
            t.value = f"Language selected {self._dd.value}"
            self.page.update()

        def typeSerachSelected(e):
            t2.value = f"Research selected {self._dd2.value}"

        self.page.add(ft.Row([self._dd]), ft.Row([self._dd2, self._txt, btn]), lv)

        self.page.update()

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
