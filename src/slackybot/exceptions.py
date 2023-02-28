class SlackInitializeError(Exception):

    def __init__(self, message="Unable to initialize Slack object"):
        self.message = message
        super().__init__(self.message)


class MessageNotSend(Exception):

    def __init__(self, message="The message has not been sent"):
        self.message = message
        super().__init__(self.message)


class MessageNotUpdated(Exception):

    def __init__(self, message="The message has not been updated"):
        self.message = message
        super().__init__(self.message)


class NotASlackMessage(Exception):

    def __init__(self, message="Given value is not a SlackMessage object"):
        self.message = message
        super().__init__(self.message)
