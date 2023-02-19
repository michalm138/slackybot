class SlackInitializeError(Exception):

    def __init__(self, message="Unable to initialize Slack object"):
        self.message = message
        super().__init__(self.message)
