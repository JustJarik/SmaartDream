from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.list import MDListItem, MDListItemHeadlineText, MDListItemSupportingText
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogSupportingText
from kivymd.uix.screen import MDScreen

class MainApp(MDApp):
    def pervui(self, text):
        obhod = text
        screen896767867 = MDDialog(MDDialogHeadlineText(text='Первый способ'), MDDialogSupportingText(text=
        'Лечь на спину\n'
        'Дышать в следующем ритме: вдох - считаем 4 секунды, выдох – считаем 4 секунды, и так по кругу.\n' 
        'Засыпая, вы почувствуете, что-то неладное, это и есть ваше дыхание. Необходимо представить что вы сели на велосипед и едете с горки на большой скорости. '
        'Так вы и окажетесь в мире снов'))
        screen896767867.open()
        return screen896767867
    def vtoroi(self, text):
        obhod=text
        screen896767868 = MDDialog(MDDialogHeadlineText(text='Второй способ'),MDDialogSupportingText(text=
        'Если вы уже спите, то во сне можно попробовать сделать то, что для настоящего мира будет странным:\n'
        'Пропустить руку сквозь твердый объект\n'
        'Сжать твердый объект\n'
        'Прыгнуть\n'
        'Посмотреть на часы\n'
        'Прочитать текст\n'
        'Посмотреть на руки\n'
        'Посмотреть в зеркало\n'
        'Задать вопрос: «как я сюда попал(а)?»'))
        screen896767868.open()
        return screen896767868

    def tretii(self, text):
        obhod = text
        screen896767869 = MDDialog(MDDialogHeadlineText(text='Третий способ'), MDDialogSupportingText(text=
        'Установите будильник, отсчитав пять часов с момента потенциального засыпания.\n'
        'После пробуждения не совершайте резких движений и сконцентрируйтесь на воспоминаниях о только что приснившемся.'
        ' Если «ничего не снилось» можно вспомнить любой другой сон, даже из детства\n'
        'Расслабьтесь и сконцентрируйтесь на намерении осознать себя во сне\n'
        'Представьте себя в том сне, внушайте, что все вокруг нереально.\n'
        'Повтор предыдущих двух пунктов, до полного погружения'))
        screen896767869.open()
        return screen896767869

    def chetire(self, text):
        obhod = text
        screen896767860 = MDDialog(MDDialogHeadlineText(text='Четвертый способ'), MDDialogSupportingText(text=
        'Можно записывать свои сны на бумагу и перед сном быстро проходится по их сюжету,'
        ' может случится так, что сон повторится, произойдет конфликт, и ваше сознание включится'))
        screen896767860.open()
        return screen896767860
    def pyat(self, text):
        obhod = text
        screen896767861 = MDDialog(MDDialogHeadlineText(text='Как запоминать сны?'), MDDialogSupportingText(text=
        'Придерживайтесь единого режима сна, засыпайте и просыпайтесь в одно и тоже время. '
        'Не принимайте седативных веществ(снотворное и подобные сильные вещества, ромашку или чай можно)'
        'Проветривайте помещение, в котором спите'
        'Начните вести дневник снов, можете в него записать старые сны и кошмары, которые вы помните'))
        screen896767861.open()
        return screen896767861

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Olive"  # "Purple", "Red"
        grid = MDGridLayout(cols=1)
        mdnazvne = MDLabel(text='Умный будильник', halign='center')
        mdpusto1 = MDLabel(text='')
        mdpusto2 = MDLabel(text='')
        mdpusto3 = MDLabel( text='')
        mdpusto4 = MDLabel(text='')
        sps1=MDListItem(MDButton(MDButtonText(text='подробнее'),
                                 on_release=self.pervui), MDListItemHeadlineText(text="Первый способ"),
                        MDListItemSupportingText(text="Во время засыпания"))
        sps2=MDListItem(MDButton(MDButtonText(text='подробнее'),
                                 on_release=self.vtoroi), MDListItemHeadlineText(text="Второй способ"),
                        MDListItemSupportingText(text="Во время сна"))
        sps3=MDListItem(MDButton(MDButtonText(text='подробнее'),
                                 on_release=self.tretii), MDListItemHeadlineText(text="Третий способ"),
                        MDListItemSupportingText(text="До засыпания/во сне"))
        sps4=MDListItem(MDButton(MDButtonText(text='подробнее'),
                                 on_release=self.chetire), MDListItemHeadlineText(text="Четвертый способ"),
                        MDListItemSupportingText(text="До засыпания"))
        sps5=MDListItem(MDButton(MDButtonText(text='подробнее'),
                                 on_release=self.pyat), MDListItemHeadlineText(text='Как запоминать сны'),
                        MDListItemSupportingText(text="Подборка советов"))

        grid.add_widget(mdnazvne)
        grid.add_widget(sps1)
        grid.add_widget(sps2)
        grid.add_widget(sps3)
        grid.add_widget(sps4)
        grid.add_widget(sps5)
        grid.add_widget(mdpusto1)
        grid.add_widget(mdpusto2)
        grid.add_widget(mdpusto3)
        grid.add_widget(mdpusto4)
        return grid
MainApp().run()