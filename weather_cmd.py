from cmd import Cmd
from weather_api_wrapper import weatherDistro

class weather_cmd(Cmd):
    def start_distro(self,api_key):
        self.distro=weatherDistro(api_key)
    def do_today(self, args):
        """Type city name to get weather data."""
        if len(args) == 0:
            print("Please provide a city name.")
        else:
            town = args
            weather=self.distro.show_current(args)

            print(weather["weather"][0]["description"])

    def do_forecast(self, args):
        """Type city name to get weather data."""
        if len(args) == 0:
            print("Please provide a city name.")
        else:
            town = args
            print(self.distro.weekly_forecast(args))

        def do_quit(self, args):
            """Quits the program."""
            print("Quitting.")
            raise SystemExit


if __name__ == '__main__':
    prompt = weather_cmd()
    prompt.start_distro("f03d78a3f960b77051da152f008881e4")
    prompt.prompt = '> '
    prompt.cmdloop('Starting prompt... To output todays weather, use today <city name>')