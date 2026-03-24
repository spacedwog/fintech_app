class Epic:
    def __init__(self, nome, justificativa):
        self.nome = nome
        self.justificativa = justificativa


class UserStory:
    def __init__(self, descricao, criterios):
        self.descricao = descricao
        self.criterios = criterios


class INVESTValidation:
    def __init__(self, historia, validacoes):
        self.historia = historia
        self.validacoes = validacoes


class Prioridade:
    def __init__(self, historia, justificativa):
        self.historia = historia
        self.justificativa = justificativa