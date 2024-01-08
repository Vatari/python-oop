from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    def __init__(self):
        self.divers = []
        self.fish_list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        divers = {
            "ScubaDiver": ScubaDiver,
            "FreeDiver": FreeDiver
        }
        if diver_type not in ["FreeDiver", "ScubaDiver"]:
            return f"{diver_type} is not allowed in our competition."

        for diver in self.divers:
            if diver.name == diver_name:
                return f"{diver_name} is already a participant."

        new_diver = divers[diver_type](diver_name)
        self.divers.append(new_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        fishes = {
            "PredatoryFish": PredatoryFish,
            "DeepSeaFish": DeepSeaFish,
        }
        if fish_type not in ["PredatoryFish", "DeepSeaFish"]:
            return f"{fish_type} is forbidden for chasing in our competition."

        for fish in self.fish_list:
            if fish.name == fish_name:
                return f"{fish_name} is already permitted."

        new_fish = fishes[fish_type](fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = next((d for d in self.divers if d.name == diver_name), None)
        if not diver:
            return f"{diver_name} is not registered for the competition."

        fish = next((f for f in self.fish_list if f.name == fish_name), None)
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                return f"{diver_name} missed a good {fish_name}."

        diver.hit(fish)
        return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        recovered_count = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.update_health_status()
                diver.renew_oxy()
                recovered_count += 1
        return f"Divers recovered: {recovered_count}"

    def diver_catch_report(self, diver_name: str):
        diver = next((d for d in self.divers if d.name == diver_name), None)
        if not diver:
            return f"{diver_name} is not registered for the competition."

        catch_report = f"**{diver_name} Catch Report**\n"
        for fish in diver.catch:
            catch_report += fish.fish_details() + "\n"

        return catch_report.strip()

    def competition_statistics(self):
        healthy_divers = [diver for diver in self.divers if not diver.has_health_issue]
        sorted_divers = sorted(healthy_divers, key=lambda x: (x.competition_points, len(x.catch), x.name), reverse=True)

        statistics = "**Nautical Catch Challenge Statistics**\n"
        for diver in sorted_divers:
            statistics += f"{diver}\n"

        return statistics
