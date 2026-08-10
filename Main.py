from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
import datetime

balance = 859.0
phone = "0712345678"
bonga = 85
transactions = ["Account Created"]
pin = "1234"
logged_in = False

menu = {
    "1":"Balance","2":"Send Money","3":"Lipa","4":"Mini Statement","5":"PayBill",
    "6":"Bundles","7":"Save","8":"Withdraw","9":"Airtime","10":"Fuliza",
    "11":"M-Shwari","12":"KCB","13":"Wealth","14":"Insurance","15":"School",
    "16":"Taxes","17":"Change PIN","18":"PDF Statement","19":"Search",
    "20":"Admin","21":"Voice","22":"Bonga","23":"Graphs","24":"Banks","25":"Exit"
}

class MpesaApp(App):
    def log_tx(self, tx):
        transactions.append(f"{datetime.datetime.now().strftime('%d/%m %H:%M')} - {tx}")

    def popup(self, title, message):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=message))
        btn = Button(text='OK', size_hint_y=0.3)
        popup = Popup(title=title, content=content, size_hint=(0.8, 0.4))
        btn.bind(on_press=popup.dismiss)
        content.add_widget(btn)
        popup.open()

    def login(self, pin_input):
        global logged_in
        if pin_input.text == pin:
            logged_in = True
            self.root.clear_widgets()
            self.build_menu()
        else:
            self.popup("Error", "❌ Wrong PIN")

    def build_login(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text="WYC-MPESA V6.2 CEO EDITION", font_size=20))
        self.pin_input = TextInput(password=True, multiline=False, hint_text="Enter M-PESA PIN")
        btn = Button(text="Login")
        btn.bind(on_press=lambda x: self.login(self.pin_input))
        layout.add_widget(self.pin_input)
        layout.add_widget(btn)
        return layout

    def build_menu(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=5)
        header = Label(text=f"Balance: Ksh {balance:.2f} | Bonga: {bonga} pts | {phone}", size_hint_y=0.2)
        layout.add_widget(header)

        scroll = ScrollView()
        grid = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)
        grid.bind(minimum_height=grid.setter('height'))

        for k,v in menu.items():
            btn = Button(text=f"{k}. {v}", size_hint_y=None, height=40)
            btn.bind(on_press=lambda x, key=k: self.handle_choice(key))
            grid.add_widget(btn)
        scroll.add_widget(grid)
        layout.add_widget(scroll)
        self.root.add_widget(layout)

    def handle_choice(self, choice):
        global balance, bonga
        if choice == "1":
            self.popup("Balance", f"Balance: Ksh {balance:.2f}")
        elif choice == "2":
            self.popup("Send Money", "Send Money feature loaded")
        elif choice == "22":
            self.popup("Bonga", f"Bonga Points: {bonga}. Earn 1pt per Ksh 10")
        elif choice == "24":
            self.popup("Bank Transfer", "Bank Transfer feature loaded")
        elif choice == "18":
            self.pdf_statement()
        elif choice == "19":
            self.popup("Search", "Search feature loaded")
        elif choice == "20":
            self.popup("Admin", "Admin Panel - Use code 9999")
        elif choice == "25":
            App.get_running_app().stop()
        else:
            self.popup(menu[choice], f"✅ {menu[choice]} - Service Active")

    def pdf_statement(self):
        with open("mpesa_statement.txt", "w") as f:
            f.write("WYC-MPESA STATEMENT\n")
            for tx in transactions[-10:]:
                f.write(tx+"\n")
        self.popup("PDF", "✅ Statement Saved")

    def build(self):
        self.root = BoxLayout()
        self.root.add_widget(self.build_login())
        return self.root

if __name__ == '__main__':
    MpesaApp().run()
