class About:
  def __version__():
    return "Version\t: 0.0.01(Alpha Version)"

  def __about__():
    return "Bioinformatics Project\n\nBy : Heru Triana\n"

  def __logo__():
    print("  ___            _    _              ___       ")
    print(" | _ \ _ _  ___ | |_ (_) _ _   __ _ | _ \ _  _ ")
    print(" |  _/| '_|/ _ \|  _|| || ' \ / _` ||  _/| || |")
    print(" |_|  |_|  \___/ \__||_||_||_|\__,_||_|   \_, |")
    print("                                          |__/ ")
  
  def __all__():
    About.__logo__()
    print(About.__about__())
    print(About.__version__())