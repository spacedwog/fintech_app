class AlertService:

    def check_budget(self, total_gasto, limite):
        if limite == 0:
            return None

        percent = total_gasto / limite

        if percent >= 1:
            return "🚨 Você ultrapassou o limite!"
        elif percent >= 0.8:
            return "⚠️ Você atingiu 80% do limite!"
        return None