from abc import ABC, abstractmethod


class Notifire(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


class SMSNotifire(Notifire):
    def __init__(self, telephone: str):
        self.telephone = telephone

    def send(self, message: str):
        print(f"SMS send. {self.telephone}, {message}")


class NotifierDecorator:
    def __init__(self, wrapper: Notifire):
        self.wrapper = wrapper

    def send(self, message: str):
        self.wrapper.send(message)


class WhatsappNotifierDecorator(NotifierDecorator):
    def __init__(self, wrapper: Notifire, whatsapp_id: str):
        super().__init__(wrapper)
        self.whatsapp_id = whatsapp_id

    def send(self, message: str):
        super().send(message)
        print(f"Send whatsapp message {message}")


class TelegramNotifierDecorator(NotifierDecorator):
    def __init__(self, wrapper: Notifire, telegram_id: str):
        super().__init__(wrapper)
        self.telegram_id = telegram_id

    def send(self, message: str):
        super().send(message)
        print(f"Send telegram message {message}")


notifier = SMSNotifire("+1234567890")
notifier = WhatsappNotifierDecorator(notifier, "123456")
notifier = TelegramNotifierDecorator(notifier, "098765")
notifier.send("Found!")
